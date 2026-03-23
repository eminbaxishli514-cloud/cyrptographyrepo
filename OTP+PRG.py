import random

def to_bit_stream(data_bytes):
    result = ""
    for b in data_bytes:
        result += format(b, '08b')
    return result

def from_bit_stream(bit_string):
    byte_list = []
    for i in range(0, len(bit_string), 8):
        byte_chunk = bit_string[i : i + 8]
        byte_value = int(byte_chunk, 2)
        byte_list.append(byte_value)
    return bytes(byte_list)

def bit_wise_xor(bits1, bits2):
    result = ""
    for i in range(len(bits1)):
        b1 = int(bits1[i])
        b2 = int(bits2[i])
        result += str(b1 ^ b2)
    return result


def generate_prg_key(seed_value, length_in_bits):
    random.seed(seed_value)
    
    key_bits = ""
    for i in range(length_in_bits):
        bit = random.randint(0, 1)
        key_bits += str(bit)
    return key_bits

message = "salam"
seed = "my_secret_password"

#Message conversion
msg_bits = to_bit_stream(message.encode())
print("Message Bits:  " + msg_bits)

#PRG
keystream = generate_prg_key(seed, len(msg_bits))
print("PRG Keystream: " + keystream)

#The decryption process
cipher_bits = bit_wise_xor(msg_bits, keystream)
print("Cipher Bits:   " + cipher_bits)

#The decryption process
decrypted_bits = bit_wise_xor(cipher_bits, keystream)
print("Final Result:  " + from_bit_stream(decrypted_bits).decode())