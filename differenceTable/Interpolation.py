import math
import os


class interpolation:

    def __init__(self):
        self.table = [[0 for x in range(11)] for y in range(11)]
        self.delta = [[0 for x in range(11)] for y in range(11)]
        self.S = [0 for y in range(5)]
        self.point = [0 for y in range(4)]
        self.mul = [0 for y in range(12)]
        self.lastTable = []

    def Setup(self):
        self.table = [[float(0.0) for _ in range(11)] for _ in range(11)]
        self.table[1][0] = float(0.28)
        self.table[0][1] = float(0.7200)
        self.delta = [[float(-50.0) for _ in range(11)] for _ in range(11)]
        self.lastTable = [float(0.0) for _ in range(11)]

        for index in range(2, 11, 1):
            self.table[index][0] = self.table[index - 1][0] + 0.25
            self.table[0][index] = self.table[0][index - 1] + 0.12

        with open(os.path.dirname(os.path.realpath(__file__)) + "\\datasheet.in") as openfileobject:
            j: int = 1
            for line in openfileobject:
                valueInput = line.replace('\n', '').split()
                for k in range(1, len(valueInput) + 1, 1):
                    self.table[j][k] = float(valueInput[k - 1])
                j += 1

    # def generatDelta(self):


    def NForward(self, x: float):
        baseIndex: int = 0

        for index in range(1, 10, 1):
            if self.table[index][0] <= x <= self.table[index + 1][0]:
                baseIndex = index
                break

        self.S[0] = (x - self.table[baseIndex][0]) / 0.25
        self.point[0] = baseIndex
        return 10 - baseIndex

    def NBackward(self, x: float):
        baseIndex = 0
        for index in range(1, 10, 1):
            if x <= self.table[index][0]:
                baseIndex = index
                break
        self.S[1] = (x - self.table[baseIndex][0]) / 0.25
        self.point[1] = baseIndex
        return baseIndex - 1

    def deltaCal(self, x: float, index: int, method: int):
        self.delta = [[float(-50.0) for index in range(11)] for _ in range(11)]

        for i in range(1, 10, 1):
            self.delta[1][i]: float = self.table[i + 1][index] - self.table[i][index]

        for j in range(1, 10, 1):
            for k in range(1, 11 - j, 1):
                self.delta[j + 1][k]: float = self.delta[j][k + 1] - self.delta[j][k]

        if method == 1:
            self.NFCalX(x, index)
        else:
            if method == 2:
                self.NBCalX(x, index)
            else:
                if method == 3:
                    self.GFCalX(x, index)
                else:
                    self.GBCalX(x, index)

    # Build the last table by using 10 values from UseCal function
    def LastCal(self, y: float, method: int):

        self.delta = [[-50.00 for _ in range(11)] for _ in range(11)]

        for i in range(1, 10, 1):
            self.delta[1][i]: float = self.lastTable[i + 1] - self.lastTable[i]

        for j in range(1, 10, 1):
            for k in range(1, 11 - j, 1):
                self.delta[j + 1][k]: float = self.delta[j][k + 1] - self.use[j][k]
            if method == 1:
                self.NFCalY(y)
            else:
                if method == 2:
                    self.NBCalY(y)
                else:
                    if method == 3:
                        self.GFCalY(y)
                    else:
                        self.GBCalY(y)

    # NewtonForwardansstore
    def NFCalX(self, x: float, index: float):
        ans: float = self.table[self.point[0]][index]
        self.SCal(1, 0)
        for i in range(1, 10 - self.point[0] + 1, 1):
            ans += self.delta[i][self.point[0]] * self.mul[i]
        self.lastTable[index] = ans

    # gaussianForward ans store
    def GFCalX(self, x: float, index: int):
        ans: float = self.table[self.point[2]][index]
        self.SCal2(1, 2)
        k: int = 9
        even: int = 1
        i: int = self.point[2]
        while i > 0:
            even ^= 1
            if even: i -= 1
            if i > k or i == 0:
                break
            ans += self.delta[10 - k][i] * self.mul[10 - k]
            k -= 1
        self.lastTable[index] = ans

    def computeCircle(self, cnt, j, k, even):
        while j > 0:
            even ^= 1
            if even:
                j -= 1
            if j > k or j == 0:
                break
            k -= 1
            cnt += 1
        return cnt

    def GForward(self, x: float):
        baseValue = 10.0
        baseIndex = 0
        for index in range(1, 11, 1):
            currentValue: float = abs(x - self.table[index][0])
            if currentValue <= baseValue:
                baseValue = currentValue
                baseIndex = index
        cnt = self.computeCircle(0, baseIndex, 9, 1)
        print("GF have ", cnt, " circle(s)\n")
        self.S[2] = (x - self.table[baseIndex][0]) / 0.25
        self.point[2] = baseIndex
        return cnt

    def GBackward(self, x: float):
        baseValue: float = 10.0
        baseIndex: int = 0
        for index in range(1, 11, 1):
            tmp: float = abs(x - self.table[index][0])
            if tmp <= baseValue:
                baseValue = tmp
                baseIndex = index
        cnt = self.computeCircle(0, baseIndex, 9, 0)
        print("GB have ", cnt, " circle(s)\n")
        self.S[3] = (x - self.table[baseIndex][0]) / 0.25
        self.point[3] = baseIndex
        return cnt

    def SCal(self, fb: float, method: int):
        self.mul[0] = 1
        for i in range(11):
            tmp: float = self.S[method] - i * fb
            self.mul[i + 1] = tmp * self.mul[i]
        for j in range(11):
            self.mul[j] /= math.factorial(j)

    def SCal2(self, fb: float, method: float):
        self.mul[0] = 1
        for i in range(11):
            if i % 2 == 0:
                fb *= -1
            tmp = self.S[method] - int((i + 1) / 2) * fb
            self.mul[i + 1] = tmp * self.mul[i]
        for j in range(11):
            self.mul[j] /= math.factorial(j)

    def NFCalY(self, y: float):
        baseIndex: int = 0
        for i in range(1, 10, 1):
            if self.table[0][i] <= y <= self.table[0][i + 1]:
                baseIndex = i
                break
        self.S[4] = (y - self.table[0][baseIndex]) / 0.1200
        ans: int = self.lastTable[baseIndex]
        self.SCal(1, 4)
        for i in range(1, 10 - baseIndex + 1, 1):
            ans += self.delta[i][baseIndex] * self.mul[i]
        print("NF's result is ====> ", ans, "\n")

    # NewtonBackward and store
    def NBCalX(self, x, index):
        ans: float = self.table[self.point[1]][index]
        self.SCal(-1, 1)

        j: int = self.point[1]
        for i in range(1, self.point[1] - 2, 1):
            j -= 1
            ans += self.delta[i][j] * self.mul[i]
        self.lastTable[index] = ans

    # NewtonBackward and store
    def NBCalY(self, y: float):
        baseIndex: int = 0
        for i in range(1, 10, 1):
            if self.table[0][i] <= y <= self.table[0][i + 1]:
                baseIndex = i + 1
                break
        self.S[4] = (y - self.table[0][baseIndex]) / 0.12
        ans: float = self.lastTable[baseIndex]
        self.SCal(-1, 4)
        j: int = baseIndex
        for i in range(1, baseIndex - 2, 1):
            j -= 1
            ans += self.delta[i][j] * self.mul[i]
        print("NB's result is ====> ", ans, "\n")

    def GFCalY(self, y: float):
        baseValue: float = 10.0
        baseIndex: int = 0
        for i in range(1, 11, 1):
            tmp: float = abs(y - self.table[0][i])
            if tmp <= baseValue:
                baseValue = tmp
                baseIndex = i
        self.S[4] = (y - self.table[0][baseIndex]) / 0.1200
        ans: float = self.lastTable[baseIndex]
        self.SCal2(1, 4)
        k: int = 9
        even: int = 1
        i: int = baseIndex
        while i > 0:
            even ^= 1
            if even:
                i -= 1
            if i > k or i == 0:
                break
            ans += self.delta[10 - k][i] * self.mul[10 - k]
            k -= 1
        print("GF's result is ====> ", ans, "\n")

    # gaussianBackwardans store
    def GBCalX(self, x: float, index: int):
        ans: float = self.table[self.point[3]][index]
        self.SCal2(-1, 3)
        k: int = 9
        even: int = 0
        i: int = self.point[3]
        while i > 0:
            even ^= 1
            if even:
                i -= 1
            if i > k or i == 0:
                break
            ans += self.delta[10 - k][i] * self.mul[10 - k]
            k -= 1
        self.lastTable[index] = ans

    def GBCalY(self, y: float):
        baseValue: float = 10.0
        baseIndex: int = 0
        for i in range(1, 11, 1):
            tmp: float = abs(y - self.table[0][i])
            if tmp <= baseValue:
                baseValue = tmp
                baseIndex = i
        self.S[4] = (y - self.table[0][baseIndex]) / 0.1200
        ans: float = self.lastTable[baseIndex]
        self.SCal2(-1, 4)
        k: int = 9
        even: int = 0
        i: int = baseIndex
        while i > 0:
            even ^= 1
            if even:
                i -= 1
            if i > k or i == 0:
                break
            ans += self.delta[10 - k][i] * self.mul[10 - k]
            k -= 1
        print("GB's result is ====> ", ans, "\n")

    # Build the last table by using 10 values from UseCal function
    def LastCal(self, y: float, method: int):
        for i in range(11):
            for j in range(11):
                self.delta[i][j] = -50.0
        for i in range(1, 10, 1):
            self.delta[1][i]: float = self.lastTable[i + 1] - self.lastTable[i]
        for j in range(1, 10, 1):
            for k in range(1, 11 - j, 1):
                self.delta[j + 1][k]: float = self.delta[j][k + 1] - self.delta[j][k]

        if method == 1:
            self.NFCalY(y)
        else:
            if method == 2:
                self.NBCalY(y)
            else:
                if method == 3:
                    self.GFCalY(y)
                else:
                    self.GBCalY(y)

    # def numbers_to_months(self, argument):
    #     switcher = {
    #         1: self.NFCalX(x, index),
    #         2: self.NBCalX(x, index),
    #         3: self.GFCalX(x, index),
    #     }
    #     func = switcher.get(argument, lambda: self.GBCalY(y))
