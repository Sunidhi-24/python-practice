# Write a Function

# Problem

# Given a year, determine whether it is a leap year.
# Return True if it is a leap year, otherwise return False.
#
# Leap Year Rules:
# - Divisible by 400 → Leap Year
# - Divisible by 100 → Not a Leap Year
# - Divisible by 4 → Leap Year
# - Otherwise → Not a Leap Year

## Approach
# - Check if the year is divisible by 400.
# - If yes, return True.
# - Otherwise, check if it is divisible by 100.
# - If yes, return False.
# - Otherwise, check if it is divisible by 4.
# - If yes, return True.
# - Otherwise, return False.

## Code
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

## Complexity
# - Time Complexity: O(1)
# - Space Complexity: O(1)
