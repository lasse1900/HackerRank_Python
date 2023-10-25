def longest_common_child(s1, s2):
    str1 = s1
    str2 = s2
    m, n = len(str1), len(str2)

    # Create a 2D table to store the lengths of common child strings
    table = [[0] * (n + 1) for x in range(m + 1)]

    # Fill in the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # Reconstruct the longest common child string
    common_child = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            common_child.append(str1[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the list to get the common child string in the correct order
    common_child = common_child[::-1]

    ret = ''.join(common_child)
    return len(ret)

# Example usage
# str1 = "AGGTAB"
# str2 = "GXTXAYB"
# str1 = "HARRY"
# str2 = "SALLY"

s1 = input()
s2 = input()
result = longest_common_child(s1, s2)
print(result)  # Output: "GTAB"
