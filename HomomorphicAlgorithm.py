## Elgamal Homomorphic Decryption Attack Algorithm
## Nick Bellinger
## Mod Cryptography
## 2/28/19

import FastInverseAlgorithm
import FastPoweringAlgorithm

# Public Variables
p = 467
g = 2

##############################################
#   Alice and Bob - Message to be attacked   #
##############################################

# Alice's Variables
a = 153

# Bob's Variables
k1 = 197
m1 = 331

def CalculateAlice(p,g,a):
    A = FastPoweringAlgorithm.FastPower(g,a,p)%p
    #A = pow(g,a)%p
    return A
A = CalculateAlice(p,g,a)
#print("A: " + str(A))
def CalculateBob(p,g,k1,m1,A):
    C1 = FastPoweringAlgorithm.FastPower(g,k1,p)%p
    #C1 = pow(g,k1)%p
    C2 = m1*FastPoweringAlgorithm.FastPower(A,k1,p)%p
    #C2 = m1*pow(A,k1)%p
    return C1,C2


C1,C2 = CalculateBob(p,g,k1,m1,A)

##############################################
#  Eve's Message - Known message for attack  #
##############################################

# Eve's variables
k2 = 211
m2 = 199

def CalculateEve(p,g,k2,m2,A):
    D1 = pow(g,k2)%p
    D2 = m2*pow(A,k2)%p
    return D1,D2

def CalculateE1_E2(C1,C2,D1,D2):
    E1 = (C1*D1)%p
    E2 = (C2*D2)%p
    return E1,E2

D1,D2 = CalculateEve(p,g,k2,m2,A)

E1,E2 = CalculateE1_E2(C1,C2,D1,D2)

##############################################
#      Decryption Oracle "Calculation"       #
##############################################

oracle = (m1*m2)%p
# m2 inverse calculation
m2Inverse = FastInverseAlgorithm.FastInverse(m2,p)%p
# Use m2 inverse to get the original message
originalMessage = (m2Inverse*oracle)%p

print("Original Message: " + str(originalMessage))