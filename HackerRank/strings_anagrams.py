#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    array_a = a
    array_b = b
    pop_amount = 0
    if (len(array_a) == (len(array_b))):
        pop_amount = 1
    else:
        pop_amount = 0
    while len(array_a) >= 0:
        if  array_a != array_b:
            array_a = array_a[:-1]
            array_b = array_b[:-1]
            pop_amount += 1
        else:
            return pop_amount
    return False

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()
    b = input()
    res = makeAnagram(a, b)
    # fptr.write(str(res) + '\n')
    # fptr.close()
    print(res)
