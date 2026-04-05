import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd

data = pd.read_csv("data.csv")
x = data.values
pca = PCA(n_components=1)
x_pca = pca.fit_transform(x)
print(x_pca)
plt.scatter(x_pca, [0] * len(x))
plt.show()
