# Print 'n' number as square pattern

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(n, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output: 
# Enter the number: 6
# 6 6 6 6 6 6 
# 6 6 6 6 6 6 
# 6 6 6 6 6 6 
# 6 6 6 6 6 6 
# 6 6 6 6 6 6 
# 6 6 6 6 6 6