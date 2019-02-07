##Shift Cipher Program by Nick Bellinger##
#Mod Cryptography
#1/29/19

import sys

#List definitions
encoding = []
encryption = []
decoding = []
decryption = []
cipherText = []

#Display title
print("Shift Cipher Program")


#Ask for input of shift number and message to be encrypted
shift = int(input("Please enter a shift number: "))
message = input("Please enter message to be encoded: ").lower()

#Use ASCII values to determine if a char or not
#Continue if char, stop program and display error if not
for x in message:
    if (int(ord(x)) >= 97 and int(ord(x)) <= 122):
        break
    else:
        print("Invalid Input, please enter valid string a-z.")
        sys.exit()

#Split message and add to a list   
splitMessage = list(message)

#Char to int conversion - appended to encoding list
print("Message: " + str(splitMessage))
for x in splitMessage:
        
    if (x == 'a'):
        encoding.append(0)
    elif (x == 'b'):
        encoding.append(1)
    elif (x == 'c'):
        encoding.append(2)
    elif (x == 'd'):
        encoding.append(3)
    elif (x == 'e'):
        encoding.append(4)
    elif (x == 'f'):
        encoding.append(5)
    elif (x == 'g'):
        encoding.append(6)
    elif (x == 'h'):
        encoding.append(7)
    elif (x == 'i'):
        encoding.append(8)
    elif (x == 'j'):
        encoding.append(9)
    elif (x == 'k'):
        encoding.append(10)
    elif (x == 'l'):
        encoding.append(11)
    elif (x == 'm'):
        encoding.append(12)
    elif (x == 'n'):
        encoding.append(13)
    elif (x == 'o'):
        encoding.append(14)
    elif (x == 'p'):
        encoding.append(15)
    elif (x == 'q'):
        encoding.append(16)
    elif (x == 'r'):
        encoding.append(17)
    elif (x == 's'):
        encoding.append(18)
    elif (x == 't'):
        encoding.append(19)
    elif (x == 'u'):
        encoding.append(20)
    elif (x == 'v'):
        encoding.append(21)
    elif (x == 'w'):
        encoding.append(22)
    elif (x == 'x'):
        encoding.append(23)
    elif (x == 'y'):
        encoding.append(24)
    elif (x == 'z'):
        encoding.append(25)
    else:
        encoding.append(x)

print("Encoded Values: " + str(encoding))

#Add shift to message and add to encryption list
for x in encoding:

    encryption.append((x + shift) % 26)

print("Shifted Values: " + str(encryption))

#Int to char conversion - append to cipherText list
for x in encryption:

    if (x == 0):
        cipherText.append('a')
    elif (x == 1):
        cipherText.append('b')
    elif (x == 2):
        cipherText.append('c')
    elif (x == 3):
        cipherText.append('d')
    elif (x == 4):
        cipherText.append('e')
    elif (x == 5):
        cipherText.append('f')
    elif (x == 6):
        cipherText.append('g')
    elif (x == 7):
        cipherText.append('h')
    elif (x == 8):
        cipherText.append('i')
    elif (x == 9):
        cipherText.append('j')
    elif (x == 10):
        cipherText.append('k')
    elif (x == 11):
        cipherText.append('l')
    elif (x == 12):
        cipherText.append('m')
    elif (x == 13):
        cipherText.append('n')
    elif (x == 14):
        cipherText.append('o')
    elif (x == 15):
        cipherText.append('p')
    elif (x == 16):
        cipherText.append('q')
    elif (x == 17):
        cipherText.append('r')
    elif (x == 18):
        cipherText.append('s')
    elif (x == 19):
        cipherText.append('t')
    elif (x == 20):
        cipherText.append('u')
    elif (x == 21):
        cipherText.append('v')
    elif (x == 22):
        cipherText.append('w')
    elif (x == 23):
        cipherText.append('x')
    elif (x == 24):
        cipherText.append('y')
    elif (x == 25):
        cipherText.append('z')
    else:
        decryption.append(x)

print("Cipher Text: " + str(cipherText))

#Reversal of shift to decode message
for x in encryption:

    decoding.append((x - shift) % 26)

print("Decoded Values: " + str(decoding))

#Int to char conversion - append to decryption list
for x in decoding:

    if (x == 0):
        decryption.append('a')
    elif (x == 1):
        decryption.append('b')
    elif (x == 2):
        decryption.append('c')
    elif (x == 3):
        decryption.append('d')
    elif (x == 4):
        decryption.append('e')
    elif (x == 5):
        decryption.append('f')
    elif (x == 6):
        decryption.append('g')
    elif (x == 7):
        decryption.append('h')
    elif (x == 8):
        decryption.append('i')
    elif (x == 9):
        decryption.append('j')
    elif (x == 10):
        decryption.append('k')
    elif (x == 11):
        decryption.append('l')
    elif (x == 12):
        decryption.append('m')
    elif (x == 13):
        decryption.append('n')
    elif (x == 14):
        decryption.append('o')
    elif (x == 15):
        decryption.append('p')
    elif (x == 16):
        decryption.append('q')
    elif (x == 17):
        decryption.append('r')
    elif (x == 18):
        decryption.append('s')
    elif (x == 19):
        decryption.append('t')
    elif (x == 20):
        decryption.append('u')
    elif (x == 21):
        decryption.append('v')
    elif (x == 22):
        decryption.append('w')
    elif (x == 23):
        decryption.append('x')
    elif (x == 24):
        decryption.append('y')
    elif (x == 25):
        decryption.append('z')
    else:
        decryption.append(x)
        
print("Decrypted Message: " + str(decryption))
