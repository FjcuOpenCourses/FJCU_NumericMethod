from differenceTable.Interpolation import interpolation


def main():
    sample = interpolation()
    sample.Setup()
    X: float
    Y: float
    while 0 == 0:
        X = float(input("Enter X: "))
        Y = float(input("Enter Y: "))
        print("f( ", X, ", ", Y, " ) ")

        print("NF's circle(s) : ", sample.NForward(float(X)), "\n")  # NewtonForward

        for i in range(1, 11, 1):
            sample.deltaCal(X, i, sample.NFCalX(X, i))

        sample.LastCal(Y, 1)
        print("\n")

        print("NB's circle(s) : ", sample.NBackward(X), "\n")  # NewtonBackward

        for i in range(1, 11, 1):
            sample.deltaCal(X, i, 2)

        sample.LastCal(Y, 2)
        print("\n")

        print("GF's circle(s) : ", sample.GForward(X), "\n")  # gaussianForward
        for i in range(1, 11, 1):
            sample.deltaCal(X, i, 3)

        sample.LastCal(Y, 3)
        print("\n")

        print("GB's circle(s) : ", sample.GBackward(X), "\n")  # gaussianBackward
        for i in range(1, 11, 1):
            sample.deltaCal(X, i, 4)

        sample.LastCal(Y, 4)
        print("\n")


main()
