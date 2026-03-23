#Ceaser Cipher (`ceasercipher.py`) does this
This file implements a Caesar-style shift on lowercase letters (`a` to `z`).
It has 2 main functions: `encrypt(text, key)` and `decyrpt(ciphertext, key)` (spelling is `decyrpt` in code).

Step 1: It defines `finder(a, b)`.
It loops `for i in range(len(a)):` and returns `i` when `a[i] == b`.

Step 2: `encrypt(text, key)` starts.
It sets `result = ""`.
It sets `letters = "abcdefghijklmnopqrstuvwxyz"`.

Step 3: It loops through the plaintext character by character (`for i in text:`).
Inside the loop it checks `if i in text:`.
This condition is always true, because `i` is already coming from `text`.
So the `else:` branch basically never runs.

Step 4: Still inside the loop, it calculates the shifted letter.
It calls `number = finder(letters, i)`.
So `i` must be exactly one of `letters` (otherwise `finder` returns `None` and the next math breaks).
Then it computes `letters[(number + key) % 26]`.

Step 5: It appends the shifted result to `result`.

Step 6: `decyrpt(ciphertext, key)` reverses the shift.
It also sets `letters = "abcdefghijklmnopqrstuvwxyz"` and `result = ""`.
For each ciphertext character `i`:
1. If `i` is in `letters`, it finds its index `number`.
2. It computes `letters[(number - key) % 26]` and appends that.
3. If `i` is NOT in `letters`, it appends `i` unchanged.

Step 7: The file is mostly function-only.
The bottom parts that would read input are commented out (so nothing runs unless you call `encrypt` / `decyrpt` from another script).

#Brute Force Ceaser (`bruteforceceaser.py`) does this
This file tries all Caesar keys (1..25) to decrypt a fixed ciphertext.
It uses a known expected plaintext to identify the correct key.

Step 1: It stores one fixed ciphertext string in `cipher_text`.

Step 2: It defines `finder(a, b)`.
Same idea: find the index of a character in a list/string.

Step 3: It defines `decyrpt(ciphertext, key)`.
For each character `i` in `ciphertext`:
1. If `i` is a lowercase letter, it finds its index `number` in `letters = "abcdefghijklmnopqrstuvwxyz"`.
2. It shifts backwards with `letters[(number - key) % 26]`.
3. Non-letters are appended unchanged.

Step 4: It builds a list of keys.
`key_space` starts empty.
Then it loops `for i in range(1, 26):` which gives keys 1..25.

Step 5: It prints decryption for every key.
For each `i` in `key_space` it runs `print(f"{decyrpt(cipher_text,i)}\n")`.
So you see 25 plaintext candidates.

Step 6: It finds the key using the expected plaintext.
It loops keys again:
If `decyrpt(cipher_text, i) == "ifweallunitewewillcausetheriverstostainthegreatwaterswiththeirblood"`
then it prints that key `i`.

#Affine Cipher (`affinecipher.py`) does this
This file implements an affine substitution cipher on lowercase letters.
Formula used in encryption: `y = (multiplier * x + shifter) % 26`
Formula used in decryption (with modular inverse): `x = inverse_multiplier * (y - shifter) mod 26`

Step 1: It defines `finder(a, b)`.
It returns the index where `a[i] == b`.

Step 2: It defines `gcd(a, b)` using Euclidean algorithm.
It keeps replacing `(a, b)` with `(b, a % b)` until `b == 0`.
It returns the final `a`.

Step 3: `encrypt(plaintext, multiplier, shifter)` begins.
It sets `letters = "abcdefghijklmnopqrstuvwxyz"` and `result = ""`.

Step 4: It checks the key is valid.
It checks `if gcd(multiplier, 26) == 1:`.
If `multiplier` is coprime with 26, an inverse exists and decryption can work.
If not, it returns the message:
"For the inverse to exist, the number must be coprime to 26."

Step 5: It loops through the plaintext.
It runs `for char in plaintext.lower():`
So uppercase input becomes lowercase.

Step 6: For each character:
If `char in letters`:
1. `x = finder(letters, char)` gives the letter index (0..25).
2. `y = (multiplier * x + shifter) % 26` computes the encrypted index.
3. Append `letters[y]` to `result`.
Else:
Append the character unchanged to `result`.

Step 7: `inverse(a, m=26)` finds the modular inverse.
It loops `for i in range(1, m):` (so i is 1..25).
It checks `(i * a) % m == 1`.
When it finds one, it returns `i`.
If it never finds one, it returns `None`.

Step 8: `decrypt(ciphertext, multiplier, shifter, inverse_of_multiplier)` reverses.
It sets `letters` and `result` again.
It checks `if gcd(multiplier, 26) == 1:`.
Then for each ciphertext character `i`:
1. If `i in letters`:
   - `y = finder(letters, i)` is the ciphertext index.
   - It computes `x = (inverse_of_multiplier * (y - shifter)) % 26`.
   - Append `letters[x]` to the plaintext result.
2. Otherwise append `i` unchanged.

Step 9: Bottom of the file runs a demo.
It sets `plaintext = "hello world"`, `multiplier = 5`, `shifter = 8`.
It encrypts, prints ciphertext.
It computes `inv = inverse(multiplier)`.
Then it decrypts and prints the decrypted text.

#Frequency Analysis (`frequencyanalysis.py`) does this
This file uses a frequency attack idea to guess the Caesar key.
It assumes the ciphertext is from a substitution that preserves letter order statistics (here it tries Caesar shifts).

Step 1: It stores expected English frequencies in `letter_frequencies`.

Step 2: It counts frequencies in the ciphertext.
It sets `our_frequencies = {}`.
Then it loops `for i in cipher_text:`:
1. If `i` not in `our_frequencies`, set it to 1.
2. Else increase by 1.

Step 3: It converts counts into probabilities.
It sets `length = len(cipher_text)`.
Then for each key `i` in `our_frequencies`:
It replaces `our_frequencies[i] = our_frequencies[i] / length`.

Step 4: It sorts English letters by frequency.
`letters = sorted(letter_frequencies, key=letter_frequencies.get, reverse=True)`.
So `letters[0]` is the most common English letter, etc.

Step 5: It sorts ciphertext letters by observed frequency.
`cipher_chars = sorted(our_frequencies, key=our_frequencies.get, reverse=True)`.
So `cipher_chars[0]` is the most common ciphertext letter observed.

Step 6: It defines `difference(a, b)` to create candidate keys.
Inside `difference`:
1. It sets `alphabet = "abcdefghijklmnopqrstuvwxyz"`.
2. It loops over every index `i` in `alphabet` and finds `first_index` for `a` and `second_index` for `b`.
3. It returns `(first_index - second_index) % 26`.
So if ciphertext letter `a` is aligned to English letter `b`, the key is that difference.

Step 7: It generates a list of candidate keys.
It builds `differences = []`.
For `i` in `range(len(cipher_chars))`:
It appends `difference(cipher_chars[i], letters[i])`.
Meaning: it pairs the i-th most frequent ciphertext letter with the i-th most frequent English letter.

Step 8: It decrypts using each candidate key.
It defines `decyrpt(ciphertext, key)` (again with backwards shift `letters[(number-key)%26]`).
Then for each `i` in `differences`:
It prints `decyrpt(cipher_text, i)`.

#GCD methods (`gcd.py`) does this
This file is a mini notebook for different gcd approaches.
Important: it repeatedly redefines `def gcd(a,b):` multiple times.
So the name `gcd` changes meaning after each redefinition.

Part 1: Slow divisor checking (and note about it)
Step 1: It defines `gcd(a,b)` with:
1. `result = 1`
2. For every `i` in `range(1, a+1)`:
   - If `a%i == 0 and b%i == 0`, it multiplies `result *= i`.
Step 2: It sets `a = 5`, `b = 10` and prints `gcd(5,10)`.
For `5` and `10`, the common divisors are `1` and `5`, so product is `5`, matching the real gcd.
But for other numbers, multiplying all common divisors is not the same as gcd.

Part 2: “A bit faster version”
Step 1: It redefines `gcd(a,b)`.
This time it loops `for i in range(1, min(a, b) + 1):`
and still multiplies all i that divide both.
Then it prints the same `gcd(5,10)` again.

Part 3: Euclidean algorithm (correct gcd)
Step 1: It redefines `gcd(a,b)`:
While `b` is not zero:
1. Set `a, b = b, a % b`
Return `a`.
Then it prints `gcd(5,10)`.

Part 4: Built-in example
It imports `math` and prints `math.gcd(a,b)` for the same `a=5,b=10`.

Part 5: Subtraction-based gcd
It redefines `gcd(a,b)` again:
While `a != b`:
1. If `a > b`, set `a -= b`.
2. Else set `b -= a`.
Return `a`.
Then it prints that gcd.

#Extended Euclidean (`extendedecludian.py`) does this
This file computes the extended gcd.

Step 1: `extended_gcd(a, b)` initializes coefficients.
It sets `x0, x1 = 1, 0` and `y0, y1 = 0, 1`.
These track coefficients for representing the gcd as a linear combination.

Step 2: It loops while `b != 0`.
1. Computes quotient `q = a // b`.
2. Updates `(a, b) = (b, a % b)`.
3. Updates the x-coefficients:
   - `x0, x1 = x1, x0 - q * x1`
4. Updates the y-coefficients:
   - `y0, y1 = y1, y0 - q * y1`

Step 3: It returns `(a, x0, y0)`.
When the loop ends, `a` is the gcd and `x0,y0` are the coefficients such that:
`a_original * x0 + b_original * y0 = gcd`

Step 4: Bottom of file reads input and prints.
It asks the user for `a` and `b` with `input(...)`.
Then it prints `extended_gcd(a,b)`.

#RSA (`rsa.py`) does this
This file shows a minimal RSA encryption/decryption demo using small primes.

Step 1: It defines `gcd(a,b)` (Euclidean algorithm).
This gcd is used to ensure `e` is valid.

Step 2: `generate_rsa_keypair(prime_p, prime_q)` builds keys.
1. Compute `modulus_n = prime_p * prime_q`
2. Compute Euler totient `phi_n = (prime_p - 1) * (prime_q - 1)`
3. Start with `public_exponent_e = 65537`
4. While `public_exponent_e < phi_n`:
   - If `gcd(public_exponent_e, phi_n) == 1`, break (valid e)
   - Else increase `public_exponent_e += 2`
5. Compute `private_exponent_d = pow(public_exponent_e, -1, phi_n)`.
This returns the modular inverse of `e` modulo `phi_n`.
6. It returns:
   - `public_key = (public_exponent_e, modulus_n)`
   - `private_key = (private_exponent_d, modulus_n)`

Step 3: `rsa_encrypt(message_int, public_key)`.
It unpacks `(e, n)` and computes:
`ciphertext = pow(message_int, e, n)`.

Step 4: `rsa_decrypt(ciphertext_int, private_key)`.
It unpacks `(d, n)` and computes:
`decrypted_message = pow(ciphertext_int, d, n)`.

Step 5: Bottom demo runs.
It sets `p=61, q=53`.
It sets `original_message = 42`.
It encrypts then decrypts and prints all three values.

#Diffie-Hellman (`diffiehelman.py`) does this
This file performs a Diffie-Hellman shared secret computation.

Step 1: `is_primitive_root(g, p)` checks primitive root behavior (by brute force).
It creates `seen = set()`.
Then for i from 1 to p-1:
1. Computes `val = pow(g, i, p)`.
2. If `val` is already in `seen`, return False.
3. Else add to `seen`.
At the end it returns True only if `len(seen) == p - 1`.

Step 2: `find_primitive_root(p)` searches g.
For g in range(2, p):
It calls `is_primitive_root(g, p)`.
First g that works is returned.
If none found, it raises an error.

Step 3: `generate_dh_public_key(private_key, generator_g, prime_p)`.
It computes `pow(generator_g, private_key, prime_p)`.

Step 4: `compute_dh_shared_secret(others_public_key, my_private_key, prime_p)`.
It computes `pow(others_public_key, my_private_key, prime_p)`.

Step 5: Bottom demo shows the key exchange.
1. Sets `prime_modulus_p = 23`
2. Sets `generator_g = find_primitive_root(prime_modulus_p)`
3. Picks `alice_private_key` randomly in [1, p-2]
4. Computes `alice_public_key = generate_dh_public_key(alice_private_key, generator_g, prime_modulus_p)`
5. Picks `bob_private_key` randomly in [1, p-2]
6. Computes `bob_public_key = generate_dh_public_key(bob_private_key, generator_g, prime_modulus_p)`
7. Alice computes:
   `alice_shared_secret = compute_dh_shared_secret(bob_public_key, alice_private_key, prime_modulus_p)`
8. Bob computes:
   `bob_shared_secret = compute_dh_shared_secret(alice_public_key, bob_private_key, prime_modulus_p)`
9. It prints both values and checks if they match.

#OTP using OS randomness (`OTP(usingtheOSlibraryinpython).py`) does this
This is a one-time-pad style XOR cipher demo.

Step 1: It defines `otp_xor(data, key)`.
It returns a bytes array where each output byte is XOR of corresponding bytes:
`bytes([b1 ^ b2 for b1, b2 in zip(data, key)])`

Step 2: It reads the message.
`message = input(...).encode()` converts the string to bytes.

Step 3: It generates a random key of the same length.
`key = os.urandom(len(message))`
So every run creates a new key.

Step 4: Encryption is XOR(message, key).
`ciphertext = otp_xor(message, key)`

Step 5: Decryption is XOR(ciphertext, key).
`decrypted = otp_xor(ciphertext, key)`
Because XORing twice cancels out.

Step 6: It prints ciphertext as hex and prints decrypted text.
It uses `ciphertext.hex()` and `decrypted.decode()`.

#OTP + PRG style keystream (`OTP+PRG.py`) does this
Despite the filename, this file builds a pseudo-random pad using AES-CTR.
It uses a password to generate the AES key via SHA-256.

Step 1: `generate_secure_keystream(password, length_in_bytes)`.
1. `key = hashlib.sha256(password.encode()).digest()`
   So the AES key is deterministic for a given password.
2. `iv = secrets.token_bytes(16)`
   So the keystream changes every run (because IV changes).
3. It creates an AES-CTR encryptor:
   `Cipher(algorithms.AES(key), modes.CTR(iv)).encryptor()`
4. It creates the keystream by encrypting zero bytes:
   `keystream = encryptor.update(b'\x00' * length_in_bytes)`
5. Returns `(iv, keystream)`.

Step 2: `xor_bytes(data, pad)`.
It XORs each data byte with the corresponding pad byte.

Step 3: Bottom code sets fixed message + password.
`message = "salam".encode()`
`password = "my_secret_password"`

Step 4: It generates keystream.
`iv, pad = generate_secure_keystream(password, len(message))`

Step 5: It encrypts by XOR.
`ciphertext = xor_bytes(message, pad)`

Step 6: It decrypts by XOR again with the same pad.
`decrypted = xor_bytes(ciphertext, pad)`

Step 7: It prints original, ciphertext hex, and decrypted string.

#CPA-secure OTP-like stream cipher (`cpasecureotp.py`) does this
This file implements a stream cipher where the pad is generated using AES as a PRF over counter blocks.

Step 1: `prf_f(key, x)` generates one PRF output block.
1. It creates an AES-ECB encryptor:
   `Cipher(algorithms.AES(key), modes.ECB()).encryptor()`
2. It returns:
   `block_function.update(x) + block_function.finalize()`
So `x` is a 16-byte input block and the output is 16 bytes.

Step 2: `cpa_encrypt(key, message)`.
1. Generate random `iv = secrets.token_bytes(16)`
2. Set `full_pad = b""` (this will become the whole keystream)
3. Compute number of 16-byte blocks needed:
   `num_blocks = (len(message) + 15) // 16`
4. Convert IV to an integer: `iv_int = int.from_bytes(iv, "big")`
5. For i in `range(num_blocks)`:
   - Compute `counter_block = ((iv_int + i) % (2**128)).to_bytes(16, "big")`
   - Append PRF output: `full_pad += prf_f(key, counter_block)`
6. XOR only as many bytes as the message has:
   `ciphertext = bytes([m ^ p for m, p in zip(message, full_pad)])`
7. Return `(iv, ciphertext)`

Step 3: `cpa_decrypt(key, iv, ciphertext)`.
It regenerates the exact same `full_pad`:
1. Same IV integer conversion `iv_int = int.from_bytes(iv, "big")`
2. Same `num_blocks` computed from ciphertext length
3. Same counter block loop and `full_pad += prf_f(...)`
Then it XORs ciphertext with pad again:
`return bytes([c ^ p for c, p in zip(ciphertext, full_pad)])`

Step 4: Bottom demo runs.
It creates random `secret_key = secrets.token_bytes(16)`.
It sets `long_message = b"My name is Emin, dont tell anyone"`.
It encrypts, decrypts, prints whether it matches, and prints the decrypted text.

#Blum-Micali PRG (`prgwithdiscrete.py`) does this
This file generates pseudo-random bits using Blum-Micali style updates.

Step 1: `is_primitive_root(g, p)` does a limited check.
It returns False if `g < 2`.
It computes `q = (p - 1) // 2`.
It then checks:
1. If `pow(g, 2, p) == 1`, it returns False
2. If `pow(g, q, p) == 1`, it returns False
3. Otherwise returns True.
So it is a simplified check (not the full primitive-root verification).

Step 2: `blum_micali_prg(seed, p, g, length)`.
1. If `g` is not a primitive root, it prints a warning.
2. It sets `value = seed % (p - 1)`.
3. If `value == 0`, it changes it to 1.
4. Sets `bitstream = []` and `limit = (p - 1) // 2`.
5. For each output bit position (range `length`):
   - Updates `value = pow(g, value, p)`
   - Outputs `bit = 1 if value > limit else 0`
   - Appends the bit to `bitstream`
6. Returns the list of bits.

Step 3: Bottom code tests it.
It sets `P=503`, `G=5`, `SEED=123`, `L=50`.
It prints the generated bits as a string.
Then it counts ones and zeros with:
`ones = bit_string.count('1')`
`zeros = bit_string.count('0')`
and prints those stats.

#Key builder script (`encryption.py`) does this
This file is a random “key string builder” using ASCII codes.

Step 1: It defines variables.
It sets `code = ""`, `end = ""`.
It sets `letter = "abcdefjghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"`.

Step 2: It loops through every character `i` in `letter`.
For each `i`:
1. It picks `number = randint(35, 99)`.
2. It appends `str(ord(i) + number)` to `code`.
3. It appends `str(number)` to `end`.

Step 3: It builds the final key.
`key = code + "898989" + end`

Step 4: It prints `key`.

#Dependencies note
`cpasecureotp.py` uses `cryptography` (AES, ECB).
`OTP+PRG.py` uses `cryptography` (AES, CTR).
