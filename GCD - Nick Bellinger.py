##GCD Algorithm##
#Nick Bellinger
#Mod Cryptography
#2/7/19

#Ask for input for a and b
a = input("Enter first number: ")
b = input("Enter second number: ")

#Convert a and b to integers
a = int(a)
b = int(b)

#GCD function
def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b,a%b)

#Print answer for GCD to a and b
print("GCD: " + str(GCD(a,b)))
