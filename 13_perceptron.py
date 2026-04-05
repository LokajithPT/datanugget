x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]
w = [0, 0]
b = 0
lr = 0.5
for i in range(len(x)):
    net = x[i][0] * w[0] + x[i][1] * w[1] + b
    out = 1 if net >= 0 else 0
    error = y[i] - out
    w[0] += lr * error * x[i][0]
    w[1] += lr * error * x[i][1]
    b += lr * error
print(w, b)
