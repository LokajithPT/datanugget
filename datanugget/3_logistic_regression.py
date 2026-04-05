import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

x = np.array([4, 5, 6, 7, 8, 9]).reshape(-1, 1)
y = np.array([100, 200, 300, 400, 500, 600])
c = (y > 200).astype(int)
m = LogisticRegression().fit(x, c)
pred = m.predict([[2]])
print("predict 3", pred)
