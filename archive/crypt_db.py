from cryptography.fernet import Fernet
import os

with open('database.db', 'wb') as file1:
    plaintext = file1.read()

print(os.environ.get('db_pw').encode('ascii'))
cipher = Fernet(os.environ.get('db_pw').encode('ascii'))
ciphertext = cipher.encrypt(plaintext)

with open('encrypted.bin', 'wb') as file:
    file.write(ciphertext)

# with open('encrypted.bin', 'rb') as file:
#     ciphertext = file.read()
#     cipher = Fernet(os.environ.get('db_pw').encode('ascii'))
#     print(cipher.decrypt(ciphertext))
