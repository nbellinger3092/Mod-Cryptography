## Fast Multiple Algorithm
## Nick Bellinger
## Mod Cryptography
## 3/28/19

# Takes in p, n, P and returns nP

import FastInverseAlgorithm
import FastPoweringAlgorithm
import EllipticAdd

newNum = []

n = 1000000
p = 1386493

A = 3

# P
x1 = 1
y1 = 1

#def EllipticAdd(x1,y1,x2,y2,A,p):
#    m = ((3 * (pow(x1,2)) + A) * pow((2 * y1),p-2,p)) % p
#    x3 = ((pow(m,2)) - x1 - x2) % p
#    y3 = (m * (x1 - x3) - y1) % p
#    print("R = (" + str(x3) + "," + str(y3) + ")")
#    return x3,y3

def FastMultiple(n,x1,y1,p,A):
    nP = 0
    # Convert p to binary
    bin_n = bin(n)[2:]
    # Reverse the binary string
    rev_n = bin_n[::-1]

    # Split reversed binary representation into a list
    lst_n = list(rev_n)
    
    x3, y3 = ('O','O')
    
    for x in range(len(lst_n)):
        if x ==0:
            temp1, temp2 = x1,y1
        else:
            temp1, temp2 = EllipticAdd.EllipticAdd(temp1, temp2, temp1, temp2, A, p)
 
        if int(lst_n[x]) == 1:
            x3,y3 = EllipticAdd.EllipticAdd(temp1, temp2, x3, y3, A, p)
    return x3,y3
#print(n,p, x1, y1)
x3,y3 = FastMultiple(n,x1,y1,p,A)
#print("Final: "+ str(x3) + "," + str(y3))
#print("nP = " + str(nP))
