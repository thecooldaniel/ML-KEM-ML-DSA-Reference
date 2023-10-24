from hashlib import sha3_256, sha3_512, shake_128, shake_256

def PRF(n: int, s: bytes, b: bytes) -> bytes:
    if n not in [2,3]:
        raise ValueError('n neither 2 or 3')
    if len(s) != 32:
        raise ValueError('s not 32 bytes')
    if len(b) != 1:
        raise ValueError('b not 1 byte')
    return shake_256(s + b).digest(64 * n)


class cXOF:
    def __init__(self, p: bytes, i: bytes, j: bytes, transposed=False):
        if len(p) != 32:
            raise ValueError('p not 32 bytes')
        if len(i) != 1:
            raise ValueError('i not 1 bytes')
        if len(j) != 1:
            raise ValueError('j not 1 byte')
        self.p = p
        self.i = i
        self.j = j
        self.bytesOut = 0
        if(transposed):
            self.digest = shake_128(p + i + j).digest
        else:
            self.digest = shake_128(p + j + i).digest

    def read(self, b: int) -> bytes:
        out = self.digest(b + self.bytesOut)[self.bytesOut:]
        self.bytesOut += b
        return out


def XOF(p: bytes, i: bytes, j: bytes):
    x = cXOF(p, i, j)
    return x.read

def H(s: bytes) -> bytes:
    return sha3_256(s).digest()

def J(s: bytes) -> bytes:
    return shake_256(s).digest(32)

def G(b: bytes) -> bytes:
    d = sha3_512(b).digest()
    return d[:32], d[32:]