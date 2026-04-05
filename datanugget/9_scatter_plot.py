import matplotlib.pyplot as plt

x = [12, 13, 14, 15, 16, 17, 18, 19]
y = [23, 23, 26, 28, 28, 29, 22, 2]
plt.scatter(x, y, c=y, cmap="coolwarm", s=90)
plt.show()
plt.legend()
