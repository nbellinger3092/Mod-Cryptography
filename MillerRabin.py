## Miller-Rabin Test
## Nick Bellinger
## Mod Cryptography
## 4/9/19

import GCD
import FastPoweringAlgorithm as FP

# Solve n - 1 = 2^k * q
a = 2
n = 37
m = n - 1
k = 0
q = 0
i = 0
r = 0


#####   MillerRabin Primality Test Function ################
def MillerRabin(a,n,m,k,q,i,r):
    if n % 2 == 0:
        return True
    else:
        if GCD.GCD(a,n) != 1:
            return True
        
        q,r = divmod(m,2)

        if a == 1 % n:
            return False
        
        for i in range(i,r-1):
            if a == -1 % n:
                return False
            a = pow(a,2,n)
            i = i + 1
        else:
            return True
###########################################################

print("Test: " + str(MillerRabin(a,n,m,k,q,i,r)))