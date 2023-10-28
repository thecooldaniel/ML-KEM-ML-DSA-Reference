from ML_KEM.parameters import MLKEM_512 as kparams
from ML_KEM.helpers import poly_add, poly_sub

from ML_KEM.Auxiliary.ConversionCompression import ByteEncode, ByteDecode, Decompress, Compress
from ML_KEM.Auxiliary.CryptoFunctions import PRF, XOF
from ML_KEM.Auxiliary.NTT import NTT, NTTINV, MultiplyNTTs
from ML_KEM.Auxiliary.Sampling import SampleNTT, SamplePolyCBD

from rich import print
from rich.panel import Panel

def Decrypt(dkPKE: bytes, c: bytes) -> bytes:
    c1 = c[:kparams.c1len]
    c2 = c[kparams.c1len : kparams.c1len + kparams.c2len]
    u = [[None] for i in range(0, kparams.k)]
    sh = [[None] for i in range(0, kparams.k)]

    for i in range(0, kparams.k):
        slice_s = 32 * kparams.du * i
        slice_e = 32 * kparams.du * (i + 1)
        u[i] = Decompress(kparams.du, ByteDecode(kparams.du, c1[slice_s:slice_e]))

    v = Decompress(kparams.dv, ByteDecode(kparams.dv, c2))

    for i in range(0, kparams.k):
        slice_s = (kparams.dkPKElen // 2) * i
        slice_e = (kparams.dkPKElen // 2) * (i + 1)
        sh[i] = ByteDecode(12, dkPKE[slice_s:slice_e])

    tmp = [[None] for i in range(0, kparams.k)]
    for i in range(0, kparams.k):
        u[i] = NTT(u[i])
        # inv_i = params.k - i - 1
        tmp[i] = MultiplyNTTs(sh[i], u[i])


    w = poly_add(tmp[0], tmp[1])
    w = NTTINV(w)
    w = poly_sub(v, w)

    m = ByteEncode(1, Compress(1, w))

    return m