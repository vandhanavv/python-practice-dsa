# Eg:
# n = 4
#    1
#   121
#  12321
# 1234321

n = int(input("Enter the number: "))
i = 1
while i <= n:
    spaces = 1
    while spaces <= (n - i):
        print(" ", end=' ')
        spaces = spaces + 1
    j = 1
    p = 1
    while j <= i:
        print(p, end=' ')
        p = p + 1
        j = j + 1
    p = i - 1
    while p >= 1:
        print(p, end=' ')
        p = p - 1

    i = i + 1
    print()  

# Output:
# Enter the number: 4
#       1 
#     1 2 1 
#   1 2 3 2 1 
# 1 2 3 4 3 2 1 


# n = int(input("Enter the number: "))
# i = 1
# while i <= n:
#     spaces = 1
#     while spaces <= (n - i):
#         print(" ", end=' ')
#         spaces = spaces + 1
#     j = 1
#     p = 1
#     while j <= i:
#         print(p, end=' ')
#         p = p + 1
#         j = j + 1
#     p = 1
#     val = i - 1
#     while p <= i - 1:
#         print(val, end=' ')
#         p = p + 1
#         val = val - 1

#     i = i + 1
#     print()   
