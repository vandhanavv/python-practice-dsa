# Eg:
# 4444
# 333
# 22
# 1

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= (n - i + 1):
        print((n - i + 1), end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 