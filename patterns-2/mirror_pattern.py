# Eg:
# n = 5
# 1       1
# 12     21
# 123   321  
# 1234 4321
# 123454321

n = int(input("Enter the number: "))
i = 1
totalspace = n * 2 - 2
while i <= n:
    j = 1
    while j <= i:
        print(j, end=' ')
        j = j + 1
    spaces = 1
    while spaces <= totalspace:
        print(" ", end=' ')
        spaces = spaces + 1
    totalspace = totalspace - 2
    j = i
    while j > 0:
        print(j, end=' ')
        j = j - 1
    i = i + 1
    print()

# Output:
# Enter the number: 4
# 1             1 
# 1 2         2 1 
# 1 2 3     3 2 1 
# 1 2 3 4 4 3 2 1 