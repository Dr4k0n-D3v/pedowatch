import os
import hashlib
from Crypto.Cipher import AES

def decrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
    
        salt = encrypted_data[:AES.block_size]
        iv = encrypted_data[AES.block_size:AES.block_size*2]
        encrypted_data = encrypted_data[AES.block_size*2:]
    
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    
        cipher = AES.new(key, AES.MODE_CBC, iv)
    
        decrypted_data = cipher.decrypt(encrypted_data)
    
        pad_len = decrypted_data[-1]
        decrypted_data = decrypted_data[:-pad_len]
    
        with open(file_path, 'wb') as f:
            f.write(decrypted_data)
    except:
        pass

def decrypt_directory(dir_path, password):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, password)

if __name__ == '__main__':
    password = 'qwertyiop321654sheeilikemenbb3ksij4jgi4ew0fisjiogajlrs8o--_i3jt24'
    decrypt_directory('testing', password)