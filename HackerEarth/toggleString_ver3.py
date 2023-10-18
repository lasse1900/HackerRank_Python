# name = input("Anna string: ")    # Reading input from STDIN
name = input()                  # Reading input from STDIN
#print('Hi, %s.' % name)         # Writing output to STDOUT

name_2 = []
string = " "
for i in range(len(name)):
    x = (name[i]).swapcase()
    name_2.append(x)

ret = string.join(name_2)    
output_string = ''.join(ret.split())    
print(output_string)
