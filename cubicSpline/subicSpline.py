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
        self.S: float = []
        self.dataX = []
        self.dataY = []

        self.ai = np.zeros(self.n - 1)
        self.bi = np.zeros(self.n - 1)
        self.ci = np.zeros(self.n - 1)
        self.di = np.zeros(self.n - 1)

    def Setup(self, dir):
        # read x and y to an array
        with open(dir) as openfileobject:
            for line in openfileobject:
                valueInput = line.replace('\n', '').split()
                self.dataX.append(float(valueInput[0]))
                self.dataY.append(float(valueInput[1]))

        self.generateH()
        self.generatingAMaxtrixValue()
        self.generatingBMaxtrixValue()
        self.S = np.linalg.solve(self.A, self.B)
        print("Origin S = ")
        print(self.S)
        self.fixTheSMatrix()

        for i in range(self.n - 1):
            self.ai[i] = (self.S[i + 1] - self.S[i]) / (6 * self.H[i])
            self.bi[i] = self.S[i] / 2
            self.ci[i] = (float(self.dataY[i + 1]) - float(self.dataY[i])) / self.H[
                i] - (2 * self.H[i] * self.S[i] + self.H[i] * self.S[i + 1]) / 6
            self.di[i] = float(self.dataY[i])

    # P3(x)i = ai(x-xi)^3 + bi(x-xi)^2 + ci(x-xi) + di
    def Poly(self, x: float, i: int):
        return self.ai[i] * (x - self.dataX[i]) ** 3 + self.bi[i] * (x - self.dataX[i]) ** 2 + self.ci[i] * (
                x - self.dataX[i]) + self.di[i]

    def generatingAMaxtrixValue(self):

        if self.case == 1:
            self.A[0][0] = 2 * (self.H[0] + self.H[1])
            self.A[0][1] = self.H[1]
            self.A[self.n - 3][self.n - 4] = self.H[self.n - 3]
            self.A[self.n - 3][self.n - 3] = 2 * (self.H[self.n - 3] + self.H[self.n - 2])

        elif self.case == 2:
            self.A[0][0] = 3 * self.H[0] + 2 * self.H[1]
            self.A[0][1] = self.H[1]
            self.A[self.n - 3][self.n - 4] = self.H[self.n - 3]
            self.A[self.n - 3][self.n - 3] = 2 * self.H[self.n - 3] + 3 * self.H[self.n - 2]
        else:
            self.A[0][0] = (self.H[0] + self.H[1]) * (
                    self.H[0] + 2 * self.H[1]) / self.H[1]
            self.A[0][1] = (self.H[1] ** 2 - self.H[0] ** 2) / self.H[1]
            self.A[self.n - 3][self.n - 4] = (self.H[self.n - 3] ** 2 - self.H[self.n - 2] ** 2) / \
                                             self.H[self.n - 3]
            self.A[self.n - 3][self.n - 3] = (self.H[self.n - 2] + self.H[self.n - 3]) * (
                    self.H[self.n - 2] + 2 * self.H[self.n - 3]) / self.H[self.n - 3]

        for i in range(1, self.n - 3):
            self.A[i][i - 1] = self.H[i]
            self.A[i][i] = 2 * (self.H[i] + self.H[i + 1])
            self.A[i][i + 1] = self.H[i + 1]

    def generatingBMaxtrixValue(self):
        for i in range(self.n - 2):
            u = (self.dataY[i + 2] - self.dataY[i + 1]) / self.H[i + 1]
            d = (self.dataY[i + 1] - self.dataY[i]) / self.H[i]
            self.B[i] = 6 * (u - d)

    def fixTheSMatrix(self):
        if self.case == 1:
            self.S = np.insert(self.S, 0, 0)
            self.S = np.append(self.S, 0)

        elif self.case == 2:
            self.S = np.insert(self.S, 0, self.S[0])
            self.S = np.append(self.S, self.S[-1])
        else:
            t1 = ((self.H[0] + self.H[1]) * self.S[0] - self.H[0] * self.S[1]) / self.H[1]
            t2 = ((self.H[self.n - 3] + self.H[self.n - 2]) * self.S[-1] -
                  self.H[self.n - 2] * self.S[-2]) / self.H[self.n - 3]
            self.S = np.insert(self.S, 0, t1)
            self.S = np.append(self.S, t2)

    def generateH(self):
        for i in range(self.n - 1):
            self.H[i] = self.dataX[i + 1] - self.dataX[i]
