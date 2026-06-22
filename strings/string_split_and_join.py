# Task: String Split and Join

# Concepts Used
# input() → Takes input from the user.
# split() → Splits a string into a list using a delimiter.
# join() → Joins list elements into a single string.
# def → Creates a function.
# return → Returns the modified string.
# print() → Displays the output.

# Flow

# Input

# this is a string

# ↓

# Split the string using space

# ['this', 'is', 'a', 'string']

# ↓

# Join the list using '-'

# this-is-a-string

# ↓

# Return the modified string

# ↓

# Print the output

# ↓

# Output

# this-is-a-string

# Code

def split_and_join(line):

    words = line.split(" ")

    return "-".join(words)


if __name__ == '__main__':

    line = input()

    result = split_and_join(line)

    print(result)


# Time Complexity

# O(n)

# Space Complexity

# O(n)
