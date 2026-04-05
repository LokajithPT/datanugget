from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
x = data.values
gm = GaussianMixture(n_components=2)
gm.fit(x)
gl = gm.predict(x)
print(gl)
kn = KMeans(n_clusters=2)
kn.fit(x)
kl = kn.predict(x)
print(kl)
plt.figure(figsize=(10, 3))
plt.subplot(1, 2, 1)
plt.scatter(x[:, 0], x[:, 1], c=gl)
plt.subplot(1, 2, 2)
plt.scatter(x[:, 0], x[:, 1], c=kl)
plt.show()
