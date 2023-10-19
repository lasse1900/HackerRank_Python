
x = input("Give a string: ")
print(x[::-1])

y = x[::-1]
print(y)

string = input("Give another string: ")
pituus = len(string)
print(pituus)
for i in range(len(string)):
    if(len(string)-i) >= 0:
        print(string[len(string)-i-1], end='')

