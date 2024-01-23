#!/bin/python3

from itertools import product

def square(x):
    return x*x

def maximize_expression(K, M, lists):
    # Generate all possible combinations of elements from the input lists
    combinations = product(*lists)
    
    # Initialize the maximum value to 0
    max_value = 0

    # Iterate through each combination
    for comb in combinations:
        # Calculate the value of the expression and take the modulo M
        value = sum(square(x) for x in comb) % M
        
        # Update the maximum value if the current value is greater
        max_value = max(max_value, value)

    # Return the maximum value of the expression
    return max_value

if __name__ == "__main__":
    # Read K (number of lists) and M (modulo value) from input
    K, M = map(int, input().rstrip().split())

    # Read the lists from input and extract the elements
    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    # Call the maximize_expression function and print the result
    result = maximize_expression(K, M, lists)
    print(result)
