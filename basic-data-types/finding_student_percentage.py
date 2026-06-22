# Task: Finding Student Average 
# Concepts Used
# input() → Takes input from the user.
# int() → Converts a string to an integer.
# dictionary {} → Stores data as key : value pairs.
# split() → Splits a string into a list using spaces.
# * (unpacking) → Stores all remaining values into a list.
# map() → Applies a function to every element.
# float() → Converts values to decimal numbers.
# list() → Converts a map object into a list.
# sum() → Adds all elements.
# len() → Returns the number of elements.
# f"{value:.2f}" → Prints a number with 2 decimal places.


# Flow
# Input

# Krishna 67 68 69

# ↓

# split()

# ['Krishna', '67', '68', '69']

# ↓

# name, *line

# name = Krishna
# line = ['67', '68', '69']

# ↓

# list(map(float, line))

# [67.0, 68.0, 69.0]

# ↓

# Store in dictionary

# {
# 'Krishna': [67.0, 68.0, 69.0]
# }

# ↓

# Calculate average

# sum(marks) / len(marks)

# ↓

# Print with 2 decimal places


# Code
if __name__ == '__main__':

    n = int(input())

    student_marks = {}

    for _ in range(n):

        name, *line = input().split()

        scores = list(map(float, line))

        student_marks[name] = scores

    query_name = input()

    average = sum(student_marks[query_name]) / len(student_marks[query_name])

    print(f"{average:.2f}")
  
# Time Complexity
# O(n)
# Space Complexity
# O(n)
