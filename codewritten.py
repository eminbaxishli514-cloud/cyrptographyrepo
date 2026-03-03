#A simple python script to attack the ceaser ciphers in English.
letter_frequencies = {
    'a': 0.082,
    'b': 0.015,
    'c': 0.028,
    'd': 0.043,
    'e': 0.127,
    'f': 0.022,
    'g': 0.020,
    'h': 0.061,
    'i': 0.070,
    'j': 0.0016,
    'k': 0.0077,
    'l': 0.040,
    'm': 0.024,
    'n': 0.067,
    'o': 0.075,
    'p': 0.019,
    'q': 0.0012,
    'r': 0.060,
    's': 0.063,
    't': 0.091,
    'u': 0.028,
    'v': 0.0098,
    'w': 0.024,
    'x': 0.0015,
    'y': 0.020,
    'z': 0.00074
}
#The variable above stores the frequency of letters in the English language.
our_frequencies = {

}
#The variable above will store the frequency of charcaters in our ciphertext
cipher_text = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds"
for i in cipher_text:
    if i not in our_frequencies:
        our_frequencies[i] = 1
    else:
        our_frequencies[i]+=1
#The loop above just finds the number of occurences of each letter in cipher
length = len(cipher_text)
for i in our_frequencies:
    our_frequencies[i] = our_frequencies[i]/length
"""print(our_frequencies)"""
#This loop takes the number of occurences and divides it by the length of the cipher to find the frequency
"""for i in our_frequencies:
    print(f"{i}: {our_frequencies[i]}\n")"""
#Printing the frequencies in a clean way
letters = []
letter_values = []
cipher_chars = []
cipher_values = []
# FIX 1: Use sorted() with a key to avoid duplicate letters and nested loops
letters = sorted(letter_frequencies, key=letter_frequencies.get, reverse=True)
cipher_chars = sorted(our_frequencies, key=our_frequencies.get, reverse=True)
print(letters)
print(cipher_chars)

letter_to_index = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def difference(a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    first_index = 0
    second_index = 0
    for i in range(len(alphabet)):
        if alphabet[i] == a:
            first_index = i
        if alphabet[i] == b:
            second_index = i
    return (first_index - second_index) % 26


differences = []
for i in range(len(cipher_chars)):
    differences.append(difference(cipher_chars[i],letters[i]))
print(differences)
#As we can see, we do not have a definite answer from this list,
#but the most frequent numbers in that list have a higher probability of being our key
#So, I will just write the decryption logic and a loop to go through
#and let's hope that we will get the human-readable text
#This shows the limitation of the letter frequency analysis in short texts
#as we can not get a definite result
"""
First we note that the brute-force attack from above treats the cipher as a black box,
i.e., we do not analyze the internal structure of the cipher. The substitution cipher
can easily be broken by such an analytical attack.
The major weakness of the cipher is that each plaintext symbol always maps to
the same ciphertext symbol. That means that the statistical properties of the plaintext
are preserved in the ciphertext. If we go back to the second example we observe that
the letter q occurs most frequently in the text. From this we know that q must be the
substitution for one of the frequent letters in the English language.
For practical attacks, the following properties of language can be exploited:
1. Determine the frequency of every ciphertext letter. The frequency distribution,
often even of relatively short pieces of encrypted text, will be close to that of
the given language in general. In particular, the most frequent letters can often
easily be spotted in ciphertexts. For instance, in English E is the most frequent
letter (about 13%), T is the second most frequent letter (about 9%), A is the third
most frequent letter (about 8%), and so on. Table 1.1 lists the letter frequency
distribution of English.
!!!!(This is a quote from understanding cryptography book)




"""
def finder(a,b):
    for i in range(len(a)):
        if a[i] == b:
            return i

def decyrpt(ciphertext,key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in ciphertext:
        if i in letters:
            number = finder(letters,i)
            result = result + letters[(number-key)%26]
        else:
            result = result + i
    return result

for i in differences:
    print(f"{decyrpt(cipher_text,i)}\n")

#As you can see, the first and second line shows
#ifweallunitewewillcausetheriverstostainthegreatwaterswiththeirblood
"""

If we all unite, we will cause the rivers to stain the great waters with their blood."""


"""
What this basically means that in short texts, even though we
can not get the exact key using the letter-frequency analysis immediately using a simple script
we will get a list of most probable keys using it

We could enhance the script to be more accurate but it is already strong enough






