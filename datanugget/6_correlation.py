import pandas as p
from sklearn.datasets import load_iris

data = load_iris()
df = p.DataFrame(data.data, columns=data.feature_names)
print(df.corr())
