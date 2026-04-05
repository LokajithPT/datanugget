from sklearn.model_selection import train_test_split

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
xtr, ytr, xte, yte = train_test_split(x, y, test_size=0.2, random_state=20)
print(xtr, ytr, xte, yte)
