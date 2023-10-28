from __future__ import annotations
from ML_KEM.MLKEM_parameters import MLKEM_512, MLKEM_768, MLKEM_1024, MLKEM_PARAM_SET, MLKEM_PARAMETER
from ML_KEM.reference_values import RefValues
from ML_KEM.reference_values_512 import RefValues512

class Parameters(object):
    MLKEM_PARAMS: MLKEM_PARAM_SET
    MLKEM_RFVALS: RefValues

    def __init__(self, params: MLKEM_PARAMETER):
        self.MATCH_CREF_OUTPUTS = False
        self.MLKEM_PARAM = params
    
    @property
    def MLKEM_PARAM(self) -> MLKEM_PARAMETER:
        return self._MLKEM_PARAM
    
    @MLKEM_PARAM.setter
    def MLKEM_PARAM(self, value: MLKEM_PARAMETER):
        if value == MLKEM_PARAMETER.ML_KEM_512:
            self._MLKEM_PARAMS = MLKEM_512()
        elif value == MLKEM_PARAMETER.ML_KEM_768:
            self._MLKEM_PARAMS = MLKEM_768()
        elif value == MLKEM_PARAMETER.ML_KEM_1024:
            self._MLKEM_PARAMS = MLKEM_1024()

    @property
    def MLKEM_PARAMS(self) -> MLKEM_PARAM_SET:
        return self._MLKEM_PARAMS
    
    @property
    def MLKEM_RFVALS(self) -> RefValues:
        return self._MLKEM_RFVALS
    
    @MLKEM_RFVALS.setter
    def MLKEM_RFVALS(self, value: MLKEM_PARAMETER):
        if value == MLKEM_PARAMETER.ML_KEM_512:
            self._MLKEM_RFVALS = RefValues512
        # elif value == MLKEM_PARAMETER.ML_KEM_768:
        #     self._MLKEM_RFVALS = MLKEM_768()
        # elif value == MLKEM_PARAMETER.ML_KEM_1024:
        #     self._MLKEM_RFVALS = MLKEM_1024()

params = Parameters(MLKEM_PARAMETER.ML_KEM_512)
params.MLKEM_RFVALS = MLKEM_PARAMETER.ML_KEM_512