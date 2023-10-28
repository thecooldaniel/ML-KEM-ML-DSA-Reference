from ML_KEM.parameters import params
from ctypes import c_int16

def modq(n: int) -> int:
    return n % params.MLKEM_PARAMS.q

def poly_add(a: list, b: list) -> list:
    if len(a) != len(b):
        raise ValueError("length of 'a' must match length of 'b'")
    r = []
    for i in range(0, len(a)):
        r.append(modq((a[i] + b[i])))
    return r

def poly_sub(a: list, b: list) -> list:
    if len(a) != len(b):
        raise ValueError("length of 'a' must match length of 'b'")
    r = []
    for i in range(0, len(a)):
        r.append(modq((a[i] - b[i])))
    return r

def montgomery_reduce(a: int) -> int:
    t = a & (2**16 - 1)
    t = c_int16(t * params.MLKEM_PARAMS.QINV)
    t = (a - t.value * params.MLKEM_PARAMS.q) >> 16;
    return t

def barret_reduce(a: int) -> int:
    v = c_int16(((1<<26) + params.MLKEM_PARAMS.q//2)//params.MLKEM_PARAMS.q)
    t = c_int16((v.value * a + (1<<25)) >> 26)
    t = c_int16(t.value * params.MLKEM_PARAMS.q)
    return c_int16(a - t.value).value