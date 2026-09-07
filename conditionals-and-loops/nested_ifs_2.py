n = int(input("Enter the number: "))
m = int(input("Enter the number: "))
if n % 2 == 0:
    if m % 2 == 0:
        print(1)
    else:
        print(2)
else:
    print(3)

# Output:
# 1. Enter the number: 8
#    Enter the number: 10
#    1

# 2. Enter the number: 5
#    Enter the number: 8
#    3

# 3. Enter the number: 4
#    Enter the number: 9 
#    2