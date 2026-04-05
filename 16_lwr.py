import math


def lwr(x, y, x0, tau):
    num = 0
    den = 0

    for i in range(len(x)):
        w = math.exp(-((x[i] - x0) * 2) / (2 * tau * 2))
        num += w * y[i]
        den += w

    return num / den


x = [1, 2, 8]
y = [2, 4, 6]

x0 = 2.5
tau = 2.5

result = lwr(x, y, x0, tau)

print("Predicted value at x =", x0, "is", result)
