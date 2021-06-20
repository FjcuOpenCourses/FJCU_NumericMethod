import math
import warnings

import numpy as np
from sqlalchemy import null


class leastSquare:

    def __init__(self):
        self.poly1d = null
        self.m
        self.x: list == []
        self.y: list = []

    def caculatePolynomial(self):
        self.poly1d = np.poly1d(np.polyfit(self.x, self.y, self.m))
