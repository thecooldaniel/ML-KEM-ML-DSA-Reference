from ML_KEM.helpers import modq
from ML_KEM.parameters import params

q = params.MLKEM_PARAMS.q

def BitsToBytes(b: int, l: int) -> bytes:
    # if b.bit_length() % 8 != 0:
    #     print(b.bit_length())
    #     raise ValueError('bits in b not a multiple of 8')
    # Note: ended up passing l due to trouble with using bit_length to dserive it
    B = bytearray([0] * l) 
    for i in range(0, l * 8):
        # B[i//8] = B[i//8] + ((b >> i) & 1) * 2**(i % 8)
        r1 = 2**(i % 8)
        r2 = ((b >> i) & 1)
        r3 = r1 * r2
        r4 = B[i//8] + r3
        B[i//8] = r4
    return bytes(B)

def BytesToBits(B: bytes) -> int:
    BB = bytearray(B)
    l = len(B)
    b = 0
    for i in range(0, l):
        for j in range(0, 8):
            # b |= (BB[i] % 2) << (8 * i + j)
            # BB[i] = BB[i] // 2
            r1 = (8 * i + j)
            r2 = (BB[i] % 2)
            r3 = r2 << r1
            b |= r3
            r4 = BB[i] // 2
            BB[i] = r4
    return b



def Compress(d: int, x: list) -> list:
    if d >= 12:
        raise ValueError('d must be less than 12')
    t = []
    for l in x:
         r = round( (2**d / q) * l )
         t.append(r)
    return t

def Decompress(d: int, y: list) -> list:
    if d >= 12:
        raise ValueError('d must be less than 12')
    t = []
    for l in y:
        r = round( (q / 2**d) * l)
        t.append(r)
    return t



def ByteEncode(d: int, F: list) -> bytes:
    if d < 1 or d > 12:
        raise ValueError('d must be in the range 1 <= d <= 12')
    if len(F) != 256:
        raise ValueError('F must contain 256 elements')
    b = 0
    for i in range(0, 256):
        a = F[i]
        # Inputs mod q can be negative, must make positive
        if(a < 0):
            a += q
        for j in range(0, d):
            r = a & 1
            b |= r << (i * d + j)
            a = (a - r) // 2
    B = BitsToBytes(b, d*32)
    return B

def ByteDecode(d: int, B: bytes) -> list:
    if d < 1 or d > 12:
        raise ValueError('d must be in the range 1 <= d <= 12')
    if len(B) != 32*d:
        raise ValueError('B must be of length 32*d')
    b = BytesToBits(B)
    F = [0]*256
    if d < 12:
        m = 2**d
    else: 
        m = q
    for i in range(0, 256):
        sum = 0
        for j in range(0, d):
            r1 = (b >> (i * d + j)) & 1     # Note: I'm pretty sure this is just
            r2 = (r1 * 2**j)                #       a sliding window of d-bits
            sum = (sum + r2) % m            #       along the bit array b
        F[i] = sum
    return F