## Elliptic Curve Digital Signature Algorithm
## Nick Bellinger
## Mod Cryptography
## 4/7/19

import FastMultiply as FM
import FastInverseAlgorithm as FI
import EllipticAdd as EA
import random
from datetime import datetime

# G element of large prime order q
P = [1,5]
q = 9
A = 3
p = 13

# Key creation
s = 947

V = FM.FastMultiple(s,P[0],P[1],p,A)
print("V: " + str(V))

# Signing

d = 12345 % q # Document #


random.seed(datetime.now())
e = 11#(random.randint(1,q)) % q  # Random element #
print("e: " + str(e))
# Compute eG in E(Fp)

eP = FM.FastMultiple(e,P[0],P[1],p,A)
print("eP: " + str(eP))
S1 = eP[0] % q
S2 = ((d + (s * eP[0])) * FI.FastInverse(e,p)) % q

d_sig = S1,S2

print("S1: " + str(S1))
print("S2: " + str(S2))
print("d_sig: " + str(d_sig))

# Verification

V1 = (d * FI.FastInverse(S2,p)) % q
V2 = (eP[0] * FI.FastInverse(S2,p)) % q
print("V1: " + str(V1))
print("V2: " + str(V2))

x1,y1 = FM.FastMultiple(V1,P[0],P[1],p,A)
print("x1: " + str(x1) + ", " + "y1: " + str(y1))
x2,y2 = FM.FastMultiple(V2,V[0],V[1],p,A)
print("x2: " + str(x2) + ", " + "y2: " + str(y2))
temp = (EA.EllipticAdd(x1,y1,x2,y2,A,p))
print("temp: " + str(temp))
verification = temp[0]

print("verification: " + str(verification))

if (int(S1) == int(verification)):
    print("Verification Successful!")
else:
    print("Verification Failed")
