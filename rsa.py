import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_rsa_keypair(prime_p: int, prime_q: int) -> tuple:
    modulus_n = prime_p * prime_q
    phi_n = (prime_p - 1) * (prime_q - 1)
    
    e = 65537
    if e >= phi_n or gcd(e, phi_n) != 1:
        e = 3
        while gcd(e, phi_n) != 1:
            e += 2
    private_exponent_d = pow(e, -1, phi_n)
    
    public_key = (e, modulus_n)
    private_key = (private_exponent_d, modulus_n)
    
    return public_key, private_key

def rsa_encrypt(message_int: int, public_key: tuple) -> int:
    public_exponent_e, modulus_n = public_key
    if not (0 <= message_int < modulus_n):
        raise ValueError(f"Message {message_int} must be between 0 and {modulus_n - 1}")
    ciphertext = pow(message_int, public_exponent_e, modulus_n)
    return ciphertext

def rsa_decrypt(ciphertext_int: int, private_key: tuple) -> int:
    private_exponent_d, modulus_n = private_key
    decrypted_message = pow(ciphertext_int, private_exponent_d, modulus_n)
    return decrypted_message

# Usage
if __name__ == "__main__":
    p, q = 61, 53 
    pub_key, priv_key = generate_rsa_keypair(p, q)
    original_message = 42
    encrypted = rsa_encrypt(original_message, pub_key)
    decrypted = rsa_decrypt(encrypted, priv_key)
    
    print(f"Original: {original_message} | Encrypted: {encrypted} | Decrypted: {decrypted}")
