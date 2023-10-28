
from ML_KEM.helpers import modq, montgomery_reduce, barret_reduce
from ML_KEM.parameters import params

zetas = [
  -1044,  -758,  -359, -1517,  1493,  1422,   287,   202,
   -171,   622,  1577,   182,   962, -1202, -1474,  1468,
    573, -1325,   264,   383,  -829,  1458, -1602,  -130,
   -681,  1017,   732,   608, -1542,   411,  -205, -1571,
   1223,   652,  -552,  1015, -1293,  1491,  -282, -1544,
    516,    -8,  -320,  -666, -1618, -1162,   126,  1469,
   -853,   -90,  -271,   830,   107, -1421,  -247,  -951,
   -398,   961, -1508,  -725,   448, -1065,   677, -1275,
  -1103,   430,   555,   843, -1251,   871,  1550,   105,
    422,   587,   177,  -235,  -291,  -460,  1574,  1653,
   -246,   778,  1159,  -147,  -777,  1483,  -602,  1119,
  -1590,   644,  -872,   349,   418,   329,  -156,   -75,
    817,  1097,   603,   610,  1322, -1285, -1465,   384,
  -1215,  -136,  1218, -1335,  -874,   220, -1187, -1659,
  -1185, -1530, -1278,   794, -1510,  -854,  -870,   478,
   -108,  -308,   996,   991,   958, -1460,  1522,  1628
]

def BitRev7(i: int) -> int:
    return int('{:07b}'.format(i)[::-1], 2)

def BitRev7_2(i: int) -> int:
    i = i & (2**7-1)
    ii = 0
    for j in range(0, 3):
        ii |= ((i >> 6 - j) & 1) << j
        ii |= ((i >> j) & 1) << 6 - j
    return ii

def NTT(f: list) -> list:
    if len(f) != 256:
        raise ValueError('f must be of length 256')
    fh = f.copy()
    k = 1
    length = 128
    while length >= 2:
        start = 0
        for start in range(0, 256, start+2*length):
            if params.MATCH_CREF_OUTPUTS:
                zeta = zetas[k]
            else:
                kr = BitRev7(k)
                zeta = params.z**kr 
                zeta = modq(zeta)
            k += 1

            for j in range(start, start + length):
                t = zeta * fh[j+length]
                if params.MATCH_CREF_OUTPUTS:
                    t = montgomery_reduce(t)
                else:
                    t = modq(t)
                fh[j+length] = fh[j]-t
                # fh[j+length] = modq(fh[j+length])
                fh[j] = fh[j]+t
                # fh[j] = modq(fh[j])
        length = length // 2
    for i in range(0, params.MLKEM_PARAMS.n):
        if params.MATCH_CREF_OUTPUTS:
            fh[i] = barret_reduce(fh[i])
        else:
            fh[i] = modq(fh[i])
    return fh

def NTTINV(fh: list) -> list:
    if len(fh) != 256:
        raise ValueError('fh must be of length 256')
    f = fh.copy()
    k = 127
    length = 2
    while length <= 128:
        start = 0
        for start in range(start, 256, start+2*length):
            kr = BitRev7_2(k)
            zeta = params.MLKEM_PARAMS.z**kr
            zeta = modq(zeta)
            k -= 1

            for j in range(start, start+length):
                t = f[j]
                f[j] = t + f[j+length]
                f[j] = modq(f[j])
                f[j+length] = f[j+length] - t
                f[j+length] = f[j+length] * zeta
                f[j+length] = modq(f[j+length])
        length = length * 2
    for i in range(len(f)):
        f[i] = f[i] * 3303
        f[i] = modq(f[i])
    return f

def MultiplyNTTs(fh: list, gh: list) -> list:
    if len(fh) != 256:
        raise ValueError('fh must be of length 256')
    if len(gh) != 256:
        raise ValueError('gh must be of length 256')
    
    h = [0] * 256
    for i in range(0, 128):
        zeta = 2*BitRev7(i) + 1
        zeta = params.MLKEM_PARAMS.z**zeta
        zeta = modq(zeta)

        h[2*i], h[2*i+1] = BaseCaseMultiply(fh[2*i], fh[2*i+1], gh[2*i], gh[2*i+1], zeta)
    
    return h
    

def BaseCaseMultiply(a0: int, a1: int, b0: int, b1: int, gamma: int) -> (int, int):
    c0_1 = a0 * b0
    c0_2 = a1 * b1 * gamma
    c0   = c0_1 + c0_2
    c0   = modq(c0)

    c1_1 = a0 * b1
    c1_2 = a1 * b0
    c1   = c1_1 + c1_2
    c1   = modq(c1)

    return (c0, c1)