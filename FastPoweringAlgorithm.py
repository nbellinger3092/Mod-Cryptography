## Fast Powering Algorithm##
## Nick Bellinger
## Mod Cryptography
## 2/7/19

def FastPower(g,M,N):

        # Declare variables
        finalNum = 1
        newInt = []

        # Read in integer g and power M from user
        #g = input("Please enter integer to be raised to a power: ")
        #M = input("Please enter power to raise " + g + " to: ")
        #N = input("Please enter mod ""N"" value: ")

        # Convert string to decimal
        g = int(g)
        M = int(M)
        N = int(N)

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
                        newInt.append((pow(g,pow(2,x)))%N)

        # Multiply values of newInt list mod N and store in finalNum
        for x in range(len(newInt)):
                finalNum = (finalNum * newInt[x])%N

        # Print answer mod N
        # print("The answer is: " + str(finalNum) + " mod " + str(N))
        return finalNum
