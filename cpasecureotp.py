import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def prf_f(key: bytes, x: bytes) -> bytes:
    block_function = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    return block_function.update(x) + block_function.finalize()

def cpa_encrypt(key: bytes, message: bytes) -> tuple:
    # 1. IV (r) must be random and unique for every encryption
    iv = secrets.token_bytes(16)
    full_pad = b""
    
    # 2. Determine how many 16-byte blocks we need
    num_blocks = (len(message) + 15) // 16
    
    # 3. Generate a long enough pad by incrementing a counter
    # We treat the IV as a large integer and add i to it
    iv_int = int.from_bytes(iv, "big")
    for i in range(num_blocks):
        counter_block = ((iv_int + i) % (2**128)).to_bytes(16, "big")
        full_pad += prf_f(key, counter_block)
    
    # 4. XOR the entire message with the generated long pad
    ciphertext = bytes([m ^ p for m, p in zip(message, full_pad)])
    return iv, ciphertext

def cpa_decrypt(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
    # Decryption is identical to encryption!
    full_pad = b""
    num_blocks = (len(ciphertext) + 15) // 16
    iv_int = int.from_bytes(iv, "big")
    
    for i in range(num_blocks):
        counter_block = ((iv_int + i) % (2**128)).to_bytes(16, "big")
        full_pad += prf_f(key, counter_block)
        
    return bytes([c ^ p for c, p in zip(ciphertext, full_pad)])

if __name__ == "__main__":
    secret_key = secrets.token_bytes(16)
    long_message = b"My name is Emin, dont tell anyone"

    iv_val, encrypted = cpa_encrypt(secret_key, long_message)
    decrypted = cpa_decrypt(secret_key, iv_val, encrypted)

    print(f"Original Length: {len(long_message)}")
    print(f"Cipher Length:   {len(encrypted)}")
    print(f"Match:           {long_message == decrypted}")
    print(f"Decrypted:       {decrypted.decode()}")