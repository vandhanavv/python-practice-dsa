# Method 1:
# n = int(input("Enter the number: ")) # 10
# d = 2
# flag = False
# while d < n:
#     if n % d == 0:
#         flag = True                 # break can also be used along with the flag variable to break out of the loop once it satisfies the condition of being prime
#     d = d + 1

# if flag:
#     print("n is not prime")
# else:
#     print("n is prime")

# Method 2: 
n = int(input("Enter the number: ")) # 10
d = 2
while d < n:
    if n % d == 0:
        print("n is not prime")
        break
    d = d + 1
else: 
    print("n is prime")
