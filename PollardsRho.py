## Pollard's Rho Method
## Nick Bellinger
## Mod Cryptography
## 5/2/19

import FastInverseAlgorithm as FI

# Solve g^t = h mod p

ax = 0
bx = 0
ay = 0
by = 0

x = 1
y = 1

g = 19
h = 24717
p = 48611

#####   Mixer Function  ######################
def mixer(s,g,h,p,a,b):
    
    if s < (p/3):
        s = (g * s) % p
        a = (a + 1) % (p-1)
        return s,a,b
    elif s > (p/3) and s < ((2*p)/3):
        s = (s*s) % p
        a = (2*a) % (p-1)
        b = (2*b) % (p-1)
        return s,a,b
    elif s > ((2*p)/3) and s < p:
        s = (h * s) % p
        b = (b + 1) % (p-1)
        return s,a,b
############################################

#####   GCD FUNCTION    ####################
def exGCD(u,g,x,y,a,b):
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
    return exGCD(u,g,x,y,a,b)
###########################################

# Run mixer function until x == y
while True:
    x,ax,bx = mixer(x,g,h,p,ax,bx)
    y,ay,by = mixer(y,g,h,p,ay,by)
    y,ay,by = mixer(y,g,h,p,ay,by)

    if x == y:
        print("x: " + str(x))
        print("y: " + str(g))
        print("ax: " + str(ax))
        print("bx: " + str(bx))
        print("ay: " + str(ay))
        print("by: " + str(by))
        break


# Set u and v to the difference of exponents for x and y components
u = (ax-ay) % (p-1)
v = (by-bx) % (p-1)

# Use GCD function to find d and s
a = v
b = (p-1)
d,s,i = exGCD(1,v,0,(p-1),a,b)

# Calulate w = s*v
w = (s * u) % (p-1)

# Set variable k as a counter for while loop
k = 1
while k < (d-1):
    print("k: " + str(k))
    # t is the exponent we want to find
    # This will continue to iterate k until the exponent is found
    t = (w/d) + k*((p-1)/d)
    t = int(t)
    print("T: " + str(t))
    # If g^t == h % p, the loop will break, and it will print the found t
    if pow(g,t,p) == h % p:
        print("t is: " + str(t))
        break
    else:
        print("t not found")
        k = k + 1

# Calculate g^t and h % p and compare them, print TRUE if equal, and FALSE if not
g_t = pow(g,t,p) % p
print("g^t: " + str(g_t))
h_p = h % p
print("h % p: " + str(h_p))

if g_t == h_p:
    print("TRUE")
else:
    print("FALSE")