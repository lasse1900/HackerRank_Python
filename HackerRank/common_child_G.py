def longest_common_child(s1, s2):

    n = len(s1)
    m = len(s2)

    # Create a table to store the lengths of the longest common suffixes of all
    # substrings of str1 and str2.
    table = [[0 for x in range(m + 1)] for x in range(n + 1)]

    # Iterate over the strings, and fill in the table.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # The longest common child is the length of the longest common suffix of the
    # two strings.
    return table[n][m]


# Example usage:
# s1 = "ABCDGH"
# s2 = "AEDFHR"
s1 = input()
s2 = input()

# print("The longest common child is", longest_common_child(s1, s2))
print(longest_common_child(s1, s2))