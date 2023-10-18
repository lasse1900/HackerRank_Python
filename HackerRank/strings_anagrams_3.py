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
    """
    Finds the amount of characters to be removed so that two given strings are anagrams.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        int: The amount of characters to be removed.
    """

    # Check if the strings have the same length. If not, they cannot be anagrams.
    # if len(a) != len(b):
    #     return False

    # Create two dictionaries to store the character counts of the two strings.
    a_counts = {}
    b_counts = {}
    for char in a:
        a_counts[char] = a_counts.get(char, 0) + 1
    for char in b:
        b_counts[char] = b_counts.get(char, 0) + 1

    # Find the number of characters to be removed from each string.
    a_removals = 0
    b_removals = 0
    for char in a_counts:
        if char not in b_counts or a_counts[char] > b_counts[char]:
            a_removals += a_counts[char] - b_counts.get(char, 0)
    for char in b_counts:
        if char not in a_counts or b_counts[char] > a_counts.get(char, 0):
            b_removals += b_counts[char] - a_counts.get(char, 0)

    # Return the total number of characters to be removed.
    return a_removals + b_removals


if __name__ == '__main__':
    # Get the input strings.
    a = input()
    b = input()

    # Find the number of characters to be removed.
    res = makeAnagram(a, b)

    # Print the result.
    print(res)


# This program works by first checking if the two strings have the same length. If not, they cannot be anagrams and the program returns False. Otherwise, the program creates two dictionaries to store the character counts of the two strings.

# Next, the program finds the number of characters to be removed from each string. This is done by comparing the character counts of the two strings. If a character appears more times in one string than in the other, the program counts the difference as the number of characters to be removed from that string.

# Finally, the program returns the total number of characters to be removed from the two strings.