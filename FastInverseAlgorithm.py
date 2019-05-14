##Fast Inverse Algorithm##
##Nick Bellinger
##Mod Cryptography
##2/7/19

import FasterPower as FP
import time

# a = input("Please enter base number 'a': ")
# p = input("Please enter field 'p': " )
x = 0
start = time.time()
def FastInverse(a,p):
        

        #Read in integer a and power p from user
        #a = input("Please Enter 'a': ")
        #p = input("Please enter 'p': ")

        #Declare variables
        finalNum = 1
        newInt = []

        #Convert string to decimal
        a = int(a)
        p = int(p)

        #Convert power to binary
        bin_p = bin(p-2)[2:]

        #Reverse String
        rev_p = bin_p[::-1]

        #Split reversed binary representation into a list
        lst_p = list(rev_p)

        #Iterate over reversed list to create values to be multiplied and append to newInt list
        for x in range(len(lst_p)):
                if int(lst_p[x]) == 1:
                        #newInt.append((pow(a,pow(2,x)))%p) # This works too
                        newInt.append(FP.pow_mod(a,FP.pow_mod(2,x,p),p)%p)

        #Multiply values of newInt list mod N and store in finalNum
        for x in range(len(newInt)):
                finalNum = (finalNum * newInt[x])%p

        #Print answer mod N - debug line
        #print("The answer is: " + str(finalNum))
        return finalNum%p

#Uncomment these lines when running solo.  Comment when importing to another program
# x = FastInverse(a,p)
# print("Inverse: " + str(x))
# end = time.time()
# print("Fast Inverse Runtime: " + str(end-start))