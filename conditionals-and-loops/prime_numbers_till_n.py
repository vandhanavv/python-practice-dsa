# Print prime numbers till N
# n = int(input("Enter the number: "))
# k = 2
# while k <= n:
#     d = 2
#     flag = False
#     while d < k:
#         if k % d == 0:
#             flag = True
#             break
#         d = d + 1
#     if not(flag):
#         print(k)
#     k = k + 1

n = int(input("Enter the number: "))
k = 2
while k <= n:
    d = 2
    while d < k:
        if k % d == 0:
            break
        d = d + 1
    else:
        print(k)
    k = k + 1