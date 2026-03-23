import os

def otp_xor(data: bytes, key: bytes) -> bytes:
    return bytes([b1 ^ b2 for b1, b2 in zip(data, key)])

#The message
message = input("Enter your secret message: ").encode()

#Key Generation (Must be the same length as the message)
key = os.urandom(len(message))

#Process
ciphertext = otp_xor(message, key)
decrypted = otp_xor(ciphertext, key)

print(f"Ciphertext (Hex): {ciphertext.hex()}")
print(f"Decrypted:        {decrypted.decode()}")
