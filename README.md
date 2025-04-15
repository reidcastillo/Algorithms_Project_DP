# Algorithms Implementation and Performance Analysis Project - Dynamic Programming

## This project implements the Knapsack Problem dynamic programming algorithm. Given N objects with corresponding values and weights, and a knapsack with a capacity of W, this algorithm finds the maximum value that can be obtained by adding objects to the knapsack without exceeding W. The project was done using Python.

### Instructions:
- Create a text file with your desired input. This file is formatted in 3 lines: a list of item values, a list of item weights, and the knapsack capacity (all integer values).  
  i.e  
  1 2 3 4 5  
  10, 20, 30, 40, 50  
  100  

- Run main.py  
  This will prompt you to give the name of your input file. From here, the optimal solution along with the items chosen will be displayed in the terminal.

### Files:
- knapsack.py: contains the Knapsack algorithm functions, along with input and output functions.
- main.py: Takes in a users input file and computes the optimal solution
- experimental_analysis.py: Used to experiemnt various inputs and analyze runtime and memory usage. Also generates visualizations.

### Approach:
This program uses two functions to solve the Knapsack problem.  
1. knapsack(values, weights, capacity) - this function takes in a list of values, weights, and the integer capacity. Using these it finds the max value obtainable using dynamic-programming.
   It does this by initializing a dp 2d-array that stores the solution to each sub-problem (i, w) - subset of items 1 to i and a weight limit w. At each item, the algorithm has two   
   choices: put the item in the knapsack or ignore the item. These two cases are considered in the algorithm. If the item is ignored, the dp solution for that item is the same as the   
   solution for the item subset i-1. If the item is taken, we consider the new value of the knapsack with the reduced weight capacity, and the value of not taking the item. The greater of 
   these two is selected.

2. post_process(OPT, values, weights, capacity) - this function does backtracking to determine which items were selected to obtain the optimal solution. It does this by iterating   
   backawards on the dp array, and determining whether each item encountered contributed to the current sub-problems solution. If the items value was utilized in the solution, then add   
   that item to the list. This function then returns the list of these items in the order they were provided.

### Time Complexity:
  The time complexity for this solution is big theta(n W). This is due to computing the optimal solution for each item and each possible capacity of the knapsack from 0 to W. If W is 
  sufficiently small, this time complexity is polynomial (pesudo-polynomial).

### Experiemntal Analysis:
In order to check the preformance of the program a benchmark function was created, this script will choose random inputs that increase in size and will measure the run time and the memory required. 
capacity of the knapsack (w) is also logged and is used in each case to reflect the complexity O(nW) of the algo.  The results are printed in the terminal when the file is run and the results are saved too times/memory csv so it can be used to make graphs for the report. 
   

