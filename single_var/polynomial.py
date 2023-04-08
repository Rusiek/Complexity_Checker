from .general import General

class Poly(General):
    def __init__(self, data, deg):
        super().__init__(data, deg + 1)

    # P(x) = a0 + a1 * x + ... + an * x^n
    def _f(self, x: float) -> float:
        coef = [self._params[i] * (x ** i) for i in range(len(self._params))]
        return sum(coef)
    
    def __str__(self):
        return f"Linear: "