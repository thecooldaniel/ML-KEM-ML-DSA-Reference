from enum import Enum

n = 256
q = 3329
z = 17
MONT = -1044 # 2^16 mod q
QINV = -3327 # q^-1 mod 2^16

class MLKEM_512():
    n = 256
    q = 3329
    z = 17
    k = 2
    n1 = 3
    n2 = 2
    du = 10
    dv = 4
    ekPKElen = 384 * 2  + 32
    dkPKElen = 384 * 2
    c1len = 32 * 10 * 2
    c2len = 32 * 4

class MLKEM_768():
    n = 256
    q = 3329
    z = 17
    k = 3
    n1 = 2
    n2 = 2
    du = 10
    dv = 4
    ekPKElen = 384 * 3  + 32
    dkPKElen = 384 * 3
    c1len = 32 * 10 * 2
    c2len = 32 * 4

class MLKEM_1024():
    n = 256
    q = 3329
    z = 17
    k = 4
    n1 = 2
    n2 = 2
    du = 11
    dv = 5
    ekPKElen = 384 * 4  + 32
    dkPKElen = 384 * 4
    c1len = 32 * 11 * 2
    c2len = 32 * 5

ML_KEM_PARAMETER = Enum('ML_KEM_PARAMETER', ['ML-KEM-512', 'ML-KEM-768', 'ML-KEM-1024'])