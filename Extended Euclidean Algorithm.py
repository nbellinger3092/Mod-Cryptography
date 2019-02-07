##Extended Euclidean Algorithm##
##Nick Bellinger
##Mod Cryptography
##2/7/19

#Ask for input for a and b
a = input("Please enter ""a"" for gcd calculation: ")
b = input("Please enter ""b"" for gcd calculation: ")

#Convert a and b to integers
a = int(a)
b = int(b)

#Declare variables
u = 1
x = 0
g = a
y = b

#Extended Euclidean Recursive Function
def exGCD(u,g,x,y):
    #Terminal case
    if y == 0:
        v = (g-a*u)/b
        return(g,u,v)

    t = g%y
    q = (g-t)/y

    s = u - q*x
    u = x
    g = y
    x = s
    y = t
    #Recursive statement
    return exGCD(u,g,x,y)

#Print answer for GCD, u and v values
print("GCD,u,v: " + str(exGCD(u,g,x,y)))
