from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
import numpy as np

y = [1, 0, 1, 1, 0, 0, 1, 0]
py = [0, 1, 1, 1, 1, 1, 1, 1]
print(
    r2_score(y, py),
    accuracy_score(y, py),
    f1_score(y, py),
    precision_score(y, py),
    recall_score(y, py),
)
print(np.sqrt(mean_squared_error(y, py)))
