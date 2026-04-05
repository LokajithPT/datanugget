import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

x = np.array([[2, 133], [3, 156], [4, 200], [5, 112], [6, 213]])
y = np.array([1, 1, 0, 1, 0])
m = SVC(kernel="linear")
m.fit(x, y)
plt.scatter(x[:, 0], x[:, 1], c=y)
w = m.coef_[0]
b = m.intercept_
X = np.linspace(1, 10, 100)
line = -(w[0] * X + b) / w[1]
plt.plot(X, line)
plt.show()
