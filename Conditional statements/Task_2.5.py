
a = input("Enter first side length: ")
b = input("Enter second side length: ")
c = input("Enter third side length: ")

if int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(c) + int(b) > int(a):
    print("exist")
else:
    print("not exist")
