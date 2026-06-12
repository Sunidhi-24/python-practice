# Python If-Else | HackerRank

# Problem
# Print:

# - `Weird` if `n` is odd
# - `Not Weird` if `n` is even and `2 ≤ n ≤ 5`
# - `Weird` if `n` is even and `6 ≤ n ≤ 20`
# - `Not Weird` if `n` is even and `n > 20`

## Approach

- Use `% 2` to determine whether the number is odd or even.
- For odd numbers, print `Weird`.
- For even numbers, check the required ranges and print the corresponding output.

---

## Code

n = int(input().strip())
if n % 2 != 0:
        print("Weird")
else:
        if n % 2 == 0 and n>=2 and n<=5:
            print("Not Weird")
        elif n % 2 == 0 and n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")

## Complexity

# - **Time Complexity:** O(1)
# - **Space Complexity:** O(1)
- Range Checking

✅ Accepted on HackerRank
