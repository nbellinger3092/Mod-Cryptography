## Fast Powering Algorithm##
## Nick Bellinger
## Mod Cryptography
## 2/7/19

def FastPower(g,M,N):

        # Declare variables
        finalNum = 1
        newInt = []
        append = newInt.append #Makes it slightly faster to initialize this than to call it in the loop

        # Convert string to decimal
        #g = int(g)
        #M = int(M)
        #N = int(N)

        # Convert power to binary
        bin_M = bin(M)[2:]

        # Reverse String
        rev_M = bin_M[::-1]

        # Split reversed binary representation into a list
        lst_M = list(rev_M)

        # Iterate over reversed list to create values to be multiplied 
        # and append to newInt list
        for x in range(len(lst_M)):
                if int(lst_M[x]) == 1:
                        append((pow(g,pow(2,x)))%N)
                        #newInt.append((g ** (2 ** x))%N) # This works too
                        
        # Multiply values of newInt list mod N and store in finalNum
        for x in range(len(newInt)):
                finalNum = (finalNum * newInt[x])%N
        #test = map(lambda finalNum : (finalNum * newInt)%N,newInt)

        # Print answer mod N
        # print("The answer is: " + str(finalNum) + " mod " + str(N))
        return finalNum
        #return int(test)
