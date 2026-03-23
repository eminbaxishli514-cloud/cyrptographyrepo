import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_rsa_keypair(prime_p: int, prime_q: int) -> tuple:
    modulus_n = prime_p * prime_q
    phi_n = (prime_p - 1) * (prime_q - 1)
    
    public_exponent_e = 65537#standard
    while public_exponent_e < phi_n:
        if gcd(public_exponent_e, phi_n) == 1:
            break
        public_exponent_e += 2
    # d is the modular multiplicative inverse of e modulo phi(n)
    # In Python 3.8+, pow() handles modular inverses when the exponent is -1
    private_exponent_d = pow(public_exponent_e, -1, phi_n)
    
    public_key = (public_exponent_e, modulus_n)
    private_key = (private_exponent_d, modulus_n)
    
    return public_key, private_key

def rsa_encrypt(message_int: int, public_key: tuple) -> int:
    """Encrypts an integer message using the public key."""
    public_exponent_e, modulus_n = public_key
    ciphertext = pow(message_int, public_exponent_e, modulus_n)
    return ciphertext

def rsa_decrypt(ciphertext_int: int, private_key: tuple) -> int:
    """Decrypts a ciphertext integer using the private key."""
    private_exponent_d, modulus_n = private_key
    decrypted_message = pow(ciphertext_int, private_exponent_d, modulus_n)
    return decrypted_message

# Usage
if __name__ == "__main__":
    print("--- RSA Demonstration ---")
    p, q = 61, 53 
    pub_key, priv_key = generate_rsa_keypair(p, q)
    
    original_message = 42
    encrypted = rsa_encrypt(original_message, pub_key)
    decrypted = rsa_decrypt(encrypted, priv_key)
    
    print(f"Original: {original_message} | Encrypted: {encrypted} | Decrypted: {decrypted}")