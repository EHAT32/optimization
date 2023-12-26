import numpy as np

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

func = lambda x: np.sin(x) * (x - 1) ** 2
funcDeriv = lambda x: (x-1) * (2 * np.sin(x) + (x-1) * np.cos(x)) 
a = -4
b = 0

# forDeriv = np.linspace(a, b, 5000)

L = 35

# print(enumeration(func, a, b, L))
# print(bitWise(func, a, b, L))
# print(dichotomy(func, a, b, L))
print(goldenRatio(func, a, b, L))


