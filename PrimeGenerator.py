#Prime Generator Function

import FastPoweringAlgorithm

p = input("Enter Group: ")

p = int(p)
for x in range(p):
    print(str(x))
    print("##################################################")
    for y in range(p-1):
        print(str(FastPoweringAlgorithm.FastPower(x,y,p)))
    print("##################################################")

