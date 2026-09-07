# Eg:
# n = 4
# 1234
# 123
# 12
# 1

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= (n - i + 1):
        print(j, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1

