p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))
n = p * q
print("n =", n)
phi = (p - 1) * (q - 1)
print("phi(n) =", phi)
e = int(input("Enter public key (e) such that gcd(e, phi) = 1: "))
for i in range(1, phi):
    if (i * e) % phi == 1:
        d = i
        break
print("Private key (d) =", d)
print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
M = int(input("\nEnter message (integer less than n): "))
C = pow(M, e, n)
print("Encrypted message:", C)
decrypted = pow(C, d, n)
print("Decrypted message:", decrypted)
