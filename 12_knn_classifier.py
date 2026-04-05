from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

data = load_iris()
x = data.data
y = data.target
knn = KNeighborsClassifier()
knn.fit(x, y)
pred = knn.predict(x)
for i in range(len(y)):
    if y[i] == pred[i]:
        print("CORRECT", i, y[i], pred[i])
    else:
        print("WRONG", i, y[i], pred[i])
