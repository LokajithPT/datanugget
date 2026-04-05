from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

data = load_iris()
x = data.data
y = data.target
xtr, xte, ytr, yte = train_test_split(x, y, test_size=20, random_state=42)
gn = GaussianNB()
gn.fit(xtr, ytr)
pred = gn.predict(xte)
acc = accuracy_score(pred, yte)
print(acc * 100)
print(classification_report(pred, yte))
