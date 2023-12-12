import pickle

if __name__ == "__main__":
    file = open("dataset", mode="rb")
    data = file.read()
    data = pickle.loads(data)
    knapsack_size = data[0]
    knapsack_weights = data[1]

    print(f"knapsack size: {knapsack_size}")
    print("knapsack weights:")
    print("price\tweight")

    for item in knapsack_weights:
        print(f"{item[0]}\t{item[1]}")