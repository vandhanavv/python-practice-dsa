n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(1, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# 1 
# 1 1 
# 1 1 1 
# 1 1 1 1 
# 1 1 1 1 1 