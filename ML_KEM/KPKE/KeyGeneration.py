from os import urandom
from ML_KEM.Auxiliary.Sampling import *
from ML_KEM.Auxiliary.CryptoFunctions import *
from ML_KEM.Auxiliary.NTT import *
from ML_KEM.Auxiliary.ConversionCompression import *
from ML_KEM.parameters import MLKEM_512 as params

from rich import print
from rich.panel import Panel
from rich.markdown import Markdown

from ML_KEM.helpers import add_list_modq

def KeyGen(d: bytes=None) -> (bytes, bytes):
    if d is None:
        d = urandom(32)
    p, sigma = G(d)
    N = 0
    Ah = [[[[None] * 256] for i in range(0, params.k)] for j in range(0, params.k)]
    s = [[None] for i in range(0, params.k)]
    e = [[None] for i in range(0, params.k)]
    sh = [[None] for i in range(0, params.k)]
    eh = [[None] for i in range(0, params.k)]
    t = [[None] for i in range(0, params.k)]

    for i in range(0, params.k):
        for j in range(0, params.k):
            xof = XOF(p, i.to_bytes(1, 'big'), j.to_bytes(1, 'big'))   
            Ah[i][j] = SampleNTT(xof(512))  # QUESTION: How to know how much to sample here?
    for i in range(0, params.k):
        s[i] = SamplePolyCBD(params.n1, PRF(params.n1, sigma, N.to_bytes(1, 'big')))
        N += 1 
    for i in range(0, params.k):
        e[i] = SamplePolyCBD(params.n1, PRF(params.n1, sigma, N.to_bytes(1, 'big')))
        N += 1
    
    for idx, l in enumerate(s):
        sh[idx] = NTT(l)
    for idx, l in enumerate(e):
        eh[idx] = NTT(l)

#   |     A     |   |  s  |   |  e  |
#   | :-- | :-- |   | :-- |   | :-- |
#   | 0,0 | 0,1 |   |  0  |   |  0  |
#   | 1,0 | 1,1 |   |  1  |   |  1  |

#   |             A * s             |
#   | :---------------------------- |
#   | A[0,0] * s[0] + A[0,1] * s[1] |
#   | A[1,0] * s[0] + A[1,1] * s[1] |

#   |     As+e     |
#   | :----------- |
#   | As[0] + e[0] |
#   | As[1] + e[1] |

    # t = A * s
    for i in range(0, params.k-1):
        t1 = MultiplyNTTs(Ah[i][i], sh[i])
        t2 = MultiplyNTTs(Ah[i][i+1], sh[i+1])
        t[i] = add_list_modq(t1, t2)

        t1 = MultiplyNTTs(Ah[i+1][i], sh[i])
        t2 = MultiplyNTTs(Ah[i+1][i+1], sh[i+1])
        t[i+1] = add_list_modq(t1, t2)

    # t = A * s + e
    for i in range(0, params.k):
        t[i] = add_list_modq(t[i], eh[i])

    ekPKE = ByteEncode(12, t[0])
    for i in range(1, params.k):
        ekPKE += ByteEncode(12, t[i])
    ekPKE += p

    dkPKE = ByteEncode(12, sh[0])
    for i in range(1, params.k):
        dkPKE += ByteEncode(12, sh[i])

    assert(len(ekPKE) == 384 * params.k + 32)
    assert(len(dkPKE) == 384 * params.k)

    print(Markdown('**ek_PKE**'))
    print(Panel(ekPKE.hex()))
    print(Markdown('**dk_PKE**'))
    print(Panel(dkPKE.hex()))

    return (ekPKE, dkPKE)
