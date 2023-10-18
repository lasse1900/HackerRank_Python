
# https://www.youtube.com/watch?v=EsdVqCK--4M
string = 'Hello world I am coding'
string_cap = 'Hello World I Am Coding'
num = '50'
num2 = '50g'

# string[START: END: STEP]

print(string[5:10:1])
print(string[6:11:2])
print(string[::-1])
print(string[::-2])

print(len(string))

print(num.isdigit())
print(num2.isdigit())
print('-'*15)
print(num.isnumeric())

print(string.find('world'))

print('-'*15)
print(string[string.find('I'):])
print(string[string.find('I'):18:])

print('-'*15)
print(string.title()) # Capitalize every word
print(string_cap.istitle())

print(list(string))
print(string.upper())
string = string.upper()
print(string.isupper())

print('-'*15)
print(string.swapcase())
