#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n=len(arr)
    p=0
    neg=0
    t=0
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            neg+=1
        else:
            t+=1
    print(p/len(arr))
    print(neg/len(arr))
    print(t/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
