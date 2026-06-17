# List Comprehensions

## Objective

# Generate all possible coordinates [i, j, k] such that:

# 0 ≤ i ≤ x
# 0 ≤ j ≤ y
# 0 ≤ k ≤ z

# Exclude coordinates where:

# i + j + k == n

# Return the remaining coordinates in a list.

# ## Example

# Input:

# x = 1
# y = 1
# z = 1
# n = 2

# Output:

# [[0,0,0],
#  [0,0,1],
#  [0,1,0],
#  [1,0,0],
#  [1,1,1]]


# Important Notes

# List comprehension syntax:

# [expression for item in iterable if condition]

# General pattern:

# [action
#  for i
#  for j
#  for k
#  if condition]

# range(x + 1)

# Why +1?

# range(2) → [0, 1]

# because range excludes the ending value.

# Condition:

# i + j + k != n

# != means "not equal to".

# Normal loops:

# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i + j + k != n:
#                 print([i, j, k])

# Convert loops to list comprehension:

# [action
#  for i
#  for j
#  for k
#  if condition]


#code

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    print(result)
