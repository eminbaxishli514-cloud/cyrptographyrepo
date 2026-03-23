import math

def is_primitive_root(g, p):
    """Checks if g is a primitive root modulo p."""
    if g < 2: 
        return False
    q = (p - 1) // 2
    if pow(g, 2, p) == 1: return False
    if pow(g, q, p) == 1: return False
    return True

def blum_micali_prg(seed, p, g, length):
    if not is_primitive_root(g, p):
        print(f"Warning: {g} is not a primitive root of {p}. Period may be short.")
    
    # Ensure seed is within the valid exponent range [1, p-1]
    value = seed % (p - 1)
    if value == 0: value = 1
    
    bitstream = []
    limit = (p - 1) // 2

    for i in range(length):
        value = pow(g, value, p)
        bit = 1 if value > limit else 0
        bitstream.append(bit)
        
    return bitstream

#Usage
if __name__ == "__main__":
    P = 503
    G = 5
    SEED = 123
    L = 50

    print("--- Blum-Micali PRG Test ---")
    print(f"Prime (p): {P}")
    print(f"Generator (g): {G}")
    print(f"Seed: {SEED}")
    
    generated_bits = blum_micali_prg(SEED, P, G, L)
    bit_string = "".join(map(str, generated_bits))
    
    print(f"\nGenerated Bitstream ({L} bits):")
    print(bit_string)
    
    # Statistical test
    ones = bit_string.count('1')
    zeros = bit_string.count('0')
    print(f"\nStats: {ones} ones, {zeros} zeros")
