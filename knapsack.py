
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
            items.append(n-1)   # The item contributes to the value, so it is included
            w -= weights[n-1]
            n -= 1

    return items

