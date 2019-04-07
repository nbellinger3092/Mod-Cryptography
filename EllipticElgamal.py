## Elliptic Encrypt Algorithm
## Nick Bellinger
## Mod Cryptography
## 4/6/19

import time
import FastInverseAlgorithm# as FI
import FastMultiply# as FM

p = 3623

x1 = 6   # Point on E
y1 = 730 #

A = 14

na = 947

#################################
#             Alice             #
#################################

# Calculates
Qa = FastMultiply.FastMultiple(na,x1,y1,p,A)

# Publishes Qa1,Qa2,p,E

#################################
#               BOB             #
#################################
# Picks message m1, m2
m1 = 25
m2 = 1000
# Picks random k
k = 1033

# Calculates
R = FastMultiply.FastMultiple(k,x1,y1,p,A)

S = FastMultiply.FastMultiple(k,Qa[0],Qa[1],p,A)

c1 = (S[0] * m1) % p
c2 = (S[1] * m2) % p

# Sends c1,c2,R to Alice

#################################
#             Alice             #
#################################

# Calculates 

T = FastMultiply.FastMultiple(na,R[0],R[1],p,A)

m1 = (FastInverseAlgorithm.FastInverse(T[0],p) * c1) % p
m2 = (FastInverseAlgorithm.FastInverse(T[1],p) * c2) % p

print("m1: " + str(m1))
print("m2: " + str(m2))