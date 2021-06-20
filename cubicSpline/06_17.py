import os

import numpy as np
from matplotlib import pyplot as plt

from cubicSpline.subicSpline import cubicSpline


def main():
    myCubicSpline = cubicSpline()
    myCubicSpline.Setup(os.path.dirname(os.path.realpath(__file__)) + "\\datasheet.in")



    myCubicSpline.generatingAMaxtrixValue()

    myCubicSpline.generatingBMaxtrixValue()

    myCubicSpline.fixTheSMatrix()

    print(myCubicSpline.ai[7], myCubicSpline.bi[7], myCubicSpline.ci[7], myCubicSpline.di[7])

    plt.plot(myCubicSpline.dataX, myCubicSpline.dataY, '.')

    # Print every poly in data interval
    for i in range(myCubicSpline.n - 1):
        d = np.linspace(myCubicSpline.dataX[i], myCubicSpline.dataX[i + 1], 100)
        plt.plot(d, myCubicSpline.Poly(d, i), '--')
    plt.show()


main()
