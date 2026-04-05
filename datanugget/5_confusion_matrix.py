import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X, y = make_classification(n_samples=200, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
clf = LogisticRegression().fit(X_train, y_train)
ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, cmap="Blues")
plt.show()
