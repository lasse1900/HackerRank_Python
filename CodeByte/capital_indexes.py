

char_string = 'HeLlO'

def capital_indexes(jono):
    # marks = ''
    marks_2 = []
    for i in range(len(jono)):
        if jono[i].isupper():
            # print(i)
            # marks = marks + str(i)
            marks_2.append(i)
    return marks_2

print(capital_indexes(char_string))