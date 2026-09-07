# Eg:
# n = 4
# 4321
# 4321
# 4321
# 4321

n = int(input("Enter the number: "))
i = 1 
while i <= n:
    j = 1
    while j <= n:
        print(n - j + 1, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 