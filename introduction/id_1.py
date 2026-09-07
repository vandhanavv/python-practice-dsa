# Find id of the variable. ID is the memory address of the variable and changes each time 
# you run the program (except for some python versions which has constant ID for numbers 
# between -5 to 256)


a = 10
print(id(a))
a = a + 1
print(id(a))

# Output:
# 4344201744
# 4344201776
