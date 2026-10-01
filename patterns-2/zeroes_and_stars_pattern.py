# Eg:
# n = 4
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000

n = int(input("Enter the number: "))
start = 1
end = (2 * n) + 1
mid = n + 1
i = 1
while i <= n:
    j = 1
    while j <= (2 * n) + 1:
        if j == start or j == end or j == mid:
            print("*", end=' ')
        else:
            print("0", end=' ')
        j = j + 1
    start = start + 1
    end = end - 1
    i = i + 1
    print()

# Output:
# Enter the number: 5
# * 0 0 0 0 * 0 0 0 0 * 
# 0 * 0 0 0 * 0 0 0 * 0 
# 0 0 * 0 0 * 0 0 * 0 0 
# 0 0 0 * 0 * 0 * 0 0 0 
# 0 0 0 0 * * * 0 0 0 0 
