from .general import General
import numpy as np

class Log(General):
    def __init__(self, data):
        super().__init__(data, 2)

    def _f(self, x: float) -> float:
        a, b = self._params
        return a * np.log2(b * x)
