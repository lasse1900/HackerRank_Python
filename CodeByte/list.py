
list = [1,2,6,7,9,3,4,10,8]
print(list)
list.sort()
print(list)

string = '1,2,6,5,9,8,7'
print(string)
print('-'*15)
string_2 = ''.join(string).split(',')
print(string_2)
string_2 = [x for x in string.split(',')]
print(string_2)

print(string_2[0])

jono = ''
for n in range(len(string_2)):
    jono = jono + string_2[n]

print(jono)