# Eg:
# ABCD
# BCDE
# CDEF
# DEFG

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        start_char = chr(ord('A') + i - 1)
        char = chr(ord(start_char) + j - 1)
        print(char, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 4
# A B C D 
# B C D E 
# C D E F 
# D E F G