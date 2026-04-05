import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([4, 5, 6, 7, 8, 9]).reshape(-1, 1)
y = np.array([100, 200, 300, 400, 500, 600])
m = LinearRegression().fit(x, y)
print("slope", m.coef_[0])
print("intercept", m.intercept_)
print("pridict for 27", m.predict([[3]])[0])
plt.scatter(x, y)
plt.plot(x, m.predict(x))
plt.show()
