#!/usr/bin/python3
num = list(range(0,100))

with open("primes_cm.txt","w") as fp:
    for each in num:
        for i in range(2, each- 1):
            if (each % i == 0):
                break
        else:
            fp.write("{}\t".format(str(each)))