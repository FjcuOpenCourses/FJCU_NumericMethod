import os

import numpy as np
from matplotlib import pyplot as plt

from cubicSpline.subicSpline import cubicSpline


def main():
    myCubicSpline = cubicSpline()
    myCubicSpline.Setup(os.path.dirname(os.path.realpath(__file__)) + "\\datasheet.in")

    for i in range(myCubicSpline.n - 1):
        myCubicSpline.H[i] = myCubicSpline.dataX[i + 1] - myCubicSpline.dataX[i]


    if myCubicSpline.case == 1:
        myCubicSpline.A[0][0] = 2 * (myCubicSpline.H[0] + myCubicSpline.H[1])
        myCubicSpline.A[0][1] = myCubicSpline.H[1]
        myCubicSpline.A[myCubicSpline.n - 3][myCubicSpline.n - 4] = myCubicSpline.H[myCubicSpline.n - 3]
        myCubicSpline.A[myCubicSpline.n - 3][myCubicSpline.n - 3] = 2 * (
                    myCubicSpline.H[myCubicSpline.n - 3] + myCubicSpline.H[myCubicSpline.n - 2])

    elif myCubicSpline.case == 2:
        myCubicSpline.A[0][0] = 3 * myCubicSpline.H[0] + 2 * myCubicSpline.H[1]
        myCubicSpline.A[0][1] = myCubicSpline.H[1]
        myCubicSpline.A[myCubicSpline.n - 3][myCubicSpline.n - 4] = myCubicSpline.H[myCubicSpline.n - 3]
        myCubicSpline.A[myCubicSpline.n - 3][myCubicSpline.n - 3] = 2 * myCubicSpline.H[myCubicSpline.n - 3] + 3 * \
                                                                    myCubicSpline.H[myCubicSpline.n - 2]
    else:
        myCubicSpline.A[0][0] = (myCubicSpline.H[0] + myCubicSpline.H[1]) * (
                    myCubicSpline.H[0] + 2 * myCubicSpline.H[1]) / myCubicSpline.H[1]
        myCubicSpline.A[0][1] = (myCubicSpline.H[1] ** 2 - myCubicSpline.H[0] ** 2) / myCubicSpline.H[1]
        myCubicSpline.A[myCubicSpline.n - 3][myCubicSpline.n - 4] = (myCubicSpline.H[myCubicSpline.n - 3] ** 2 -
                                                                     myCubicSpline.H[myCubicSpline.n - 2] ** 2) / \
                                                                    myCubicSpline.H[myCubicSpline.n - 3]
        myCubicSpline.A[myCubicSpline.n - 3][myCubicSpline.n - 3] = (myCubicSpline.H[myCubicSpline.n - 2] +
                                                                     myCubicSpline.H[myCubicSpline.n - 3]) * (
                                                                                myCubicSpline.H[
                                                                                    myCubicSpline.n - 2] + 2 *
                                                                                myCubicSpline.H[myCubicSpline.n - 3]) / \
                                                                    myCubicSpline.H[myCubicSpline.n - 3]

    for i in range(1, myCubicSpline.n - 3):
        myCubicSpline.A[i][i - 1] = myCubicSpline.H[i]
        myCubicSpline.A[i][i] = 2 * (myCubicSpline.H[i] + myCubicSpline.H[i + 1])
        myCubicSpline.A[i][i + 1] = myCubicSpline.H[i + 1]

    for i in range(myCubicSpline.n - 2):
        u = (myCubicSpline.dataY[i + 2] - myCubicSpline.dataY[i + 1]) / myCubicSpline.H[i + 1]
        d = (myCubicSpline.dataY[i + 1] - myCubicSpline.dataY[i]) / myCubicSpline.H[i]
        myCubicSpline.B[i] = 6 * (u - d)

    S = np.linalg.solve(myCubicSpline.A, myCubicSpline.B)
    print("Origin S = ")
    print(S)

    if myCubicSpline.case == 1:
        S = np.insert(S, 0, 0)
        S = np.append(S, 0)

    elif myCubicSpline.case == 2:
        S = np.insert(S, 0, S[0])
        S = np.append(S, S[-1])
    else:
        t1 = ((myCubicSpline.H[0] + myCubicSpline.H[1]) * S[0] - myCubicSpline.H[0] * S[1]) / myCubicSpline.H[1]
        t2 = ((myCubicSpline.H[myCubicSpline.n - 3] + myCubicSpline.H[myCubicSpline.n - 2]) * myCubicSpline.S[-1] -
              myCubicSpline.H[myCubicSpline.n - 2] * S[-2]) / myCubicSpline.H[myCubicSpline.n - 3]
        S = np.insert(S, 0, t1)
        S = np.append(S, t2)

    for i in range(myCubicSpline.n - 1):
        myCubicSpline.ai[i] = (S[i + 1] - S[i]) / (6 * myCubicSpline.H[i])
        myCubicSpline.bi[i] = S[i] / 2
        myCubicSpline.ci[i] = (float(myCubicSpline.dataY[i + 1]) - float(myCubicSpline.dataY[i])) / myCubicSpline.H[
            i] - (2 * myCubicSpline.H[i] * S[i] + myCubicSpline.H[i] * S[i + 1]) / 6
        myCubicSpline.di[i] = float(myCubicSpline.dataY[i])

    print(myCubicSpline.ai[7], myCubicSpline.bi[7], myCubicSpline.ci[7], myCubicSpline.di[7])

    plt.plot(myCubicSpline.dataX, myCubicSpline.dataY, '.')

    # Print every poly in data interval
    for i in range(myCubicSpline.n - 1):
        d = np.linspace(myCubicSpline.dataX[i], myCubicSpline.dataX[i + 1], 100)
        plt.plot(d, myCubicSpline.Poly(d, i), '--')

    plt.show()


main()
