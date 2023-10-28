from ML_KEM.parameters import params
from ML_KEM.helpers import poly_add

from ML_KEM.Auxiliary.ConversionCompression import ByteEncode, ByteDecode, Decompress, Compress
from ML_KEM.Auxiliary.CryptoFunctions import PRF, XOF
from ML_KEM.Auxiliary.NTT import NTT, NTTINV, MultiplyNTTs
from ML_KEM.Auxiliary.Sampling import SampleNTT, SamplePolyCBD

from rich import print
from rich.panel import Panel

refv = params.MLKEM_RFVALS.encrypt
mlkem_k = params.MLKEM_PARAMS.k
mlkem_n1 = params.MLKEM_PARAMS.n1
mlkem_n2 = params.MLKEM_PARAMS.n2
mlkem_du = params.MLKEM_PARAMS.du
mlkem_dv = params.MLKEM_PARAMS.dv

def Encrypt(ekPKE: bytes, m: bytes, r: bytes) -> bytes:
    if len(ekPKE) != params.MLKEM_PARAMS.ekPKElen:
        raise ValueError(f'ekPKE should be of length {384 * mlkem_k + 32}, actual length: {len(ekPKE) } bytes, needs to be ')
    if len(m) != 32:
        raise ValueError(f'm should be of length 32, actual length: {len(m)}')
    if len(r) != 32:
        raise ValueError(f'r should be of length 32, actual length: {len(r)}')
    
    N = 0
    t = [[None] for i in range(0, mlkem_k)]
    p = ekPKE[384*mlkem_k : 384*mlkem_k+32]
    Ah = [[[[None] * 256] for i in range(0, mlkem_k)] for j in range(0, mlkem_k)]
    rr = [[None] for i in range(0, mlkem_k)]
    rrh = [[None] for i in range(0, mlkem_k)]
    u = [[None] for i in range(0, mlkem_k)]
    v = [[None] for i in range(0, mlkem_k)]
    e1 = [[None] for i in range(0, mlkem_k)]
    e2 = [None] * 256

    for i in range(0, mlkem_k):
        t[i] = ByteDecode(12, ekPKE[(i * 384) : 384 * (i + 1)])

    if(params.MATCH_CREF_OUTPUTS):
        for i in range(0, mlkem_k):
            for j in range(0, 256):
                assert(t[i][j] == refv.PKC[i][j])

    for i in range(0, mlkem_k):
        for j in range(0, mlkem_k):
            xof = XOF(p, i.to_bytes(1, 'big'), j.to_bytes(1, 'big'))   
            Ah[i][j] = SampleNTT(xof(672))

    for i in range(0, mlkem_k):
        rr[i] = SamplePolyCBD(mlkem_n1, PRF(mlkem_n1, r, N.to_bytes(1, 'big')))
        N += 1 
    for i in range(0, mlkem_k):
        e1[i] = SamplePolyCBD(mlkem_n2, PRF(mlkem_n2, r, N.to_bytes(1, 'big')))
        N += 1

    e2 = SamplePolyCBD(mlkem_n2, PRF(mlkem_n2, r, N.to_bytes(1, 'big')))

    for idx, l in enumerate(rr):
        rrh[idx] = NTT(l)

    for i in range(0, mlkem_k):
        tmp = [[None] for _ in range(0, mlkem_k)]
        for j in range(0, mlkem_k):
            tmp[j] = MultiplyNTTs(Ah[j][i], rrh[j])
        for j in range(0, mlkem_k - 1):
            u[i] = poly_add(tmp[j], tmp[j+1])
        u[i] = NTTINV(u[i])
        u[i] = poly_add(u[i], e1[i])

    mu = Decompress(1, ByteDecode(1, m))

    tmp = [[None] for _ in range(0, mlkem_k)]
    for i in range(0, mlkem_k):
        tmp[i] = MultiplyNTTs(t[0], rrh[i])

    v = poly_add(tmp[0], tmp[1])
    v = NTTINV(v)
    v = poly_add(v, e2)
    v = poly_add(v, mu)

    c1 = b''
    for i in range(0, mlkem_k):
        c1 += ByteEncode(mlkem_du, (Compress(mlkem_du, u[i])))
    
    c2 = ByteEncode(mlkem_dv, Compress(mlkem_dv, v))

    print()
    print(Panel(c1.hex(), title='c1', subtitle=f'{len(c1)} bytes, {len(c1) * 8} bits'))
    print()
    print(Panel(c2.hex(), title='c2', subtitle=f'{len(c2)} bytes, {len(c2) * 8} bits'))

    return c1 + c2
    
    
