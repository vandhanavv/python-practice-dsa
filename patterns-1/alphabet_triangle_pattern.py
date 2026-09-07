# Eg:
# n = 4
# A
# BC
# CDEF
# DEFG

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        start_char = chr(ord('A') + i - 1)
        next_char = chr(ord(start_char) + j - 1)
        print(next_char, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 4
# A 
# B C 
# C D E 
# D E F G 