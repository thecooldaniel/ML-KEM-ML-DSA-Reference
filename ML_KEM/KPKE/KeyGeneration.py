from os import urandom

from ML_KEM.helpers import poly_add, modq
from ML_KEM.parameters import params

from ML_KEM.Auxiliary.ConversionCompression import ByteEncode
from ML_KEM.Auxiliary.CryptoFunctions import G, PRF, XOF
from ML_KEM.Auxiliary.NTT import NTT, MultiplyNTTs
from ML_KEM.Auxiliary.Sampling import SampleNTT, SamplePolyCBD

from rich import print
from rich.panel import Panel

refv = params.MLKEM_RFVALS.keygen
mlkem_k = params.MLKEM_PARAMS.k
mlkem_n1 = params.MLKEM_PARAMS.n1

def KeyGen(d: bytes=None) -> (bytes, bytes):

    # FIPS203 A12 K-PKE.KeyGen() 
    # Line 1
    if d is None:
        d = urandom(32) 
        # In hardware, required randomness provided by the "user" over a bus
        #   - random data provided via function in testbench
        #   - think of these external busses as an 'API'
    if(params.MATCH_CREF_OUTPUTS):
        d = params.MLKEM_RFVALS.keygen.seed

    N = 0
    Ah = [[[[None] * 256] for i in range(0, mlkem_k)] for j in range(0, mlkem_k)]
    s = [[None] for i in range(0, mlkem_k)]
    e = [[None] for i in range(0, mlkem_k)]
    sh = [[None] for i in range(0, mlkem_k)]
    eh = [[None] for i in range(0, mlkem_k)]
    t = [[None] for i in range(0, mlkem_k)]

    # FIPS203 A12 K-PKE.KeyGen() 
    # Line 2
    p, sigma = G(d)

    if(params.MATCH_CREF_OUTPUTS):
        assert(refv.c_hash_g == int.from_bytes(p + sigma, 'big'))

    # FIPS203 A12 K-PKE.KeyGen() 
    # Lines 4-8
    for i in range(0, mlkem_k):
        for j in range(0, mlkem_k):
            xof = XOF(p, i.to_bytes(1, 'big'), j.to_bytes(1, 'big'))   
            Ah[i][j] = SampleNTT(xof(672))
            # QUESTION: How to know how much to sample here?
            # In hardware, you have full output available after the shake process has concluded
            # Keccakf1600: in hardware: 1600 bits in, 1600 bits out
            # Shake128: Protocol determined by how you pad the input
            #   - only 1344/1600 bits are "read"
            #   - 3 rounds of XOF = 1344*3 bits 
            #       - 0.0083 % failure for 3 rounds
            #       - 2e-32 % failure for 4 rounds = 4 * 1344 bits <-- choose this to be safe
            #       - 1344 * 4 = 672 bytes
            # TODO: Create quick presentation for Mojtaba on Keccak, configurations, inputs, etc
            # TODO: Run 'high performance' Vivado package from Keccak team
            # TODO: Compare output of Keccak with Vivado output

    if(params.MATCH_CREF_OUTPUTS):
        for i in range(0, mlkem_k):
            for i in range(0, mlkem_k):
                assert(Ah[i][j] == refv.AC[i][j])

    # FIPS203 A12 K-PKE.KeyGen() 
    # Lines 9-11
    for i in range(0, mlkem_k):
        s[i] = SamplePolyCBD(mlkem_n1, PRF(mlkem_n1, sigma, N.to_bytes(1, 'big')))
        N += 1

    # FIPS203 A12 K-PKE.KeyGen() 
    # Lines 13-15
    for i in range(0, mlkem_k):
        e[i] = SamplePolyCBD(mlkem_n1, PRF(mlkem_n1, sigma, N.to_bytes(1, 'big')))
        N += 1

    if(params.MATCH_CREF_OUTPUTS):
        for i in range(0, mlkem_k):
            for j in range(0, 256):
                assert(refv.SC[i][j] == s[i][j])
                assert(refv.EC[i][j] == e[i][j])
    
    # FIPS203 A12 K-PKE.KeyGen() 
    # Line 17
    for idx, l in enumerate(s):
        sh[idx] = NTT(l)

    # FIPS203 A12 K-PKE.KeyGen() 
    # Line 18
    for idx, l in enumerate(e):
        eh[idx] = NTT(l)

    if(params.MATCH_CREF_OUTPUTS):
        for i in range(0, mlkem_k):
            for j in range(0, 256):
                assert(refv.SHC[i][j] == sh[i][j])
                assert(refv.EHC[i][j] == eh[i][j])

#   A is a k * k matrix
#   s is a k * 1 matrix
#   A*s is a k * 1 matrix
#   A*s+e is a k * 1 matrix

#   |     A     |   |  s  |   |  e  |
#   | :-- | :-- |   | :-- |   | :-- |
#   | 0,0 | 0,1 |   |  0  |   |  0  |
#   | 1,0 | 1,1 |   |  1  |   |  1  |

#   |             A * s             |
#   | :---------------------------- |
#   | A[0,0] * s[0] + A[0,1] * s[1] |
#   | A[1,0] * s[0] + A[1,1] * s[1] |

#   |     As+e     |
#   | :----------- |
#   | As[0] + e[0] |
#   | As[1] + e[1] |

    # t = A * s
    # FIPS203 A12 K-PKE.KeyGen() 
    # Line 19A
    for i in range(0, mlkem_k):
        tmp = [[None] for _ in range(0, mlkem_k)]
        for j in range(0, mlkem_k):
            tmp[j] = MultiplyNTTs(Ah[i][j], sh[j])
        for j in range(0, mlkem_k - 1):
            t[i] = poly_add(tmp[j], tmp[j+1])

    # if(params.MATCH_CREF_OUTPUTS):
    #     for i in range(0, mlkem_k):
    #         for j in range(0, 256):
    #             tmp = ASC512[i][j]
    #             if(tmp < 0):
    #                 tmp += params.q
    #             assert(t[i][j] == tmp) 

    # montgomey_reduce is used for all base multiplications during NTT in C ref

    # t = A * s + e
    # FIPS203 A12 K-PKE.KeyGen() 
    # Line 19B
    for i in range(0, mlkem_k):
        t[i] = poly_add(t[i], eh[i])

    if(params.MATCH_CREF_OUTPUTS):
        for i in range(0, mlkem_k):
            for j in range(0, 256):
                tmp = refv.ASEC[i][j]
                if(tmp < 0):
                    tmp += params.MLKEM_PARAMS.q
                assert(t[i][j] == tmp) 

    # FIPS203 A12 K-PKE.KeyGen() 
    # Line 20
    # Create the Encapsulation key
    ekPKE = ByteEncode(12, t[0])
    for i in range(1, mlkem_k):
        ekPKE += ByteEncode(12, t[i])
    ekPKE += p

    # FIPS203 A12 K-PKE.KeyGen() 
    # Line 21
    # Create the Decapsulation key
    dkPKE = ByteEncode(12, sh[0])
    for i in range(1, mlkem_k):
        dkPKE += ByteEncode(12, sh[i])

    assert(len(ekPKE) == params.MLKEM_PARAMS.ekPKElen)
    assert(len(dkPKE) == params.MLKEM_PARAMS.dkPKElen)

    if(params.MATCH_CREF_OUTPUTS):
        assert(dkPKE == refv.SKPC)
        assert(ekPKE == refv.PKPC)

    print()
    print(Panel(ekPKE.hex(), title='ek_PKE', subtitle=f'{len(ekPKE)} bytes, {len(ekPKE) * 8} bits'))
    print()
    print(Panel(dkPKE.hex(), title='dk_PKE', subtitle=f'{len(dkPKE)} bytes, {len(dkPKE) * 8} bits'))

    return (ekPKE, dkPKE)


