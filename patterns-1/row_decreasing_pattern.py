# Eg:
# n = 4
# 1
# 21
# 321
# 4321

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    p = i
    while j <= i:
        print(p, end=' ')
        j = j + 1
        p = p - 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1



