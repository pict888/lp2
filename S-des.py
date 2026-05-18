# Simplified DES (S-DES)
IP  = [1,5,2,0,3,7,4,6]
IP1 = [3,0,2,4,6,1,7,5]

EP  = [3,0,1,2,1,2,3,0]

P4  = [1,3,2,0]

S0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]

S1 = [
    [0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]
]

# Permutation
def permute(bits, table):
    return [bits[i] for i in table]

# XOR
def XOR(a, b):
    return [ a[i] ^ b[i] for i in range(len(a))]

# S-Box
def sbox(bits, box):

    row = (bits[0] << 1) + bits[3]
    col = (bits[1] << 1) + bits[2]
    val = box[row][col]
    return [ (val >> 1) & 1, val & 1]

# fk Function
def fk(bits, key):
    L = bits[:4]
    R = bits[4:]
    ep = permute(R, EP)
    x = XOR(ep, key)
    left  = x[:4]
    right = x[4:]
    s0 = sbox(left, S0)
    s1 = sbox(right, S1)
    p4 = permute(s0 + s1, P4)
    newL = XOR(L, p4)
    return newL + R

# Swap
def swap(bits):
    return bits[4:] + bits[:4]

# Encrypt
def encrypt(text, K1, K2):
    print("\nAfter IP:")
    text = permute(text, IP)
    print(text)
    print("\nRound 1")
    text = fk(text, K1)
    print(text)
    text = swap(text)
    print("\nAfter Swap")
    print(text)
    print("\nRound 2")
    text = fk(text, K2)
    print(text)
    text = permute(text, IP1)
    return text

# Decrypt
def decrypt(text, K1, K2):
    text = permute(text, IP)
    text = fk(text, K2)
    text = swap(text)
    text = fk(text, K1)
    text = permute(text, IP1)
    return text

# Convert string to bits
def strToBits(s):
    return [int(x) for x in s]

# MAIN
# MAIN
keyStr = input("Enter 10-bit Key: ")
plainStr = input("Enter 8-bit Plaintext: ")
key = strToBits(keyStr)
plain = strToBits(plainStr)

# Generate Keys
K1, K2 = generateKeys(key)
print("\nK1 =", K1)
print("K2 =", K2)

# Encryption
cipher = encrypt(plain, K1, K2)
print("\nEncrypted Text:")
print(cipher)

# Decryption
text = decrypt(cipher, K1, K2)
print("\nDecrypted Text:")
print(text)
