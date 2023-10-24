from ML_KEM.parameters import MLKEM_512 as params
from ML_KEM.helpers import poly_add

from ML_KEM.Auxiliary.ConversionCompression import ByteEncode, ByteDecode, Decompress, Compress
from ML_KEM.Auxiliary.CryptoFunctions import PRF, XOF
from ML_KEM.Auxiliary.NTT import NTT, NTTINV, MultiplyNTTs
from ML_KEM.Auxiliary.Sampling import SampleNTT, SamplePolyCBD

from rich import print
from rich.panel import Panel

def Encrypt(ekPKE: bytes, m: bytes, r: bytes) -> bytes:
    if len(ekPKE) != params.ekPKElen:
        raise ValueError(f'ekPKE should be of length {384 * params.k + 32}, actual length: {len(ekPKE) } bytes, needs to be ')
    if len(m) != 32:
        raise ValueError(f'm should be of length 32, actual length: {len(m)}')
    if len(r) != 32:
        raise ValueError(f'r should be of length 32, actual length: {len(r)}')
    
    N = 0
    t = [[None] for i in range(0, params.k)]
    p = ekPKE[384*params.k : 384*params.k+32]
    Ah = [[[[None] * 256] for i in range(0, params.k)] for j in range(0, params.k)]
    rr = [[None] for i in range(0, params.k)]
    rrh = [[None] for i in range(0, params.k)]
    u = [[None] for i in range(0, params.k)]
    v = [[None] for i in range(0, params.k)]
    e1 = [[None] for i in range(0, params.k)]
    e2 = [None] * 256

    for i in range(0, params.k):
        t[i] = ByteDecode(12, ekPKE[(i * 384) : 384 * (i + 1)])

    for i in range(0, params.k):
        for j in range(0, params.k):
            xof = XOF(p, i.to_bytes(1, 'big'), j.to_bytes(1, 'big'))   
            Ah[i][j] = SampleNTT(xof(672))

    for i in range(0, params.k):
        rr[i] = SamplePolyCBD(params.n1, PRF(params.n1, r, N.to_bytes(1, 'big')))
        N += 1 
    for i in range(0, params.k):
        e1[i] = SamplePolyCBD(params.n2, PRF(params.n2, r, N.to_bytes(1, 'big')))
        N += 1

    e2 = SamplePolyCBD(params.n2, PRF(params.n2, r, N.to_bytes(1, 'big')))

    for idx, l in enumerate(rr):
        rrh[idx] = NTT(l)

    for i in range(0, params.k):
        tmp = [[None] for _ in range(0, params.k)]
        for j in range(0, params.k):
            tmp[j] = MultiplyNTTs(Ah[j][i], rrh[j])
        for j in range(0, params.k - 1):
            u[i] = poly_add(tmp[j], tmp[j+1])
        u[i] = NTTINV(u[i])
        u[i] = poly_add(u[i], e1[i])

    mu = Decompress(1, ByteDecode(1, m))

    tmp = [[None] for _ in range(0, params.k)]
    for i in range(0, params.k):
        tmp[i] = MultiplyNTTs(t[0], rrh[i])

    v = poly_add(tmp[0], tmp[1])
    v = NTTINV(v)
    v = poly_add(v, e2)
    v = poly_add(v, mu)

    c1 = b''
    for i in range(0, params.k):
        c1 += ByteEncode(params.du, (Compress(params.du, u[i])))
    
    c2 = ByteEncode(params.dv, Compress(params.dv, v))

    print()
    print(Panel(c1.hex(), title='c1', subtitle=f'{len(c1)} bytes, {len(c1) * 8} bits'))
    print()
    print(Panel(c2.hex(), title='c2', subtitle=f'{len(c2)} bytes, {len(c2) * 8} bits'))

    return c1 + c2
    
    
