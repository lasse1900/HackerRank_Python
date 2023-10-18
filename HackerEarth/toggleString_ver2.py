# name = input("Anna string: ")    # Reading input from STDIN
name = input()                  # Reading input from STDIN
#print('Hi, %s.' % name)         # Writing output to STDOUT

name_2 = []
string = " "
for i in range(len(name)):
    if name[i].isupper():
        x = (name[i]).lower()
        name_2.insert(i, x)
    else:
        x = (name[i]).upper() 
        name_2.insert(i, x)

ret = string.join(name_2)    
output_string = ''.join(ret.split())    
print(output_string)
