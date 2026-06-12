# Print Function

# Problem

# Given an integer `n`, print the numbers from `1` to `n`
# on the same line without spaces or separators.

## Approach
# - Read the integer `n` from input.
# - Use a loop from `1` to `n`.
# - Print each number using `end=""` to avoid a new line after each print.

## Code
n = int(input())

for i in range(1, n + 1):
    print(i, end="")

## Complexity
# - Time Complexity: O(n)
# - Space Complexity: O(1)

## Notes
# - `end=""` prevents print() from moving to a new line after each output.
# - Default behavior is `end="\n"` (new line).
# - `sep=""` removes the separator between multiple values in a single print statement.
# - In this problem, `sep=""` is not required because only one value (`i`) is being printed.
# - Example:
#     print(1, 2, 3, sep="")
#     Output: 123
#
# - Example:
#     print(1, end="")
#     print(2, end="")
#     print(3, end="")
#     Output: 123
