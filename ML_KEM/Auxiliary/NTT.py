
from ML_KEM.helpers import modq
import ML_KEM.parameters as params

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
            kr = BitRev7(k)
            zeta = params.z**kr 
            zeta = modq(zeta)
            k += 1

            for j in range(start, start + length):
                t = zeta * fh[j+length]
                t = modq(t)
                fh[j+length] = fh[j]-t
                fh[j+length] = modq(fh[j+length])
                fh[j] = fh[j]+t
                fh[j] = modq(fh[j])
        length = length // 2
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
            zeta = params.z**kr
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
        zeta = 2*BitRev7_2(i) + 1
        zeta = params.z**zeta
        zeta = modq(zeta)

        h[2*1], h[2*i+1] = BaseCaseMultiply(fh[2*i], fh[2*i+1], gh[2*i], gh[2*i+1], zeta)
    
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