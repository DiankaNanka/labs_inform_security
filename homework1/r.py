file = open('zash.txt', 'r')

text = "".join(file)

words = 0

pos = 'out'

for i in text:

    if i != ' ' and pos == 'out':

        words += 1

        pos = 'in'

    elif i == ' ':

        pos = 'out'

print('Words: ', words)