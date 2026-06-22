# Task: What's Your Name?

# Concepts Used
# input() → Takes input from the user.
# def → Creates a function.
# print() → Displays output on the screen.
# f-string → Inserts variables inside a string.
# Function call → Executes the function.

# Flow

# Input

# Ross
# Taylor

# ↓

# Store first name
# first_name = "Ross"

# ↓

# Store last name
# last_name = "Taylor"

# ↓

# Call function
# print_full_name(first_name, last_name)

# ↓

# Create the sentence
# "Hello Ross Taylor! You just delved into python."

# ↓

# Print the sentence

# ↓

# Output

# Hello Ross Taylor! You just delved into python.

# Code

def print_full_name(first, last):

    print(f"Hello {first} {last}! You just delved into python.")


if __name__ == '__main__':

    first_name = input()

    last_name = input()

    print_full_name(first_name, last_name)


# Time Complexity

# O(1)

# Space Complexity

# O(1)
