from typing import Mapping

def get_letter_map(words):
    dict = {}
    for letter in list(words):
        dict[letter] = asd[letter.lower()]
    return dict

def affine_cipher(mul, offset, plain_map):
    newstring = ""
    for k, v in plain_map.items():
        val2 = ((v * mul) + offset) % 26
        newstring += dsa[val2].upper()
    return newstring

def affine_decrypt(mul, add, key):
    decryption = ""
    inverse_mul = abs(mul - 26)
    for letter in list(key):
        decrypt_letter = (inverse_mul * (asd[letter.lower()]-add)) % 26
        decryption += dsa[decrypt_letter].upper()
    return decryption

def encrypt():
     for i in range(0, 10000):
        for j in range(0, 26):

            res = affine_cipher(i,j, plain_map)
            #print(res)
            if res == ciphertext:
                print(i, j)
                break

def decrypt():
     for i in range(0, 10000):
        for j in range(0, 26):

            res = affine_decrypt(i,j, ciphertext)
            #print(res)
            if res == plaintext:
                print("RESULT ",i, j)
                break

if __name__ == "__main__":
    asd = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25
}
    dsa = {
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
    8:'i',
    9:'j',
    10:'k',
    11:'l',
    12:'m',
    13:'n',
    14:'o',
    15:'p',
    16:'q',
    17:'r',
    18:'s',
    19:'t',
    20:'u',
    21:'v',
    22:'w',
    23:'x',
    24:'y',
    25:'z'
}
    plaintext = "SURFACE"
    ciphertext = "NJCAXTP"
    plain_map = get_letter_map(plaintext)
    print(plain_map)

    print(affine_cipher(5,3,get_letter_map("CRYPTO")) == "NKTAUV")
    print(affine_decrypt(5, 3, "NKTAUV"))

    print(affine_decrypt(7, 23, ciphertext))
    #decrypt()

    # Task 4
    plain_map = get_letter_map("GLORY")
    for value in plain_map.values():
        print(bin(value))


    glory =          "0011001011011101000111000"
    glory_ciphered = "1010100011111111010111011"

    dough =                  "0001101110101000011000111"
    dough_ciphered_certain = "1000000110001010001000100"

    # get the cipher
    cipher = ""
    for i in range(0, len(dough)):
        cipher += "1" if bool(dough[i] == "1") != bool(dough_ciphered_certain[i] == "1") else "0"
    print("CIPHER", cipher)

    # Use cipher to extract OTP string.
    ciphering_word = ""
    for i in range(0, len(dough)):
        ciphering_word += "1" if bool(glory[i] == "1") != bool(cipher[i] == "1") else "0"
    print()
    print(ciphering_word)

    # print(dough_ciphered_certain) # Add value to validate against if needed.
