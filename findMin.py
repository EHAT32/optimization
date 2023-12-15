import numpy as np

def enumeration(func, leftX, rightX, L, accuracy = 0.01):
    dx = accuracy / L
    x = leftX
    minVal = func(leftX)
    while x < rightX:
        minVal = min(minVal, func(x))
        x += dx
    return minVal

def bitWise(func, leftX, rightX, L, accuracy = 0.01):
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

# func = lambda x: np.sin(x) * (x - 1) ** 2
# funcDeriv = lambda x: (x-1) * (2 * np.sin(x) + (x-1) * np.cos(x)) 
# a = -4
# b = 0

# forDeriv = np.linspace(a, b, 5000)

# L = np.max(np.abs(funcDeriv(forDeriv)))
# L *= 1.1

# print(enumeration(func, a, b, L))
# print(bitWise(func, a, b, L))


