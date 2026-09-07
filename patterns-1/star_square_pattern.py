# Print (*) square pattern
# Eg:
# n = 4
# ****
# ****
# ****
# ****
# i -> number of rows
# j -> number of columns

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print("*", end=' ') # end -> spaces in between stars
        j = j + 1
    print()
    i = i + 1


