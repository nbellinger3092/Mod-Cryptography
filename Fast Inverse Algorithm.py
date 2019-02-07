##Fast Inverse Algorithm##
##Nick Bellinger
##Mod Cryptography
##2/7/19

#Declare variables
finalNum = 1
newInt = []

#Read in integer a and power p from user
a = input("Please enter integer to be raised to a power: ")
p = input("Please enter power to raise " + a + " to: ")
N = input("Please enter mod ""N"" value: ")

#Convert string to decimal
a = int(a)
p = int(p)
N = int(N)

#Reduce p by 2
p = p - 2

#Convert power to binary
bin_p = bin(p)[2:]

#Reverse String
rev_p = bin_p[::-1]

#Split reversed binary representation into a list
lst_p = list(rev_p)

#Iterate over reversed list to create values to be multiplied and append to newInt list
for x in range(len(lst_p)):
    if int(lst_p[x]) == 1:
        newInt.append((pow(a,pow(2,x)))%N)

#Multiply values of newInt list mod N and store in finalNum
for x in range(len(newInt)):
    finalNum = (finalNum * newInt[x])%N

#Print answer mod N
print("The answer is: " + str(finalNum) + " mod " + str(N))
