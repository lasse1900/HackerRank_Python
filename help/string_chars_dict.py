
a = input("Give me a string of letters: ")
a = sorted(a)
print(a)


# Create dictionaries to count the frequency of each character in both strings
char_count_a = {}

# Count characters in string 'a'
for char in a:
    char_count_a[char] = char_count_a.get(char, 0) + 1


print('Amount of chars in the string:', char_count_a)

print(char_count_a.get('a'))

