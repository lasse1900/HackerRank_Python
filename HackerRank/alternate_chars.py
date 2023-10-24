
# Sample input in HackerRank
# 5
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB

def min_deletions_to_avoid_matching_adjacent(s):
    deletions = 0
    i = 1  # Start from the second character

    while i < len(s):
        if s[i] == s[i - 1]:
            deletions += 1
        i += 1

    return deletions

# Example usage:
# string = 'AABAAB'
string = 'AABAAB'
result = min_deletions_to_avoid_matching_adjacent(string)
print(f"Minimum deletions required: {result}")

