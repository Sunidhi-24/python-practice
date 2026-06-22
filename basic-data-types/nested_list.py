# Task: Finding Students with the Second Lowest Grade

# Concepts Used
# list() → Stores data.
# append() → Adds an item to a list.
# set() → Removes duplicate grades.
# sorted() → Sorts values.
# for loop → Iterates through items.

# Flow
# Input
# Harry 37.21
# Berry 37.21
# Tina 37.2
# Akriti 41
# Harsh 39

# ↓

# Store students

# ↓

# Get all grades

# ↓

# Remove duplicates and sort grades

# ↓

# Find second lowest grade

# ↓

# Find students having that grade

# ↓

# Sort names alphabetically

# ↓

# Print names


# Code

if __name__ == '__main__':

    students = []

    for _ in range(int(input())):

        name = input()

        grade = float(input())

        students.append([name, grade])

    grades = []

    for student in students:

        grades.append(student[1])

    second_lowest = sorted(set(grades))[1]

    names = []

    for student in students:

        if student[1] == second_lowest:

            names.append(student[0])

    names.sort()

    for name in names:

        print(name)

# Time Complexity
# O(n log n)

# Space Complexity
# O(n)
