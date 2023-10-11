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


