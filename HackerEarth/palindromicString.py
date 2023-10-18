# name = input("Anna string: ")    # Reading input from STDIN
name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
if (name == name[::-1]):
    print("YES")
else:
    print("NO")