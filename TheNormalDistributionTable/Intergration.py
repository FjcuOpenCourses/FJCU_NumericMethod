import math

from scipy.integrate import quad


def f(x: float):
    return 1.0 / (1.0 + math.pow(x, 2))


class intergration:

    def __init__(self, upBound: int, lowBound: int):
        self.lowBound = lowBound
        self.upBound = upBound

    def probabilityDensityFunction(self, x: float):
        return (1 / math.sqrt(2 * math.pi)) * math.exp(-1 * (x * x) / 2)

    def conditionalProbability(self, a: float, b: float, f):
        ans: float = 0
        if self.upBound > 0:
            ans, err = quad(f, a, b)
        return ans

    def trapezoidalRule(self, a: float, b: float, f):
        print('Trapezoidal Rule', '\n')
        delta: float = (b - a) / self.upBound
        sumAns: float = f(a) + f(b)
        for k in range(1, self.upBound, 1):
            sumAns += 2 * f(a + k * delta)
        return sumAns * delta / 2.0

    def simpson13Rule(self: float, a: float, b: float, f):
        print("simpson13", '\n')
        delta = (b - a) / self.upBound
        sumAns = f(a) + f(b)
        for k in range(1, self.upBound, 1):
            if k % 2 == 0:
                sumAns += (2.0 * f(a + k * delta))
            else:
                sumAns += (4.0 * f(a + k * delta))
        return sumAns * delta / 3

    def simpson38Rule(self, a: float, b: float, f):
        print("simpson38", '\n')
        delta = (b - a) / self.upBound
        sumAns = f(a) + f(b)
        for k in range(1, self.upBound, 1):
            if k % 3 == 0:
                sumAns += (2.0 * f(a + k * delta))
            else:
                sumAns += (3.0 * f(a + k * delta))
        return sumAns * delta * 3.0 / 8.0
