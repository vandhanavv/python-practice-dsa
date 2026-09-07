# Eg:
# Input: 4
# Output:
# 1
# 23
# 345
# 4567

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1 
    p = i
    while j <= i:
        print(p, end=' ')
        j = j + 1
        p = p + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# 1 
# 2 3 
# 3 4 5 
# 4 5 6 7 
# 5 6 7 8 9 

