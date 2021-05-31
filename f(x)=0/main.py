from math import cos, sin

epsilon: float = 1e-6
MaximumLoop: int = 1000


def f(x):
    return 4.98 * cos(x) + 3.2 * x * sin(2 * x) - 3 * x + 2.9


def fPrime(x):
    return 3.2 * sin(2 * x) + 3.2 * x * cos(2 * x) * 2 - 3 - (4.98 * sin(x))


def bisection(a, b):
    step = 0
    while abs(f(a) - f(b)) > epsilon and step <= MaximumLoop:
        c = (a + b) / 2
        if f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
        step += 1
    if step > MaximumLoop:
        print(" Method failed to converge\n")
    else:
        print(" Method converge at x =", c, "\n")


def fixedPointIteration(x0):
    step = 0
    x = f(x0)
    while abs(x - x0) > epsilon and step <= MaximumLoop:
        x0 = x
        x = f(x0)
        step += 1

    if step > MaximumLoop:
        print(" Method failed to converge\n")
    else:
        print(" Method converge at x =", x, "\n")


def secant(a, b):
    step = 0
    while abs(a - b) > epsilon and step <= MaximumLoop:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        a = b
        b = c
        step += 1

    if step > MaximumLoop:
        print(" Method failed to converge\n")
    else:
        print(" Method converge at x =", b, "\n")


def newton(x0):
    step = 0
    h = f(x0) / fPrime(x0)
    while abs(h) > epsilon and step <= MaximumLoop:
        h = f(x0) / fPrime(x0)
        x0 = x0 - h
        step += 1
    if step > MaximumLoop:
        print(" Method failed to converge\n")
    else:
        print("Method converge at x =", x0)


def falsePosition(a, b):
    step = 0
    x = (a * f(b) - b * f(a)) / (f(b) - f(a))
    x0 = 1.5
    while step <= MaximumLoop and abs(x - x0) > epsilon:
        x0 = x

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        step += 1
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if step > MaximumLoop:
        print(" Method failed to converge\n")
    else:
        print("Method converge at x =", x, "\n")


def modifiedFalsePosition(a, b):
    x0 = 1.5
    fa = f(a)
    fb = f(b)
    x = (a * fb - b * fa) / (f(b) - f(a))
    step = 0
    while abs(x - x0) > epsilon and step <= MaximumLoop:
        x0 = x

        if f(a) * f(x) < 0:
            b = x
            fb = f(b)
            fa /= 2
        else:
            a = x
            fa = f(a)
            fb /= 2
        step += 1
        x = (a * fb - b * fa) / (fb - fa)
    if step > MaximumLoop:
        print(" Method failed to converge\n")
    else:
        print("Method converge at x =", x, "\n")


if __name__ == '__main__':
    print("running bisection method\n")
    bisection(-5, 5)
    print("running fixedPointIteration method\n")
    fixedPointIteration(1)
    print("running secant method\n")
    secant(-5, 5)
    print("running falsePosition method\n")
    falsePosition(-5, 5)
    print("running newton method\n")
    newton(1)
    print("running modifiedFalsePosition method\n")
    modifiedFalsePosition(-5, 5)
