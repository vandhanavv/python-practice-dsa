# Reverse a number. If the number has trailing zeroes, it shouldn't be reflected in the reverse of the number.
# Eg: 40100 should be 104 and not 00104

# 421
def rev(n):
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev
n = int(input("Enter a number: "))
print(rev(n))

# Output:
# Enter a number: 10400
# 401
