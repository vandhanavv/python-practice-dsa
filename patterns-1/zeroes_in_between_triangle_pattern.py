# Eg:
# n = 4
# 1
# 11
# 202
# 3003

n = int(input("Enter the number: "))
print('1')
i = 1
while i <= n - 1:
    j = 1
    while j <= i + 1:
        if j == 1 or j == i + 1:
            print(i, end=' ')
        else:
            print('0', end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# 1
# 1 1 
# 2 0 2 
# 3 0 0 3 
# 4 0 0 0 4 