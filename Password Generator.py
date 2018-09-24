import random
import base64
from cryptography.fernet import Fernet
import linecache
import crypto

numbers = ['1', '2', '3', '4', '5', '6', '7']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
extras = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', ';', ':', '|', ',', '.', '/', '<', '>', '?']

#SET CIPHER KEY

# key = Fernet.generate_key()
# print(key)
cipher_suite = Fernet('Kx0Kig3JwMXemNz36tfS3nE_ThF_BZ8K1RpyD7X4nfM=')

# # ECRYPTING PASSWORD
# testfile = open('testing.txt', 'w')
# password = 'thisisnewpass'
# encrypted_pass = cipher_suite.encrypt(password.encode())
# testfile.write(str(encrypted_pass))
# testfile.close()
# DECRYPTING PASSWORD
# readfile = linecache.getline('rename.txt', 2).replace("'", "")
# print(readfile)
# readfile = readfile[1:len(readfile)].encode()
# print(readfile)
# decrypt_pass = cipher_suite.decrypt(readfile)
# print(decrypt_pass)



savefile = open('rename.txt', 'a')

#GENERATE PASSWORD
class GeneratePass:
    def name_password(self):
        # passname = input('What is the password for?: ')
        passname = 'Testname'
        passname_len = len(passname)
        hash_len = 30 - passname_len
        hash_len = int(hash_len/2)
        hash_len = hash_len*'#'
        pass_title = hash_len + ' ' + passname.upper() + ' ' + hash_len + '\n'
        if len(pass_title) != 33:
            pass_title = hash_len + ' ' + passname.upper() + ' ' + hash_len + '#' + '\n'
        savefile.write(pass_title)
    #GENERATE AND SAVES PASSWORD
    def passgen_plaintext(self):
        # passlen = int(input('Please choose the len of pass: '))
        passlen = 10
        nopassword = 0
        for x in range(passlen):
            number = random.choice(numbers)
            lower = random. choice(lowercase)
            upper = random.choice(uppercase)
            extra = random.choice(extras)
            #RANDOMISE PASSWORD
            random_char = (number, lower, upper, extra)
            nopassword = nopassword + 1
            password = random.choice(random_char)
            savefile.write(password)
            # print(password, end='')
            if passlen == nopassword:
                break
        # print(password)
        savefile.write('\n')
        # savefile.write('\n')
        # savefile.close()

    #GENERATE AND SAVES ENCRYPTED PASSWORD
    def passgen_encrypted(self):
        # savefile = open('rename.txt', 'r')
        password = linecache.getline('rename.txt', 2)
        print(password)
        password = password.encode()
        encrypted_pass = cipher_suite.encrypt(password)
        savefile.write(str(encrypted_pass))
        print(encrypted_pass)
        savefile.write('\n')
        savefile.write('\n')
        savefile.close()

    def passgen_decrypt(self):
        # openfile = open('rename.txt')
        readline = linecache.getline('rename.txt', 3)
        # print(readline)
        # print(type(readline))
        decrypt_line = readline.replace("'", "")  # .encode()
        # print(decrypt_line)
        # print(type(decrypt_line))
        decrypt_pass = decrypt_line[1:len(decrypt_line)-1]#.encode()
        # print(decrypt_pass)
        # print(type(decrypt_pass))

        decrypt = cipher_suite.decrypt(decrypt_pass.encode())
        print(type(decrypt))
        print(str(decrypt))
        # decrypt = decrypt
        # print(decrypt)

# GPN = GeneratePass().name_password()
# GP = GeneratePass().passgen_plaintext()
# GP = GeneratePass().passgen_encrypted()
GPD = GeneratePass().passgen_decrypt()

    # encrypt_file = cipher_suite.encrypt(savefile)













#################################################
################### TESTING #####################
#################################################

# class SaveDown:
#     savepass = open('rename.txt', 'w')
#     savepass.write(GeneratePass.password)
#     savepass.close()


#################################################


# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
# cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
# plain_text = cipher_suite.decrypt(cipher_text)
#
# print(key)
# print(cipher_text)
# print(plain_text)


##################################################

# password = b'testing09808080%'
# cr = base64.encodebytes(password)
# # password = base64.b64decode(password)
# decodepass = base64.decodebytes(cr)
# print(decodepass)
# print(cr)

##################################################