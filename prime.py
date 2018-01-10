#!/usr/bin/python3
num = list(range(0,100))

fp = open("primes.txt","w")

for each in num:
    for i in range(2,each-1):
        if (each%i == 0):
            flag=1
            break

    else:
        fp.write("{}\t".format(str(each)))

fp.close()