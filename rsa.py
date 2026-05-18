import math
# Extended Euclidean Algorithm
# def mod_inverse(e, phi):
#     def egcd(a, b):
#         if a == 0:
#             return b, 0, 1
#         g, y, x = egcd(b % a, a)
#         return g,x - (b // a) * y,y
#     g, x, _ = egcd(e, phi)
#     return x % phi

# Input
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
file = input("Enter file name: ")

# Read Text File
with open(file, "r") as f:
    text = f.read()

# RSA Setup
n = p * q
phi = (p - 1) * (q - 1)

# Choose e
e = 2
while math.gcd(e, phi) != 1:
    e += 1

# Find d
d = pow(e, -1, phi)
# for i in range(phi):
#     if (e * i) % phi == 1:
#         d = i
#         break

# Encryption
encrypted = []
for ch in text:
    encrypted.append(pow(ord(ch), e, n))

# Decryption
decrypted = ""
for c in encrypted:
    decrypted += chr(pow(c, d, n))


# Output
print("\nPublic Key :", (e, n))
print("Private Key:", (d, n))
print("\nOriginal Text:")
print(text)
print("\nEncrypted Text:")
print(encrypted)
print("\nDecrypted Text:")
print(decrypted)
