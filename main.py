
from math import cos,sin

from networkx.drawing.tests.test_pylab import plt
from numpy import disp, math


def f(x) -> float:
    return 4.98 * cos(x) + 3.2 * x * sin(2 * x) - 3 * x + 2.9


def bisection(a, b, step, x, y):
    if step == 0:
        disp('_______________________________________________')
        disp(' iter a b c f(c) |b-a|/2 ')
        disp('_______________________________________________\n')
    c = (a + b) / 2
    if c != 0:
        print(step, " ", a, " ", b, " ", c, " ", f(c))
        sample: float = f(a) * f(c)
        if sample < 0.0:
            x.append(c)
            y.append(f(c))
            bisection(a, c, step + 1, x, y)
        else:
            bisection(c, b, step + 1, x, y)
    else:
        plt.plot(x, y)


# def fixedPointIteration():





if __name__ == '__main__':
    f=lambda x:4.98 * cos(x) + 3.2 * x * sin(2 * x) - 3 * x + 2.9
    bisection(1, 2, 0, [], [])

