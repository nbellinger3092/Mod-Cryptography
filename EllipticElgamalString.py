## Elliptic Encrypt Algorithm
## Nick Bellinger
## Mod Cryptography
## 5/11/19

import time
import FastInverseAlgorithm as FI
import FastMultiply# as FM
import time

p = 200000081

x1 = 6   # Point on E
y1 = 730 #

A = 14

na = 947
start = time.time()
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

message1 = "A+C"
message2 = "B&D"
encodedMessage1 = ""
encodedMessage2 = ""

for i in range(len(message1)):
    encodedMessage1 = encodedMessage1 + str(ord(message1[i]))

for i in range(len(message2)):
    encodedMessage2 = encodedMessage2 + str(ord(message2[i]))

m1 = int(encodedMessage1)
m2 = int(encodedMessage2)

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

m1 = (FI.FastInverse(T[0],p) * c1) % p
m2 = (FI.FastInverse(T[1],p) * c2) % p

str_m1 = str(m1)
str_m2 = str(m2)

encodedMessage1 = ""
encodedMessage2 = ""

m1 = ""
m2 = ""

for text in (str_m1[i:i+2] for i in range(0, len(str_m1), 2)):
    text = int(text)
    text = chr(text)
    m1 = m1 + text
    
for text in (str_m2[i:i+2] for i in range(0, len(str_m2), 2)):
    text = int(text)
    text = chr(text)
    m2 = m2 + text

print("m1: " + str(m1))
print("m2: " + str(m2))

