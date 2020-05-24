import random



alphabet = "абвгдежзиклмнопрстуфхцчшщыьэюя"



def correct(gogo):

    text = "".join(gogo)

    text = text.lower()

    text = text.replace("ъ","ь")

    text = text.replace("ё","е")

    text = text.replace("й","и")

    text = text.replace(" ","ё")

    return text



def keygen():

    index = list(range(len(alphabet)))

    random.shuffle(index)

    key = "".join([alphabet[i] for i in index])

    f = open('key.txt', 'w')

    for i in range(0, len(alphabet)):

        f.write(alphabet[i] + ' ---> ' + key[i]+ '\n')

    f.write('" " -> ё')

    return key



def crypt(g, key):

    text = list(g)

    for i in range(len(text)):

        if text[i] in alphabet:

            index = alphabet.index(text[i])

            text[i] = key[index]

    return "".join(text)



def decrypt(g, key):

    text = list(g)

    for i in range(len(text)):

        if text[i] in key:

            index2 = key.index(text[i])

            text[i] = alphabet[index2]

    return "".join(text)



def read():

    text = ""

    f = open('ex.txt', 'r')

    g = f.read()

    text = "".join(g)

    return text



def write(dada):

    f = open('ex2.txt', 'w')

    f.write(dada)



def write_dec(a):

    f = open('ex3.txt','w')

    a = a.replace('ё',' ')

    f.write(a)



text = read()

text = correct(text)

key = keygen()

text = crypt(text, key)

write(text)

text = decrypt(text, key)

write_dec(text)