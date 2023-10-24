import inspect
from random import randrange
from typing import Callable
from os import urandom

from rich import print
from rich.panel import Panel
from rich.progress import track

from ML_KEM.Auxiliary.CryptoFunctions import *
from ML_KEM.Auxiliary.ConversionCompression import *
from ML_KEM.Auxiliary.Sampling import *
from ML_KEM.Auxiliary.NTT import *

from ML_KEM.KPKE.KeyGeneration import *

def test(func: Callable, iters: int):
    # caller_name = inspect.stack()[1][3]
    name = func.__name__
    for _ in track(range(0, 100), description=name):
        func()

def all():
    print(Panel('Running all tests'))
    test(BytesEncodeDecode_deq12, 100)
    test(BytesEncodeDecode_dlt12, 100)
    test(NTT, 100)

def BytesEncodeDecode_deq12():
    t = [randrange(1, q-1) for j in range(0, 256)]
    T = ByteEncode(12, t)
    tt = ByteDecode(12, T)
    assert(t == tt)

def BytesEncodeDecode_dlt12():
    for i in range(1, 12):
        t = [randrange(1, 2**i) & (2**i-1) for j in range(0, 256)]
        T = ByteEncode(i, t)
        tt = ByteDecode(i, T)
        assert(t == tt)

def NTT_Both():
    f = [randrange(1, q-1) for j in range(0, 256)]
    fh = NTT(f)
    ff = NTTINV(fh)
    assert(f == ff)

def scratch():
    KeyGen()

    z = 1

def c_comparisons():
    # hash_input = 0xdeadbeef.to_bytes(4, 'little')
    # c_hash_h = 0xB5EFFBB3E956C8ADB67687FAF087F864C083FB48E9F42F6CA62D4DF5DB7331E8
    # c_hash_g = 0x261DAA56FF722DD4807F4427C60700661F72F5777F249B2B78AB5AF489B4C5338C9DC9AA1265580B43913AB191D7AB88D53653898876FC8FC67E8C4DA587D8B1

    # p_hash_h = H(hash_input)
    # p_hash_g = G(hash_input)

    # assert(c_hash_h == int.from_bytes(p_hash_h, 'big'))
    # assert(c_hash_g == int.from_bytes(p_hash_g[0] + p_hash_g[1], 'big'))

    static_seed = 0x8CDE0C16E69FD32881FD56B8926F06AF5DE861298490F404B27234767F176EB0.to_bytes(32, 'little')
    # c_hash_g = 0x855DD1E6847BB6E28483F21626785165F707ABEFE6571F4E39FB01EA883023533696F7DC6738DC5039ABB7A56854A54581F77A416DF07D4E799BC18BFB004F16
    # p_hash_g = G(static_seed)
    # assert(c_hash_g == int.from_bytes(p_hash_g[0] + p_hash_g[1], 'big'))

    KeyGen(static_seed)


    z = 1


