# Task: Finding the Runner-Up Score

# Concepts Used
# input() → Takes input from the user.
# int() → Converts a string to an integer.
# list() → Creates a list.
# map() → Applies a function to every element.
# set() → Removes duplicate values.
# sort() → Sorts the list in ascending order.
# [-2] → Accesses the second last element.

# Flow
# Input
# 5
# 2 3 6 6 5

# ↓

# Convert to list
# [2, 3, 6, 6, 5]

# ↓

# Remove duplicates using set()
# {2, 3, 5, 6}

# ↓

# Convert back to list
# [2, 3, 5, 6]

# ↓

# Sort the list
# [2, 3, 5, 6]

# ↓

# Take second last element
# 5

# ↓

# Print 5

# Code

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().split()))

    unique_scores = list(set(arr))

    unique_scores.sort()

    print(unique_scores[-2])

# Time Complexity
# O(n log n)

# Space Complexity
# O(n)
