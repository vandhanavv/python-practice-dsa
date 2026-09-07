def fibonacci(n):
    a = 0 
    b = 1
    if n < 0:
        print(" ")
    elif n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        i = 1
        while i < n:
            c = a + b
            a = b
            b = c
            i = i + 1
        return b

n = int(input("Enter the number: "))
print(fibonacci(n))