import numpy as np


def sig(x):
    return 1 / (1 + np.exp(-x))


def dsig(x):
    return x * (1 - x)


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Change this line
y = np.array([[0], [0], [0], [1]])  # AND
# y = np.array([[0],[1],[1],[0]]) # XOR

np.random.seed(1)

w1 = np.random.rand(2, 2)
w2 = np.random.rand(2, 1)

b1 = np.random.rand(1, 2)
b2 = np.random.rand(1, 1)

lr = 0.1

for i in range(10000):
    h = sig(X @ w1 + b1)
    o = sig(h @ w2 + b2)

    d2 = (y - o) * dsig(o)
    d1 = (d2 @ w2.T) * dsig(h)

    w2 += h.T @ d2 * lr
    w1 += X.T @ d1 * lr

    b2 += np.sum(d2, axis=0) * lr
    b1 += np.sum(d1, axis=0) * lr

print(np.round(o))
