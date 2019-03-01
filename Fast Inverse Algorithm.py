##Fast Inverse Algorithm##
##Nick Bellinger
##Mod Cryptography
##2/7/19

#Declare variables
finalNum = 1
newInt = []

#Read in integer a and power p from user
a = input("Please Enter 'a': ")
p = input("Please enter 'p': ")

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
        newInt.append((pow(a,pow(2,x)))%p)

#Multiply values of newInt list mod N and store in finalNum
for x in range(len(newInt)):
    finalNum = (finalNum * newInt[x])%p

#Print answer mod N
print("The answer is: " + str(finalNum))
