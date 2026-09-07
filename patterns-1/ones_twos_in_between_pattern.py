n = int(input("Enter the number: "))
i = 1
print(1)
while i <= n - 1:
    j = 1
    while j <= i + 1:
        if j == 1 or j == i + 1:
            print(1, end=' ')
        else:
            print(2, end= ' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# 1
# 1 1 
# 1 2 1 
# 1 2 2 1 
# 1 2 2 2 1 