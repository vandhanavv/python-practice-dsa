# Eg:
# ****
# ***
# **
# *

n = int(input("Enter the number: "))
i = 1 
while i <= n:
    j = 1
    while j <= n - i + 1:
        print("*", end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 