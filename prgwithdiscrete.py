
def get_prime_factors(n):
    """Returns a set of all prime factors of n."""
    factors = set()
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.add(temp)
    return factors

def is_primitive_root(g, p):
    """Checks if g is a primitive root modulo"""
    if g < 2: 
        return False
    phi = p - 1
    factors = get_prime_factors(phi)
    for f in factors:
        if pow(g, phi // f, p) == 1:
            return False
    return True

def blum_micali_prg(seed, p, g, length):
    if not is_primitive_root(g, p):
        raise ValueError(f"Error: {g} is not a primitive root modulo {p}.")
    x = seed % p
    if x == 0: 
        x = 1
    
    bitstream = []
    limit = (p - 1) // 2

    for i in range(length):
        x = pow(g, x, p)
        bit = 1 if x <= limit else 0
        bitstream.append(bit)
    return bitstream

#Usage
if __name__ == "__main__":
    P = 503  
    G = 5    
    SEED = 123
    L = 60 
    print(f"Prime (p): {P}")
    print(f"Generator (g): {G}")
    print(f"Initial Seed: {SEED}")
    
    try:
        generated_bits = blum_micali_prg(SEED, P, G, L)
        bit_string = "".join(map(str, generated_bits))
        
        print(f"\nGenerated Bitstream ({L} bits):")
        print(bit_string)
        ones = bit_string.count('1')
        zeros = bit_string.count('0')
        print(f" - Ones:  {ones} ({(ones/L)*100:.1f}%)")
        print(f" - Zeros: {zeros} ({(zeros/L)*100:.1f}%)")
        
    except ValueError as e:
        print(e)
