#This code does some operations that ready libraries offer, I tried to implement it for learning. Anyone can call a library.

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(password: str, salt: bytes) -> bytes:
    """Turns a password into a 32-byte key using 600,000 iterations."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000,
    )
    return kdf.derive(password.encode())

def encrypt(password: str, plaintext: str):
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = derive_key(password, salt)
    
    #Encrypt
    encryptor = Cipher(algorithms.AES(key), modes.CTR(iv)).encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return salt, iv, ciphertext

def decrypt(password: str, salt: bytes, iv: bytes, ciphertext: bytes):
    key = derive_key(password, salt)
    decryptor = Cipher(algorithms.AES(key), modes.CTR(iv)).decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode()

#Usage
my_password = "correct-horse-battery-staple"
message = "My name is Emin, and this is secure."
#Encryption
salt_val, iv_val, secret_data = encrypt(my_password, message)

print(f"Stored Salt: {salt_val.hex()}")
print(f"Stored IV:   {iv_val.hex()}")
print(f"Ciphertext:  {secret_data.hex()}")
#Decryption
try:
    original_text = decrypt(my_password, salt_val, iv_val, secret_data)
    print(f"\nDecrypted Message: {original_text}")
except Exception as e:
    print("Decryption failed! Check your password.")
