# Eg:
# Input:
# n = 4
# Output:
# 1
# 12
# 123
# 1234

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 6
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6