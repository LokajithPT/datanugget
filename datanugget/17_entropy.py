import math


def entropy(data):
    yes = data.count("yes")
    no = data.count("no")
    tot = len(data)

    if yes == 0 or no == 0:
        return 0

    p1 = yes / tot
    p2 = no / tot

    return -(p1 * math.log2(p1) + p2 * math.log2(p2))


def info(data, attr):
    gain = entropy(data)

    for v in set(attr):
        subset = []
        for i in range(len(attr)):
            if attr[i] == v:
                subset.append(data[i])

        gain -= (len(subset) / len(data)) * entropy(subset)

    return gain


play = ["no", "no", "yes", "yes"]

outlook = ["sunny", "sunny", "overcast", "rain"]
temp = ["hot", "hot", "hot", "mild"]
wind = ["weak", "strong", "weak", "weak"]
humidity = ["high", "high", "high", "high"]


print("entropy:", entropy(play))
print("information gain(outlook):", info(play, outlook))
print("information gain(temp):", info(play, temp))
print("information gain(wind):", info(play, wind))
print("information gain(humidity):", info(play, humidity))
