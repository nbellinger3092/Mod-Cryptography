## Elgamal Decryption Algorithm
## Nick Bellinger
## Mod Cryptography
## 2/25/19

# Declare variables
# Test variables
p = 467
g = 2
a = 153

C1 = 87
C2 = 57

# Fast Power function w/ no mod function when calcuating powers
def FastPowerNoMod(g,M):
    
    # Declare variables
    finalNum = 1
    newInt = []

    # Convert string to decimal
    g = int(g)
    M = int(M)

    # Convert power to binary
    bin_M = bin(M)[2:]

    # Reverse String
    rev_M = bin_M[::-1]

    # Split reversed binary representation into a list
    lst_M = list(rev_M)

    # Iterate over reversed list to create values to be multiplied and append to newInt list
    for x in range(len(lst_M)):
        if int(lst_M[x]) == 1:
            newInt.append((pow(g,pow(2,x))))

    # Multiply values of newInt list mod N and store in finalNum
    for x in range(len(newInt)):
        finalNum = (finalNum * newInt[x])
    
    return finalNum

# Fast Inverse Function
def FastInverse(a,p):
    # Declare variables
    finalNum = 1
    newInt = []

    # Convert string to decimal
    a = int(a)
    p = int(p)

    # Convert power to binary
    bin_p = bin(p-2)[2:]

    # Reverse String
    rev_p = bin_p[::-1]

    # Split reversed binary representation into a list
    lst_p = list(rev_p)

    # Iterate over reversed list to create values to be multiplied and append to newInt list
    for x in range(len(lst_p)):
        if int(lst_p[x]) == 1:
            newInt.append((pow(a,pow(2,x)))%p)

    # Multiply values of newInt list mod N and store in finalNum
    for x in range(len(newInt)):
        finalNum = (finalNum * newInt[x])%p
    
    return finalNum

# Calculate C1^a
C1a = FastPowerNoMod(C1,a)
# Calcualte (C1^a)^-1
C1aInverse = FastInverse(C1a,p)
# Calculate (g^(ak))^-1
gakInverse = (C1aInverse * C2)%p
m = gakInverse
# Print result
print("m: " + str(m))
