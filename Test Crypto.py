from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# cipher_suit = Fernet('fVQIaUACFlaK7ltqWBViIqrpyTQkfnIccA0UlIsYF_A=')
# # print(key)
# # password = b'supersecretspassword'
# # encrypted_password = cipher_suit.encrypt(password)
# # print(encrypted_password)
#
# decrypted_password = cipher_suit.decrypt(b'gAAAAABbp92dSHxnmVICajPecwUax0b2KA9SjGko347k50kd8ljs7DtuPGNQK1P-FU-l9B8irqjPBzt28AxyR2X6d6wnU3YOnc-LBfBfMRPZX6SHqgMp7gw=')
# print(decrypted_password)


dict = dict( one = 1, two = 2, three = 3, four = 4, five = 5)
d = {'one':1, 'two':2, 'three':3}
l = ['hello', 'there', 'test', 'list']

dict['seven'] = 7
l.append('added text')
l.insert(0, 'start')
# for x in l:
#     print(x)

test = ['test', 'for', 'GitHub']

for x in test:
    print(x)