from random import random

class General():
    def __init__(self, data, params_num) -> None:
        self._data = data
        self._params = [0 for _ in range(params_num)]

    def __score_line(self):
        output = 0
        for n, exec_time in self._data:
            output += (self._f(n) - exec_time) ** 2
        return output
    
    def optimize_line(self, it_max: int=10 ** 5, max_param_val: float=10):
        p_len = len(self._params)
        best_score = float("inf")
        for _ in range(it_max):
            self._params = [max_param_val * random() for _ in range(p_len)]
            new_score = self.__score_line()
            if new_score < best_score:
                best_score = new_score
        return best_score

    def _f(self, x: float) -> float: ...
    def __str__(self) -> str: ...

