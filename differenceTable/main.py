import math
from decimal import Decimal, ROUND_HALF_EVEN

table = [[0 for x in range(11)] for y in range(11)]
use = [[0 for x in range(11)] for y in range(11)]
S = [[] for y in range(5)]
point = [[] for y in range(4)]
mul = [[] for y in range(11)]
lastTable = []


def computeCircle(cnt, j, k, even):
    while j > 0:
        even ^= 1
        if even:
            j -= 1
        if j > k or j == 0:
            break
        k -= 1
        cnt += 1
    return cnt


def Setup():
    lastTable = [float(0.0) for _ in range(11)]
    table = [[float(0.0) for _ in range(11)] for _ in range(11)]
    use = [[float(-50.0) for _ in range(11)] for _ in range(11)]

    table[1][0] = float(0.28)
    table[0][1] = float(0.7200)

    for index in range(2, 11, 1):
        table[index][0] = table[index - 1][0] + 0.25
    for index in range(2, 11, 1):
        table[0][index] = table[0][index - 1] + 0.1200


def NForward(x: float):
    base: int = 0
    for index in range(10):
        if float(table[index][0]) > x:
            base = index - 1
            break
    S[0] = (x - table[base][0]) / 0.25
    point[0] = base
    return 10 - base


def NBackward(x: float):
    base = 0
    for index in range(1, 10, 1):
        if x <= table[index][0]:
            base = i
            break
    S[1] = (x - table[base][0]) / 0.25
    point[1] = base
    return base - 1


def GForward(x):
    baseValue = 10.0
    baseIndex = 0
    for index in range(1, 11, 1):
        currentValue: float = abs(x - table[index][0])
        if currentValue <= baseValue:
            baseValue = currentValue
            baseIndex = i
    cnt = computeCircle(0, baseIndex, 9, 1)
    print("GF have ", cnt, " circle(s)\n")
    S[2] = (x - table[baseIndex][0]) / 0.25
    point[2] = baseIndex
    return cnt


def GBackward(x):
    baseValue: float = 10.0
    baseIndex: int = 0
    for index in range(1, 11, 1):
        tmp: float = abs(x - table[index][0])
        if tmp <= baseValue:
            baseValue = tmp
            baseIndex = index
    cnt = computeCircle(0, baseIndex, 9, 0)
    print("GB have ", cnt, " circle(s)\n")
    S[3] = (x - table[baseIndex][0]) / 0.25
    point[3] = baseIndex
    return cnt


def SCal(fb: float, method: int):
    mul[0] = 1
    for i in range(1, 11, 1):
        tmp: float = S[method] - i * fb
        mul[i + 1] = tmp * mul[i]
    for j in range(11):
        mul[j] /= math.factorial(j)


def SCal2(fb, method):
    mul[0] = 1;
    for i in range(11):
        tmp
        if i % 2 == 0:
            tmp = S[method] - int((i + 1) / 2) * -fb
        else:
            tmp = S[method] - int((i + 1) / 2) * fb

        print("S will +/- ", int((i + 1) / 2), "\n")
        mul[i + 1] = tmp * mul[i]
    for j in range(11):
        mul[j] /= math.factorial(j)


# NewtonForwardansstore
def NFCalX(x, index):
    ans: float = table[point[0]][index]
    SCal(1, 0)
    for i in range(1, 10 - point[0] + 1, 1):
        ans += use[i][point[0]] * mul[i]
        print("circle : ", use[i][point[0]], " ", " mul : ", mul[i], "\n")
    lastTable[index] = ans
    print("ans = ", ans, "\n")


def NFCalY(y):
    baseIndex: int = 0
    for i in range(10):
        if y >= table[0][i] or y <= table[0][i + 1]:
            baseIndex = i
            break
    S[4] = (y - table[0][baseIndex]) / 0.1200
    ans: int = lastTable[baseIndex]
    SCal(1, 4)
    for i in range(1, 10 - baseIndex + 1, 1):
        ans += use[i][baseIndex] * mul[i]
    print("NF's result is ====> ", ans, "\n")


# NewtonBackward ans store
def NBCalX(x, index):
    ans: float = table[point[1]][index]
    SCal(-1, 1)
    j: int = point[1]
    for i in range(1, point[1], 1):
        j -= 1
        ans += use[i][j] * mul[i]
    lastTable[index] = ans


def NBCalY(y):
    baseIndex: int = 0
    for i in range(1, 10, 1):
        if table[0][i] <= y <= table[0][i + 1]:
            base = i + 1
            break
    S[4] = (y - table[0][baseIndex]) / 0.1200
    ans: float = lastTable[baseIndex]
    SCal(-1, 4)
    j: int = baseIndex
    for i in range(1, base, 1):
        j -= 1
        ans += use[i][j] * mul[i]
    print("NB's result is ====> ", ans, "\n")


# gaussianForward ans store
def GFCalX(x, index):
    ans: float = table[point[2]][index]
    SCal2(1, 2)
    k: int = 9
    even: int = 1
    i: int = point[2]
    while i > 0:
        even ^= 1;
        if even: i -= 1
        if i > k or i == 0:
            break;
        ans += use[10 - k][i] * mul[10 - k]
        k -= 1
    lastTable[index] = ans


def GFCalY(y):
    baseValue: float = 10.0
    baseIndex: int = 0
    for i in range(1, 11, 1):
        tmp: float = abs(y - table[0][i])
        if tmp <= baseValue:
            baseValue = tmp
            baseIndex = i
    S[4] = (y - table[0][baseIndex]) / 0.1200
    ans: float = lastTable[baseIndex]
    SCal2(1, 4)
    k: int = 9
    even: int = 1
    i: int = baseIndex
    while i > 0:
        even ^= 1
        if even:
            i -= 1
        if i > k or i == 0:
            break
        ans += use[10 - k][i] * mul[10 - k]
        k -= 1
    print("GF's result is ====> ", ans, "\n")


# gaussianBackwardans store
def GBCalX(x: float, index: int):
    ans: float = table[point[3]][index]
    SCal2(-1, 3)
    k: int = 9
    even: int = 0
    i: int = point[3]
    while i > 0:
        even ^= 1
        if even:
            i -= 1
        if i > k or i == 0:
            break;
        ans += use[10 - k][i] * mul[10 - k]
        k -= 1
    lastTable[index] = ans


def GBCalY(y: float):
    baseValue: float = 10.0
    baseIndex: int = 0
    for i in range(1, 11, 1):
        tmp: float = abs(y - table[0][i])
        if tmp <= baseValue:
            baseValue = tmp
            baseIndex = i
    S[4] = (y - table[0][baseValue]) / 0.1200
    ans: float = lastTable[baseValue]
    SCal2(-1, 4)
    k: int = 9
    even: int = 0
    i: int = baseIndex
    while i > 0:
        even ^= 1
        if even:
            i -= 1
        if i > k or i == 0:
            break
        ans += use[10 - k][i] * mul[10 - k]
        k -= 1
    print("GB's result is ====> ", ans, "\n")


# Build the 10 table using every Y's colunm
def UseCal(x: float, index: int, method: int):
    use = [[float(-50.0) for index in range(11)] for _ in range(11)]
    for i in range(1, 10, 1):
        use[1][i]: float = table[i + 1][index] - table[i][index]
    for j in range(1, 10, 1):
        for k in range(1, 11 - j, 1):
            use[j + 1][k]: float = use[j][k + 1] - use[j][k]
    if method == 1:
        NFCalX(x, index)
    if method == 2:
        NBCalX(x, index)
    if method == 3:
        GFCalX(x, index)
    else:
        GBCalX(x, index)


# Build the last table by using 10 values from UseCal function
def LastCal(y: float, method: int):
    for i in range(11):
        for j in range(11):
            use[i][j] = -50.0
    for i in range(1, 10, 1):
        use[1][i]: float = lastTable[i + 1] - lastTable[i]
    for j in range(1, 10, 1):
        for k in range(1, 11 - j, 1):
            use[j + 1][k]: float = use[j][k + 1] - use[j][k]
        if method == 1:
            NFCalY(y)
        if method == 2:
            NBCalY(y)
        if method == 3:
            GFCalY(y)
        else:
            GBCalY(y)


Setup()
X: float
Y: float
while 0 == 0:
    X = input("Enter X: ")
    Y = input("Enter Y: ")
    print("f( ", X, ", ", Y, " ) ")
    print("NF's circle(s) : ", NForward(float(X)), "\n")  # NewtonForward
    for i in range(1, 11, 1):
        UseCal(X, i, 1)
    for i in range(1, 11, 1):
        print(lastTable[i], " ")
        LastCal(Y, 1)
        print("\n")
    print("NB's circle(s) : ", NBackward(X), "\n")  # NewtonBackward
    for i in range(1, 11, 1):
        UseCal(X, i, 2)
    for i in range(1, 11, 1):
        print(lastTable[i], " ")
    LastCal(Y, 2)
    print("\n")
    print("GF's circle(s) : ", GForward(X), "\n")  # gaussianForward
    for i in range(1, 11, 1):
        UseCal(X, i, 3)
    for i in range(1, 11, 1):
        print(lastTable[i], " ")
    LastCal(Y, 3)
    print("\n")
    print("GB's circle(s) : ", GBackward(X), "\n")  # gaussianBackward
    for i in range(1, 11, 1):
        UseCal(X, i, 4)
    for i in range(1, 11, 1):
        print(lastTable[i], " ")
    LastCal(Y, 4)
    print("\n")
