# Task: Mutations

# Concepts Used
# input() → Takes input from the user.
# slicing → Extracts parts of a string.
# + → Concatenates (joins) strings.
# def → Creates a function.
# return → Returns the modified string.
# split() → Separates input values.
# print() → Displays the output.

# Flow

# Input

# abracadabra
# 5 k

# ↓

# Store the string

# abracadabra

# ↓

# Split the string into two parts

# string[:5] → abrac
# string[6:] → dabra

# ↓

# Insert the new character

# abrac + k + dabra

# ↓

# Create the modified string

# abrackdabra

# ↓

# Return the modified string

# ↓

# Print the output

# ↓

# Output

# abrackdabra

# Code

def mutate_string(string, position, character):

    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':

    s = input()

    i, c = input().split()

    new_string = mutate_string(s, int(i), c)

    print(new_string)


# Time Complexity

# O(n)

# Space Complexity

# O(n)
