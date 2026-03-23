import secrets



def is_primitive_root(g: int, p: int) -> bool:
    seen = set()

    for i in range(1, p):
        val = pow(g, i, p)
        if val in seen:
            return False
        seen.add(val)

    return len(seen) == p - 1


def find_primitive_root(p: int) -> int:
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    raise ValueError("No primitive root found")



    

def generate_dh_public_key(private_key: int, generator_g: int, prime_p: int) -> int:
    """Computes the public key component to send to the other party."""
    return pow(generator_g, private_key, prime_p)

def compute_dh_shared_secret(others_public_key: int, my_private_key: int, prime_p: int) -> int:
    """Computes the final shared secret."""
    return pow(others_public_key, my_private_key, prime_p)

#Usage
if __name__ == "__main__":
    # Public parameters agreed upon by Alice and Bob
    prime_modulus_p = 23  # Usually a very large prime
    generator_g = find_primitive_root(prime_modulus_p)       # A primitive root modulo p
    
    # 1. Alice generates her keys
    alice_private_key = secrets.randbelow(prime_modulus_p - 2) + 1
    alice_public_key = generate_dh_public_key(alice_private_key, generator_g, prime_modulus_p)
    
    # 2. Bob generates his keys
    bob_private_key = secrets.randbelow(prime_modulus_p - 2) + 1
    bob_public_key = generate_dh_public_key(bob_private_key, generator_g, prime_modulus_p)
    
    # 3. They exchange public keys over the open internet. 
    # Alice computes the secret using Bob's public key
    alice_shared_secret = compute_dh_shared_secret(bob_public_key, alice_private_key, prime_modulus_p)
    
    # Bob computes the secret using Alice's public key
    bob_shared_secret = compute_dh_shared_secret(alice_public_key, bob_private_key, prime_modulus_p)
    
    print(f"Alice's calculated secret: {alice_shared_secret}")
    print(f"Bob's calculated secret:   {bob_shared_secret}")
    print(f"Match Successful:          {alice_shared_secret == bob_shared_secret}")