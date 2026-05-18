P10 = [3,5,2,7,4,10,1,9,8,6]    # 1-10 no dups
P8  = [6,3,7,4,8,5,10,9]        # 3-10 no dups

IP  = [2,6,3,1,4,8,5,7]         # 1-8 no dups
IP1 = [4,1,3,5,7,2,8,6]         # inv of IP

EP  = [4,1,2,3,2,3,4,1]         # 1-4 dup once
P4  = [2,4,3,1]                 # 1-4 no dup

S0 = [                          # 4x 0-3 maybe dup
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]

S1 = [                          # 4x 0-3 maybe dup
    [0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]
]

# Permutation
def perm(bits, table):
    result = []
    for i in table:
        result.append(bits[i-1])
    return result

# XOR
def xor(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x ^ y)
    return result

# Left Rotate
def rot(bits, n):
    return bits[n:] + bits[:n]

# S-Box
def sbox(bits, box):
    row = (bits[0] << 1) + bits[3]
    col = (bits[1] << 1) + bits[2]
    value = box[row][col]
    return [value // 2, value % 2]

# Generate Keys
def keys(key):
    key = perm(key, P10)
    L = key[:5]
    R = key[5:]
    L = rot(L, 1)
    R = rot(R, 1)
    K1 = perm(L + R, P8)
    L = rot(L, 2)
    R = rot(R, 2)
    K2 = perm(L + R, P8)
    return K1, K2

# fk Function
def fk(bits, key):
    L = bits[:4]
    R = bits[4:]
    ep = perm(R, EP)
    x = xor(ep, key)
    left  = x[:4]
    right = x[4:]
    s0 = sbox(left, S0)
    s1 = sbox(right, S1)
    p4 = perm(s0 + s1, P4)
    newL = xor(L, p4)
    return newL + R

# Encryption / Decryption
def run(bits, K1, K2):
    bits = perm(bits, IP)
    bits = fk(bits, K1)
    bits = bits[4:] + bits[:4]
    bits = fk(bits, K2)
    bits = perm(bits, IP1)
    return bits

# Convert String to Bits
def strToBits(s):
    bits = []
    for x in s:
        bits.append(int(x))
    return bits

# MAIN
keyStr = input("Enter 10-bit Key: ")
plainStr = input("Enter 8-bit Plaintext: ")
key = strToBits(keyStr)
plain = strToBits(plainStr)
# Generate K1 and K2
K1, K2 = keys(key)
# Encryption
cipher = run(plain, K1, K2)
# Decryption
text = run(cipher, K2, K1)
print("\nK1 =", K1)
print("K2 =", K2)
print("\nEncrypted:", cipher)
print("Decrypted:", text)
