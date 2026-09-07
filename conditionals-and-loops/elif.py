a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a >= b and a >= c:
    print("Greatest number:", a) 
elif b >= a and b >= c:
    print("Greatest number:", b)
else:
    print("Greatest number:", c)

# Output:
# Enter a number: 5
# Enter a number: 4
# Enter a number: 3
# 5