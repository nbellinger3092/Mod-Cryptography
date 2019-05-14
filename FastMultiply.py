## Fast Multiple Algorithm
## Nick Bellinger
## Mod Cryptography
## 3/28/19

# Takes in p, n, P and returns nP
import time
import EllipticAdd

newNum = []

start = time.time()

n = 1000000
p = 1386493

A = 3

# P
x1 = 1
y1 = 1

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
        if x == 0:
            temp1, temp2 = x1,y1
        else:
            temp1, temp2 = EllipticAdd.EllipticAdd(temp1, temp2, temp1, temp2, A, p)
 
        if int(lst_n[x]) == 1:
            x3,y3 = EllipticAdd.EllipticAdd(temp1, temp2, x3, y3, A, p)
    return x3,y3

#Uncomment this line when running solo.  Comment when importing to another program
x3,y3 = FastMultiple(n,x1,y1,p,A)

end = time.time()
print("Runtime: " + str(end-start))