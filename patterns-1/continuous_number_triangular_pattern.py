# Eg:
# n = 4
# 1
# 23
# 456
# 78910

n = int(input("Enter the number: "))
i = 1
p = 1
while i <= n:
    j = 1 
    while j <= i:
        print(p, end=' ')
        j = j + 1
        p = p + 1
    print()
    i = i + 1

# Output:
# Enter the number: 4
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10