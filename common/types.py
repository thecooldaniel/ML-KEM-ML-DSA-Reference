from __future__ import annotations
from typing import Any
from common.helpers import toRadix
import common.config as config

class rint(int):
    radix = config.DEF_RADIX

    def __add__(self, __value):
        return rint(int.__add__(self, __value))
    
    def __sub__(self, __value):
        return rint(int.__sub__(self, __value))
    
    def __mul__(self, __value):
        return rint(int.__mul__(self, __value))
    
    def __pow__(self, __value, mod=None) -> rint:
        if mod is not None:
            return rint(pow(int(self), __value, mod))
        return rint(super().__pow__(__value))
    
    def __rpow__(self, __value, __mod: int | None = None) -> Any:
        return rint(super().__rpow__(__value, __mod))
    
    def __mod__(self, __value) -> rint:
        return rint(super().__mod__(__value))
    
    
    def __str__(self) -> str:
        if config.DEF_OUTPUT == 'HEX' or self.radix < 0:
            return '0x{:x}'.format(int(self))
        clist, plist = toRadix(self.radix, int(self))
        return clist
    
    def radix(self, radix: int = None, minwords: int = None) -> list:
        if radix is None:
            radix = self.radix
        if minwords is None:
            minwords = 1
        clist, plist = toRadix(radix, int(self), minwords)
        return clist
