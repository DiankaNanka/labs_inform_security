def z(o):

    zash = o

    zash = zash.lower()

    key = 3

    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    rash = ""

    for letter in zash:

        position = alphabet.find(letter)

        newPosition = position + key

        if letter in alphabet:

            rash = rash + alphabet[newPosition]

        else:

            rash = rash + letter

    return rash



f1 = open('zash.txt', 'r')

text = "".join(f1)

gg = z(text)

f2 = open('rash.txt', 'w')

f2.writelines(gg)

f2.close()