import os
import sys
import math
import time
def LGC(a=1103515245, m=2**32, c=12345, no_sample=1, x0=0.1, repeat = True):
    """
    A function to generate Pseudo Random Number based LCG Algorithm

    args:
    a: A parameter(multiplier) which is used in the algorithm
    m: A parameter which is used in the algorithm
    c: A parameter(increment) used in the algorithm
    no_sample: The number of random numbers to generate, returns a list
    x0: The initial value from which the algorithm should start
    repeat: If true then return a single random number between 0 and 1
    """
    rand = []
    x = x0
#     rand.append(x0)
    if repeat:
        x = x0*m
        for i in range(no_sample):
            x = (a*x+c)%m
            rand.append(x/m)
        return rand

    for i in range(no_sample):
        x = (a*x+c)%m
        rand.append(x/m)
    return rand

    

