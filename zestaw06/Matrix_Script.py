#!/bin/python3

import math
import os
import random
import re
import sys

# Read dimensions of the matrix from input
dimensions = input().rstrip().split()

# Convert dimensions to integers
n = int(dimensions[0])  # Number of rows
m = int(dimensions[1])  # Number of columns

matrix = []

# Read the matrix from input
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Transpose the matrix using zip(*matrix)
transposed_matrix = zip(*matrix)

# Concatenate the characters in each column to form the decoded text
decoded_text = "".join("".join(col) for col in transposed_matrix)

# Use regular expression to replace non-alphanumeric characters between alphanumeric characters with a space
decoded_text = re.sub(
    r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])", " ", decoded_text
)

# Print the final decoded text
print(decoded_text)
