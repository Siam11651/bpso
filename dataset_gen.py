import pickle
import random

if __name__ == "__main__":
    N = 1000

    # Generate profits and weights between 1 and 1000
    profits = [random.randint(1, 1000) for _ in range(N)]
    weights = [random.randint(1, 1000) for _ in range(N)]
    data = pickle.dumps((500000, list(zip(profits, weights))))
    file = open("dataset", mode="wb")

    file.write(data)
    file.close()