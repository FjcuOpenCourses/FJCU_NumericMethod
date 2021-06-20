import math
import os

import numpy as np


class cubicSpline:

    def __init__(self):
        self.n = 22
        self.case = 1

        self.A = np.zeros((self.n - 2, self.n - 2))
        self.B = np.zeros(self.n - 2)
        self.H = np.zeros(self.n + 1)

        self.dataX = []
        self.dataY = []

        self.ai = np.zeros(self.n - 1)
        self.bi = np.zeros(self.n - 1)
        self.ci = np.zeros(self.n - 1)
        self.di = np.zeros(self.n - 1)

    def Setup(self, dir):
        with open(dir) as openfileobject:
            for line in openfileobject:
                valueInput = line.replace('\n', '').split()
                self.dataX.append(float(valueInput[0]))
                self.dataY.append(float(valueInput[1]))

    # P3(x)i = ai(x-xi)^3 + bi(x-xi)^2 + ci(x-xi) + di
    def Poly(self, x: float, i: int):
        return self.ai[i] * (x - self.dataX[i]) ** 3 + self.bi[i] * (x - self.dataX[i]) ** 2 + self.ci[i] * (
                    x - self.dataX[i]) + self.di[i]
