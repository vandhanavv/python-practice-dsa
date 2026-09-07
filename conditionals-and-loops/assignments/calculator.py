# Calculator program

bool = True
while bool:
    n = int(input("Enter the operation to be performed: "))
    if n == 1:
        a1 = int(input("Enter a number: "))
        a2= int(input("Enter a number: "))
        print(a1 + a2)
    elif n == 2:
        a1 = int(input("Enter a number: "))
        a2= int(input("Enter a number: "))
        print(a1 - a2)
    elif n == 3:
        a1 = int(input("Enter a number: "))
        a2= int(input("Enter a number: "))
        print(a1 * a2)
    elif n == 4:
        a1 = int(input("Enter a number: "))
        a2= int(input("Enter a number: "))
        print(a1 // a2)
    elif n == 5:
        a1 = int(input("Enter a number: "))
        a2= int(input("Enter a number: "))
        print(a1 % a2)
    elif n == 6:
        bool = False
        exit()
    else: 
        print("Invalid Operation")
    
