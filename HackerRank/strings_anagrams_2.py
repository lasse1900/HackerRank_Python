def makeAnagram(a, b):
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
        if char in char_count_b:
            removal_count += abs(char_count_a[char] - char_count_b[char])
        else:
            removal_count += char_count_a[char]

    for char in char_count_b:
        if char not in char_count_a:
            removal_count += char_count_b[char]

    return removal_count

if __name__ == '__main__':
    a = input()
    b = input()
    res = makeAnagram(a, b)
    print(res)

# It seems like you want to modify the given code to calculate the number of characters that need to be removed from two strings to make them anagrams. 
# The code has a few issues. # Here's a corrected version of your code:

# This code counts the frequency of characters in both strings and calculates the number of characters to be removed to make them anagrams. 
# It should give you the correct result.