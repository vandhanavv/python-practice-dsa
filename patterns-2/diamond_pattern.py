# Eg:
# n = 5
#   *
#  ***
# *****
#  *** i = 2
#   *  i = 1

n = int(input("Enter the number: "))
firstHalf = (n + 1) // 2
secondHalf = n // 2
i = 1
while i <= firstHalf:
    spaces = 1
    while spaces <= (firstHalf - i):
        print(" ", end=' ')
        spaces = spaces + 1
    j = 1
    while j <= (2 * i - 1):
        print("*", end=' ')
        j = j + 1
    print()
    i = i + 1
i = secondHalf
while i >= 1:
    spaces = 1
    while spaces <= (secondHalf - i + 1):
        print(" ", end=' ')
        spaces = spaces + 1
    j = 1
    while j <= (2 * i - 1):
        print("*", end=' ')
        j = j + 1
    print()
    i -= 1

# Output:
# Enter the number: 5
#     * 
#   * * * 
# * * * * * 
#   * * * 
#     * 

 