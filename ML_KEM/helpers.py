import ML_KEM.parameters as params

def modq(n: int) -> int:
    return n % params.q

def add_list_modq(a: list, b: list) -> list:
    if len(a) != len(b):
        raise ValueError("length of 'a' must match length of 'b'")
    r = []
    for i in range(0, len(a)):
        r.append(modq((a[i] + b[i])))
    return r