from ML_KEM.parameters import q
from ML_KEM.helpers import modq
from ML_KEM.Auxiliary.ConversionCompression import BytesToBits

def SampleNTT(B: bytes) -> list:
    if len(B) < 256 * 2:
        raise ValueError(f'B must be at least of length {256 * 2}')
    i = 0
    j = 0
    a = [0] * 256
    while j < 256:
        d1_1 = B[i+1] % 16
        d1_2 = d1_1 * 256
        d1   = B[i] + d1_2

        d2_1 = B[i+1] // 16
        d2_2 = B[i+2] * 16
        d2   = d2_1 + d2_2

        if d1 < q:  
            a[j] = d1
            j += 1
        if d2 < q and j < 256:
            a[j] = d2
            j += 1
        i += 3
    return a

def SamplePolyCBD(n: int, B: bytes) -> list:
    if len(B) != 64 * n:
        raise ValueError(f'B must be of length {64 * n}')
    if n not in [2,3]:
        raise ValueError('n neither 2 or 3')

    b = BytesToBits(B)
    f = [0] * 256
    for i in range(0, 256):
        x = 0
        y = 0
        for j in range(0, n):
            x1 = b >> (2*i*n + j)
            x2 = x1 & 1
            x += x2
            
            y1 = b >> (2*i*n + n + j)
            y2 = y1 & 1
            y += y2

        f1 = x - y
        f2 = modq(f1)
        f[i] = f2
    return f