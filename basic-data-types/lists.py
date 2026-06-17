# Lists

# Task:
# Create an empty list and execute N commands.

# Commands:
# - insert i e
# - print
# - remove e
# - append e
# - sort
# - pop
# - reverse


# Important Notes

# input().split()
# - Splits input into separate words.

# insert(i, e)
# - Inserts e at index i.

# append(e)
# - Adds e to the end.

# remove(e)
# - Removes first occurrence of e.

# sort()
# - Sorts list in ascending order.

# pop()
# - Removes last element.

# reverse()
# - Reverses the list.

# for _ in range(N)
# - Repeat N times without using the loop variable.


#code
if __name__ == '__main__':
    N = int(input())

    lst = []

    for _ in range(N):
        command = input().split()

        if command[0] == 'insert':
            lst.insert(int(command[1]), int(command[2]))

        elif command[0] == 'print':
            print(lst)

        elif command[0] == 'remove':
            lst.remove(int(command[1]))

        elif command[0] == 'append':
            lst.append(int(command[1]))

        elif command[0] == 'sort':
            lst.sort()

        elif command[0] == 'pop':
            lst.pop()

        elif command[0] == 'reverse':
            lst.reverse()
