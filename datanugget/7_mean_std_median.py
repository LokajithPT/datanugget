import pandas as p

data = {"x": [25, 35, 37, 38, 40], "y": [5, 4, 3, 2, 1]}
df = p.DataFrame(data)
print(df.mean())
print(df.std())
print(df.median())
