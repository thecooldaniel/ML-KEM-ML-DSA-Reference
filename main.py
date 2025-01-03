from rich import print, inspect
from common.types import rint
import ML_KEM.tests as mlk_tests
from ML_KEM.KPKE.KeyGeneration import KeyGen
from ML_KEM.KPKE.Encryption import Encrypt
from ML_KEM.KPKE.Decryption import Decrypt
from ML_KEM.parameters import params

from os import urandom


def main():
    # mlk_tests.all()
    # mlk_tests.scratch()
    # mlk_tests.c_comparisons()
    params.MATCH_CREF_OUTPUTS = True

    static_seed = 0x8CDE0C16E69FD32881FD56B8926F06AF5DE861298490F404B27234767F176EB0.to_bytes(32, 'little')
    r = urandom(32)
    m = b'\xde\xad\xbe\xef' * 8
    ek1, dk1 = KeyGen(static_seed)
    c = Encrypt(ek1, m, urandom(32))
    # mm = Decrypt(dk1, c)

    b = 1

    # ek2, dk2 = KeyGen(r)
    # assert(ek1 == ek2)
    # assert(dk1 == dk2)


if __name__ == '__main__':
    main()