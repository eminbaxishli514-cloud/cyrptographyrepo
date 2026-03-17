def prg(seed, p, g, length):
    value = seed
    bitstream = []
    limit = (p - 1) // 2

    for i in range(length):
        if value > limit:
            bit = 1
        else:
            bit = 0
        bitstream.append(bit)
        value = pow(g, value, p)
        
    return bitstream


my_seed = 123
my_bits = prg(seed=my_seed, p=701, g=2, length=50)

print(f"Seed: {my_seed}")
print(f"Generated Bits: {''.join(map(str, my_bits))}")