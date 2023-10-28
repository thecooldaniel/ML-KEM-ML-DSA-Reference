from enum import Enum

class MLKEM_PARAM_SET(object):
    n = 256
    q = 3329
    z = 17
    MONT = -1044 # 2^16 mod q
    QINV = -3327 # q^-1 mod 2^16
    k = 0
    n1 = 0
    n2 = 0
    du = 0
    dv = 0
    ekPKElen = 0
    dkPKElen = 0
    c1len = 0
    c2len = 0

class MLKEM_512(MLKEM_PARAM_SET):
    k = 2
    n1 = 3
    n2 = 2
    du = 10
    dv = 4
    ekPKElen = 384 * 2  + 32
    dkPKElen = 384 * 2
    c1len = 32 * 10 * 2
    c2len = 32 * 4

class MLKEM_768(object):
    k = 3
    n1 = 2
    n2 = 2
    du = 10
    dv = 4
    ekPKElen = 384 * 3  + 32
    dkPKElen = 384 * 3
    c1len = 32 * 10 * 2
    c2len = 32 * 4

class MLKEM_1024(object):
    k = 4
    n1 = 2
    n2 = 2
    du = 11
    dv = 5
    ekPKElen = 384 * 4  + 32
    dkPKElen = 384 * 4
    c1len = 32 * 11 * 2
    c2len = 32 * 5

MLKEM_PARAMETER = Enum('ML_KEM_PARAMETER', ['ML_KEM_512', 'ML_KEM_768', 'ML_KEM_1024'])