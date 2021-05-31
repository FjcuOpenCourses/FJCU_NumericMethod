# 參考標準常態分配表，製作一份更精準的常態分配表
#
# 1. 一般常態分配表是到小數點以下第二位
#
#     例如  P( z < 0.68 )=0.7517
#
#     常態分配表，查表  z 的範圍，小於 0.00 , 0.01, 0.02, 0.03 ......1.00, 1.01, 1.02, 1.03, ......
#
#     表格中， z 的範圍只到小數點後第二位
#
# 2. Hw. 3 要求同學做出來的標準常態分配表，z 的範圍是到小數點後第三位
#
#     例如 P( z < 1.284) 直接查表就可以得到
#
# 3. 這個表格，z 的範圍由 0.000 ~ 4.999
#
# 同學說，聽不懂題目。應該是把常態分配拋到九霄雲外，才不知老師的要求
#
# 建議，先回顧標準常態分配表的意義。慢慢就知道該怎麼作了
import math

from scipy.integrate import quad

table = [[[] for _ in range(101)] for _ in range(55)]


def probabilityDensityFunction(x: float):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-1 * (x * x) / 2)


def conditionalProbability(a: float, b: float):
    return quad(probabilityDensityFunction, a, b)


def initTable():
    table[0][0]: float = 0.0
    table[0][1]: float = 0.0
    table[1][0]: float = 0.00
    for i in range(2, 101, 1):
        table[0][i]: float = table[0][i - 1] + 0.01

    for i in range(2, 55, 1):
        table[i][0]: float = table[i - 1][0] + 0.1

    for i in range(1, 55, 1):
        for j in range(1, 101, 1):
            table[i][j], err = conditionalProbability(0.0, table[i][0] + table[0][j])


def caculateNormalDistribute(number: float):
    Xcoodinate: float = float(int(number * 10) / 10)
    Ycoodinate: float =  float(int(number * 100) % 100) / 100
    baseX:int=0
    baseY:int=0
    while table[baseX+1][0]<=Xcoodinate:
        baseX+=1
    while table[0][baseY+1]<=Ycoodinate:
        baseY+=1
    return table[baseX][baseY]


initTable()
while True:
    X = input("Enter X: ")
    print("P( z <", X, ")=", caculateNormalDistribute(float(X)), "\n")
