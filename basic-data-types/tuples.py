# Tuples

## Objective

# Read N integers, create a tuple, and print its hash value.

# ## Input

# First line:
# N → number of integers

# Second line:
# N space-separated integers

# ## Example

# Input:

# 2
# 1 2

# Tuple:

# (1, 2)

# Output:

# 3713081631934410656



# # Important Notes

# - Tuple: Immutable collection → `t = (1, 2, 3)`

# - `input().split()` → Splits input into strings.

# ```python
# "1 2" → ['1', '2']
# ```

# - `map(int, ...)` → Converts strings to integers.

# ```python
# ['1', '2'] → 1, 2
# ```

# - `tuple()` → Creates a tuple.

# ```python
# (1, 2)
# ```

# - `hash()` → Returns a hash value for a tuple (value may vary across Python environments).

# ## Key Pattern

# ```python
# tuple(map(int, input().split()))
# ```

# **Flow:** Input → Split → Convert to int → Create tuple → Print hash.

#code
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t=tuple(integer_list)
    print(hash(t))

#used python2
