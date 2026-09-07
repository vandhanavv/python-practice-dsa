# Eg:
# n = 5
# E
# DE
# CDE
# BCDE
# ABCDE

n = int(input("Enter the number: "))
i = 1
start_char = chr(ord('A') + n - 1) # instead of this you can use start_char = chr(ord('A') + n - i) and remove line 15 (start_row_char = chr(ord(start_char) - i + 1))
while i <= n:
    j = 1
    while j <= i:
        start_row_char = chr(ord(start_char) - i + 1)
        char = chr(ord(start_row_char) + j - 1)
        print(char, end=' ')
        j = j + 1
    print()
    i = i + 1