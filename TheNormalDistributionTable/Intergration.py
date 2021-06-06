import math

from scipy.integrate import quad

lowBound = 10


# def f(x: float):
#     return 1.0 / (1.0 + x * x)


def probabilityDensityFunction(x: float):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-1 * (x * x) / 2)


def conditionalProbability(a: float, b: float, upBound: int, f):
    ans: float = 0
    if upBound > 0:
        ans, err = quad(f, a, b)
    return ans


def trapezoidalRule(a: float, b: float, upBound: int, f):
    print('Trapezoidal Rule', '\n')
    delta: float = (b - a) / upBound
    sumAns: float = f(a) + f(b)
    for k in range(1, upBound, 1):
        sumAns += 2 * f(a + k * delta)
    return sumAns * delta / 2.0


def simpson13Rule(a: float, b: float, upBound: int, f):
    print("simpson13", '\n')
    delta = (b - a) / upBound
    sumAns = f(a) + f(b)
    for k in range(1, upBound, 1):
        if k % 2 == 0:
            sumAns += (2.0 * f(a + k * delta))
        else:
            sumAns += (4.0 * f(a + k * delta))
    return sumAns * delta / 3


def simpson38Rule(a: float, b: float, upBound: int, f):
    print("simpson38", '\n')
    delta = (b - a) / upBound
    sumAns = f(a) + f(b)
    for k in range(1, upBound, 1):
        if k % 3 == 0:
            sumAns += (2.0 * f(a + k * delta))
        else:
            sumAns += (3.0 * f(a + k * delta))
    return sumAns * delta * 3.0 / 8.0
