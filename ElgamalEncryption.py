## Elgamal Encryption Algorithm
## Nick Bellinger
## Mod Cryptography
## 2/25/19

# Declare variables
#Test variables
p = 467
g = 2
A = 224
#a = 153
k = 197
m = 331

# Fast Powering Algorithm
def FastPower(g,M,N):
    
    #Declare variables
    finalNum = 1
    newInt = []

    #Convert string to decimal
    g = int(g)
    M = int(M)
    N = int(N)

    #Convert power to binary
    bin_M = bin(M)[2:]

    #Reverse String
    rev_M = bin_M[::-1]

    #Split reversed binary representation into a list
    lst_M = list(rev_M)

    #Iterate over reversed list to create values to be multiplied and append to newInt list
    for x in range(len(lst_M)):
        if int(lst_M[x]) == 1:
            newInt.append((pow(g,pow(2,x)))%N)

    #Multiply values of newInt list mod N and store in finalNum
    for x in range(len(newInt)):
        finalNum = (finalNum * newInt[x])%N
    
    return finalNum

def FastPowerNoMod(g,M):
    
    #Declare variables
    finalNum = 1
    newInt = []

    #Convert string to decimal
    g = int(g)
    M = int(M)

    #Convert power to binary
    bin_M = bin(M)[2:]

    #Reverse String
    rev_M = bin_M[::-1]

    #Split reversed binary representation into a list
    lst_M = list(rev_M)

    #Iterate over reversed list to create values to be multiplied and append to newInt list
    for x in range(len(lst_M)):
        if int(lst_M[x]) == 1:
            newInt.append((pow(g,pow(2,x))))

    #Multiply values of newInt list mod N and store in finalNum
    for x in range(len(newInt)):
        finalNum = (finalNum * newInt[x])
    
    return finalNum

#A = FastPower(g,a,p)

C1 = FastPower(g,k,p)

Ak = FastPowerNoMod(A,k)

C2 = (m*Ak)%p

print("$(" + str(C1) + "," + str(C2) + ")$")
