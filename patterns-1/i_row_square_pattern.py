# Print ith row as square pattern

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 4
# 1 1 1 1 
# 2 2 2 2 
# 3 3 3 3 
# 4 4 4 4