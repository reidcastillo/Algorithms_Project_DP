from knapsack import knapsack, post_process, read_input, display_results


if __name__ == "__main__":
    file_name = input("What is the name of your input file?\n")
    values, weights, capacity = read_input(file_name)
    OPT, OPT_value = knapsack(values, weights, capacity)
    selected_items = post_process(OPT, values, weights, capacity)
    display_results(OPT_value, selected_items)
