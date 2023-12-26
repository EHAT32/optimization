import numpy as np
import random

def enumeration(func, leftX, rightX, L, accuracy = 1e-2):
    dx = accuracy / L
    x = leftX
    minVal = func(leftX)
    while x < rightX:
        minVal = min(minVal, func(x))
        x += dx
    return minVal

def bitWise(func, leftX, rightX, L, accuracy = 1e-2):
    dx = accuracy / L
    x = leftX
    minVal = func(leftX)
    while x < rightX:
        if func(x) > minVal:
            if 2 * accuracy > dx:
                return func((x + x - dx) / 2)
            else:
                dx *= -0.25
        minVal = min(minVal, func(x))
        x += dx
    return minVal

def dichotomy(func, leftX, rightX, L, accuracy = 1e-2):
    eps = accuracy / L
    delta = eps / 2
    a = leftX
    b = rightX
    xLeft = (a + b) / 2 - delta
    xRight = (a + b) / 2 + delta
    while b - a > 2 * eps:
        if func(xLeft) < func(xRight):
            b = xRight
        else:
            a = xLeft
        xLeft = (a + b) / 2 - delta
        xRight = (a + b) / 2 + delta
        # print(xRight - xLeft - 2 * delta)
    return func((a + b) / 2)

def goldenRatio(func, leftX, rightX, L, accuracy = 1e-2):
    ratio = (1 + np.sqrt(5)) / 2
    a = leftX
    b = rightX
    eps = accuracy / L
    xLeft = b - (b - a) / ratio
    xRight = a + (b - a) / ratio
    while b - a > eps:
        y1 = func(xLeft)
        y2 = func(xRight)
        if y1 >= y2:
            a = xLeft
        else:
            b = xRight
        xLeft = b - (b - a) / ratio
        xRight = a + (b - a) / ratio  
    return func((a + b) / 2)

def findTriple():
    ...

def parabola(func, leftX, rightX, L, accuracy = 1e-2):
    ITER_NUM = 10000
    dx = accuracy / L
    i = 0
    x1 = leftX
    x3 = rightX
    x2 = (x1 + x3) / 2
    f1 = func(x1)
    f2 = func(x2)
    f3 = func(x3)
    j = 0
    while f2 > f3:
        f2 = func(x3 - j * dx)
        j += 1
        x2 = x3 - j * dx
    j = 0
    while f2 > f1:
        f2 = func(x1 + j * dx)
        j +=1
        x2 = x1 + j * dx
    #coeffs
    a = f1
    b = (f2 - a) / (x2 - x1)
    c = (f3 - a - b * (x3 - x1)) / ((x3 - x1 )*(x3 - x2))
    newX = (x1 + x2) / 2 - b / (2 * c)
    while abs(x3 - x1) > dx and i < ITER_NUM:
        if newX > x2:
            if func(newX) > f2:
                x3 = x2
            else:
                x1 = x2
        else:
            if func(newX) > f2:
                x1 = x2
            else:
                x3 = x2
        x2 = newX

        # x2 = newX
        f1 = func(x1)
        f2 = func(x2)
        f3 = func(x3)
        # newX2 = x3
        # while not (f1 > f2 and f2 < f3):
        #     newX2 -= dx
        #     f2 = func(newX2)

        a = f1
        b = (f2 - a) / (x2 - x1)
        c = (f3 - a - b * (x3 - x1)) / ((x3 - x1 )*(x3 - x2))
        newX = (x1 + x2) / 2 - b / (2 * c)

        i += 1
    return func(newX)

func = lambda x: np.sin(x) * (x - 1) ** 2
funcDeriv = lambda x: (x-1) * (2 * np.sin(x) + (x-1) * np.cos(x)) 
a = -4
b = 0

L = 35


# print(enumeration(func, a, b, L))
# print(bitWise(func, a, b, L))
# print(dichotomy(func, a, b, L))
# print(goldenRatio(func, a, b, L))
# print(parabola(func, a, b, L))

