# Eg:
# ABCD
# ABCD
# ABCD
# ABCD

n = int(input("Enter the number: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        char = chr(ord('A') + j - 1)
        print(char, end=' ')
        j = j + 1
    print()
    i = i + 1

# Output:
# Enter the number: 5
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E