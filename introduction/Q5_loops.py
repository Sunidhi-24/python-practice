# Loops

# Problem

# Given an integer `n`, print the square of each non-negative integer
# less than `n` on a separate line.

## Approach
# - Read the integer `n` from input.
# - Use a loop to iterate from `0` to `n-1`.
# - Print the square of each number using `i ** 2`.

## Code

n = int(input())

for i in range(n):
    print(i ** 2)

## Complexity
# - Time Complexity: O(n)
# - Space Complexity: O(1)
