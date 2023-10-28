from __future__ import annotations
from ML_KEM.MLKEM_parameters import MLKEM_PARAMETER

class RefValues(object):
    parameter: MLKEM_PARAMETER
    keygen: RefValuesKeygen
    encrypt: RefValuesEncrypt

    def __init__(self, param: MLKEM_PARAMETER):
        self.parameter = param


class RefValuesKeygen(object):
    parameter: MLKEM_PARAMETER
    seed = 0x8CDE0C16E69FD32881FD56B8926F06AF5DE861298490F404B27234767F176EB0.to_bytes(32, 'little')
    c_hash_g = 0x855DD1E6847BB6E28483F21626785165F707ABEFE6571F4E39FB01EA883023533696F7DC6738DC5039ABB7A56854A54581F77A416DF07D4E799BC18BFB004F16
        
    def __init__(self, params: MLKEM_PARAMETER):
        self.parameter = params
        self.AC = []
        self.SC = []
        self.EC = []
        self.SHC = []
        self.EHC = []
        self.ASC = []
        self.ASEC = []
        self.PKC = []
        self.SKC = []
        self.PKPC = []
        self.SKPC = []

class RefValuesEncrypt(object):
    parameter: MLKEM_PARAMETER

    def __init__(self, params: MLKEM_PARAMETER):
        self.parameter = params
        self.PKC = []