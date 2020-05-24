class Xorr:

    def __init__(self, file_path, key):

        self.file_path = file_path

        self.key = key

        self.content = self.encrypted_text = self.decrypted_text = None



    def r_file(self):

        with open(self.file_path, 'r', encoding='utf8') as f:

            self.content = ''.join([line for line in f])



    def __xor_operation(self, text):

        content_codes = list(map(ord, text))

        key_codes = list(map(ord, self.key))

        key_codes_length = len(key_codes)

        new_codes = []

        for i in range(len(content_codes)):

            j = i % key_codes_length

            new_codes.append(content_codes[i] ^ key_codes[j])

        return ''.join(list(map(chr, new_codes)))



    def enc_text(self):

        self.enc_text = self.__xor_operation(self.content)



    def dec_text(self):

        self.dec_text = self.__xor_operation(self.enc_text)

        print(self.dec_text == self.content)  # для проверки



    def w_file(self):

        with open('./encrypted.txt', 'w', encoding='utf8') as f:

            f.write(self.enc_text)





X_C = Xorr('./encrypt.txt', input('key: '))

X_C.r_file()

X_C.enc_text()

X_C.dec_text()

X_C.w_file()