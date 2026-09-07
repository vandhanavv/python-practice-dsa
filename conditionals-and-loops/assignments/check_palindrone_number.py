# To check if a number is palindrome or not

def check_palindrome(n):
    rev = 0
    num = n 
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    if rev == n:     # don't use num here since num is reduced to 0 after while loop runs
        return True
    else:
        return False

n = int(input("Enter the number: "))
output = check_palindrome(n)
if output:
    print("True")
else: 
    print("False")

# Output:
# 1. Enter the number: 424
#    True

# 2. Enter the number: 35348576438
#    False

