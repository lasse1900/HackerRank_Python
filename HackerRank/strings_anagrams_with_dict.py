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
    # Create dictionaries to count the frequency of each character in both strings
    char_count_a = {}
    char_count_b = {}

    # Count characters in string 'a'
    for char in a:
        char_count_a[char] = char_count_a.get(char, 0) + 1

    # Count characters in string 'b'
    for char in b:
        char_count_b[char] = char_count_b.get(char, 0) + 1

    # Initialize the count of characters to be removed
    removal_count = 0

    # Calculate the number of characters to be removed to make the strings anagrams
    for char in char_count_a:
        # print('char in a:', char)
        if char in char_count_b:
            print('if char also in b: ', char)
            # print('<->', char_count_a[char], ' ', char_count_b[char])
            removal_count += abs(char_count_a[char] - char_count_b[char])
        else:
            print('--> ', char)
            removal_count += char_count_a[char]

    for char in char_count_b:
        if char not in char_count_a:
            removal_count += char_count_b[char]

    return removal_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()
    b = input()
    res = makeAnagram(a, b)
    # fptr.write(str(res) + '\n')
    # fptr.close()
    print(res)
