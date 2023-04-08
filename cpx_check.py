from sol import f
from single_var.polynomial import Poly
from single_var.log import Log
from time import time
import matplotlib.pyplot as plt

class Cpx_Check():
    def __init__(self, data: list):
        self.__data = data

    def solve(self):
        best_score, function = float("inf"), None

        # Polynomial Check:
        for deg in range(1, 5):
            deg_str = '^' + str(deg) if deg != 1 else ''
            print(f"Testing O(n{deg_str}) functions...")
            test = Poly(self.__data, deg)
            score = test.optimize_line()
            print(f"O(n{deg_str}) functions score: {score}\n")
            if score < best_score:
                best_score = score
                function = f"O(n{deg_str})" 

        # Log Check:
        print(f"Testing O(log(n)) functions...")
        test = Log(self.__data)
        score = test.optimize_line()
        print(f"O(log(n)) functions score: {score}\n")
        if score < best_score:
            best_score = score
            function = f"O(log(n))"     

        print(f"Complexity of program: {function}")