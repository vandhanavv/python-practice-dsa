# Eg:
# n = 4
#    1
#   232 i = 2, p = 2
#  34543 i = 3, p = 4
# 4567654 i = 4, p = 6

n = int(input("Enter the number: "))
i = 1
while i <= n:
    spaces = 1
    while spaces <= (n - i):
        print(" ", end=' ')
        spaces = spaces + 1
    j = 1
    p = i
    while j <= i:
        print(p, end=' ')
        p = p + 1
        j = j + 1
    p = 2 * (i - 1)
    while p >= i:
        print(p, end=' ')
        p = p - 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5