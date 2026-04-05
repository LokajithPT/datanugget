import os

SOLUTIONS = {}

files = [
    ("1", "pca"),
    ("2", "svm_linear"),
    ("3", "logistic_regression"),
    ("4", "linear_regression"),
    ("5", "confusion_matrix"),
    ("6", "correlation"),
    ("7", "mean_std_median"),
    ("8", "train_test_split"),
    ("9", "scatter_plot"),
    ("10", "metrics"),
    ("11", "read_csv"),
    ("12", "knn_classifier"),
    ("13", "perceptron"),
    ("14", "naive_bayes"),
    ("15", "gmm_kmeans"),
    ("16", "lwr"),
    ("17", "entropy"),
    ("18", "nn_and"),
]

files_dict = {num: name for num, name in files}

base_dir = os.path.dirname(os.path.abspath(__file__))

for num, name in files:
    filepath = os.path.join(base_dir, f"{num}_{name}.py")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            SOLUTIONS[num] = f.read()


def help():
    print("Available programs:")
    for num in sorted(SOLUTIONS.keys(), key=lambda x: int(x)):
        name = files_dict.get(num, "unknown")
        print(f" - {num} -> {name}")


def get(num, filename):
    if num in SOLUTIONS:
        with open(filename, "w") as f:
            f.write(SOLUTIONS[num])
        print(f"Generated {filename}")
    else:
        print(f"Not found: {num}")
        print("Run dn.help() to see available files.")
