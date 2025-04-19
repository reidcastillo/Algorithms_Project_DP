
# Implements the knapsack algorithm (referenced from Chapter 6 PowerPoint slides)
def knapsack(values, weights, capacity):

    # The number of values and weights does not match
    if len(values) != len(weights):
        raise ValueError("values and weights must be the same length")
    n = len(values)

    # Initialize the dp array that stores the max value possible at each possible remaining knapsack capacity (n+1 by capacity+1)
    OPT = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):   # For each item
        for w in range(1, capacity + 1):   # For each possible knapsack capacity
            # Case 1: If the object is greater than the capacity, it won't be selected
            if weights[i-1] > w:
                OPT[i][w] = OPT[i-1][w]   # Solution is the same as the previous optimal solution

            # Case 2: The object can be selected, pick the max between the value of not picking the item,
            # and the new value gained from selecting the item
            else:
                OPT[i][w] = max(OPT[i-1][w], values[i-1] + OPT[i-1][w - weights[i-1]])

    return OPT, OPT[n][capacity]   # Returns the dp array and the max value obtainable with the full knapsack size and n possible items

# Optimized knapsack approach that uses a 1d array only, optimizing the space complexity to O(W)
def optimized_knapsack(values, weights, capacity):

    # The number of values and weights does not match
    if len(values) != len(weights):
        raise ValueError("values and weights must be the same length")
    n = len(values)

    # Initialize the dp array, but only of size capacity + 1 this time. Each index holds optimal value for each possible capacity
    OPT = [0] * (capacity + 1)

    for i in range(1, n + 1):   # For each item
        for w in range(capacity, weights[i-1] - 1, -1):   # For each possible knapsack capacity, in reverse

            # Pick max of two cases: Don't take the item = the same solution to the prior weight
            # Take the item = the new value is the new items value + the optimal value from the prior weight
            OPT[w] = max(OPT[w], values[i-1] + OPT[w - weights[i - 1]])

    return OPT[capacity]   # Returns the dp array and the max value obtainable with the full knapsack size and n possible items

# Post-processing that obtains a list of the items selected (also references the PowerPoint)
def post_process(OPT, values, weights, capacity):

    n = len(values)  # Starting at the last item and full capacity
    w = capacity
    items = []

    while n > 0 and w > 0:
        if OPT[n][w] == OPT[n-1][w]:   # OPT does not include the item, as it does not add any value
            n -= 1
            continue
        else:
            items.append(n)   # The item contributes to the value, so it is included
            w -= weights[n-1]
            n -= 1

    return list(reversed(items))

# Function that parses the input from a text file (1st line = values, 2nd line = weights, 3rd line = capacity)
def read_input(file):

    with open(file, 'r') as file:
        lines = file.readlines()

        first_line = lines[0]
        values = []
        for value in first_line.split():
            values.append(int(value))

        second_line = lines[1]
        weights = []
        for weight in second_line.split():
            weights.append(int(weight))

        capacity = int(lines[2])

    return values, weights, capacity

# Function that displays the results of the Knapsack algorithm
def display_results(value, items):
    print("Optimal value:", value)
    chosen = "Items Chosen: "

    for i, item in enumerate(items):
        if i == len(items) - 1:
            chosen += str(item)
        else:
            chosen += str(item) + ", "

    print(chosen)


