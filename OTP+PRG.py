#This code does some operations that ready libraries offer, I tried to implement it for learning. Anyone can call a library.

import hashlib
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def generate_secure_keystream(password, length_in_bytes):
    key = hashlib.sha256(password.encode()).digest()
    
    # We use a random IV so that the same password produces a different pad every time
    iv = secrets.token_bytes(16)
    
    # Use AES in CTR mode to generate the pseudo-random keystream
    encryptor = Cipher(algorithms.AES(key), modes.CTR(iv)).encryptor()
    keystream = encryptor.update(b'\x00' * length_in_bytes)
    
    return iv, keystream

def xor_bytes(data, pad):
    return bytes([b1 ^ b2 for b1, b2 in zip(data, pad)])

#Usage
message = "salam".encode()
password = "my_secret_password"

#Generation
iv, pad = generate_secure_keystream(password, len(message))

#Encryption
ciphertext = xor_bytes(message, pad)

# 3. Decryption
decrypted = xor_bytes(ciphertext, pad)

print(f"Original:  {message.decode()}")
print(f"Cipher:    {ciphertext.hex()}")
print(f"Decrypted: {decrypted.decode()}")
