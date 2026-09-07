# Print jth column number as square pattern

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(j, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 4
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 