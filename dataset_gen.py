import pickle

if __name__ == "__main__":
    filepath = "datasets/ks16a"
    file = open(filepath + "/c.txt", mode="r")
    capacity = int(file.read())

    file.close()

    file = open(filepath + "/p.txt", mode="r")
    profits = []

    for line in file.readlines():
        profits.append(int(line))
    
    file.close()

    file = open(filepath + "/w.txt", mode="r")
    weights = []

    for line in file.readlines():
        weights.append(int(line))
    
    file.close()

    data = pickle.dumps((capacity, list(zip(profits, weights))))
    file = open("dataset", mode="wb")

    file.write(data)
    file.close()