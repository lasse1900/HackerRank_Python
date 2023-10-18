
string = input("Give a string: ")

for i in range(len(string)):
    if (len(string) - i ) >= 0: 
        print(string[len(string)-i-1], end='')

print('-'*15)

reversed_string = string[::-1]
print(reversed_string)



