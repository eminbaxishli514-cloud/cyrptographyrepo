import os

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
        xor_result = b1 ^ b2
        result += str(xor_result)
    return result


#Input message
message = input("Enter your secret message: ")
message_bytes = message.encode()

message_bits = to_bit_stream(message_bytes)
print("Message Bits: " + message_bits)

num_bits = len(message_bits)
num_bytes = (num_bits + 7) // 8
random_data = os.urandom(num_bytes)
key_bits = to_bit_stream(random_data)
key_bits = key_bits[:num_bits]
print("Key Bits:     " + key_bits)

#The encryption process
cipher_bits = bit_wise_xor(message_bits, key_bits)
print("Cipher Bits:  " + cipher_bits)

#The decryption process
decrypted_bits = bit_wise_xor(cipher_bits, key_bits)
decrypted_text = from_bit_stream(decrypted_bits).decode()

print("\nFinal Result(decrypted, to test the decryption validity): " + decrypted_text)




#The random library

