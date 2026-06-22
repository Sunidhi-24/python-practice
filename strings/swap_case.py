# Task: sWAP cASE

# Concepts Used
# input() → Takes input from the user.
# swapcase() → Converts lowercase letters to uppercase and uppercase letters to lowercase.
# def → Creates a function.
# return → Returns the modified string.
# print() → Displays the output.

# Flow

# Input

# HackerRank.com presents "Pythonist 2".

# ↓

# Store the string

# ↓

# Apply swapcase()

# HackerRank → hACKERrANK
# presents → PRESENTS
# Pythonist → pYTHONIST

# ↓

# Return the modified string

# ↓

# Print the output

# ↓

# Output

# hACKERrANK.COM PRESENTS "pYTHONIST 2".

# Code

def swap_case(s):

    return s.swapcase()


if __name__ == '__main__':

    s = input()

    result = swap_case(s)

    print(result)


# Time Complexity

# O(n)

# Space Complexity

# O(n)
