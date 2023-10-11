from enum import Enum

n = 256
q = 3329
z = 17

class ParameterSet():
    n = 256
    q = 3329
    z = 17
    def __init__(self, k, n1, n2, du, dv):
        self.k = k
        self.n1 = n1
        self.n2 = n2
        self.du = du
        self.dv = dv

MLKEM_512 = ParameterSet(2, 3, 2, 10, 4)
MLKEM_768 = ParameterSet(3, 2, 2, 10, 4)
MLKEM_1024 = ParameterSet(4, 2, 2, 11, 5)

ML_KEM_PARAMETER = Enum('ML_KEM_PARAMETER', ['ML-KEM-512', 'ML-KEM-768', 'ML-KEM-1024'])