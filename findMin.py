import numpy as np
import random

def enumeration(func, leftX, rightX, L, accuracy = 1e-2):
    dx = accuracy / L
    x = leftX
    minVal = func(leftX)
    while x < rightX:
        minVal = min(minVal, func(x))
        x += dx
    return x-dx, minVal

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

        f1 = func(x1)
        f2 = func(x2)
        f3 = func(x3)
        a = f1
        b = (f2 - a) / (x2 - x1)
        c = (f3 - a - b * (x3 - x1)) / ((x3 - x1 )*(x3 - x2))
        newX = (x1 + x2) / 2 - b / (2 * c)

        i += 1
    return func((x3 + x1) / 2)

def midPoint(func, leftX, rightX, L, accuracy = 1e-2):
    dx = accuracy / L
    a = leftX
    b = rightX
    eps = 1e-5
    midPoint = (a+b) / 2
    deriv = (func(midPoint + dx) - func(midPoint - dx)) / (2 * dx)
    while abs(b - a) > 2 * dx:
        if deriv > eps:
            b = midPoint
        elif deriv < -1*eps:
            a = midPoint
        else:
            return func((a + b) / 2)
        midPoint = (a + b) / 2
        deriv = (func(midPoint + dx) - func(midPoint - dx)) / (2 * dx)
    return func((a + b) / 2)

def firstDeriv(func, x, dx):
    return (func(x + dx) - func(x - dx)) / (2 * dx)

def secDeriv(func, x, dx):
    return (func(x + dx) - 2 * func(x) + func(x - dx)) / (dx ** 2)

def newton(func, leftX, rightX, L, accuracy = 1e-2):
    dx = accuracy / L
    eps = 1e-5
    xk = (leftX + rightX) / 2
    first = firstDeriv(func, xk, dx)
    second = secDeriv(func, xk, dx)
    while abs(first) > eps:
        xk -= first / second

        first = firstDeriv(func, xk, dx)
        second = secDeriv(func, xk, dx)
    return func(xk)

def markwardt(func, leftX, rightX, L, accuracy = 1e-2):
    dx = accuracy / L
    xk = (leftX + rightX) / 2
    eps = 1e-5
    mu = 1
    first = firstDeriv(func, xk, dx)
    second = secDeriv(func, xk, dx)
    while abs(first) > eps:
        xk -= first / (second + mu)

        if abs(firstDeriv(func, xk, dx)) < abs(first):
            mu *= 2
        else:
            mu /= 2
        first = firstDeriv(func, xk, dx)
        second = secDeriv(func, xk, dx)
    return func(xk)
    

def brokenLines(func, leftX, rightX, L, accuracy = 1e-2):
    xOpt = (leftX + rightX) / 2 + (func(leftX) - func(rightX)) / (2 * L)
    pOpt = (func(leftX) + func(rightX)) / 2 + L * (leftX - rightX) / 2
    delta = (func(xOpt) - pOpt)
    while delta > accuracy:
        x1 = xOpt + delta / (2 * L)
        x2 = xOpt - delta / (2 * L)
        if func(x1) < func(x2):
            xOpt = x1
        else:
            xOpt = x2
        pOpt = (func(xOpt) + pOpt) / 2
        delta = func(xOpt) - pOpt

    return func(xOpt)

# func = lambda x: np.sin(x) * (x - 1) ** 2
# funcDeriv = lambda x: (x-1) * (2 * np.sin(x) + (x-1) * np.cos(x)) 
# a = -4
# b = 0

# L = 35


# print(enumeration(func, a, b, L))
# print(bitWise(func, a, b, L))
# print(dichotomy(func, a, b, L))
# print(goldenRatio(func, a, b, L))
# print(parabola(func, a, b, L))
# print(midPoint(func, a, b, L))
# print(newton(func, a, b, L))
# print(markwardt(func, a, b, L))
# print(brokenLines(func, a, b, L))