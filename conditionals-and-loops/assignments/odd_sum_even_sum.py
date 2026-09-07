n = int(input("Enter the number: "))
evenSum = 0
oddSum = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        evenSum = evenSum + digit
    else:
        oddSum = oddSum + digit
    n = n // 10

print("Even sum:", evenSum)
print("Odd sum:", oddSum)

# Output:
# Enter the number: 421
# Even sum: 6
# Odd sum: 1