# Eg:
# A
# BB
# CCC

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        char = chr(ord('A') + i - 1)
        print(char, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
