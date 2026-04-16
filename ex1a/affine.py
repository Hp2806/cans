def mod_inverse(a):
    a = a % 26
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None
def process_affine(text, a, b, is_encrypt=True):
    result = ""
    a_inv = mod_inverse(a)
    if a_inv is None:
        return "Error: Key A must be coprime with 26"
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            x = ord(ch) - base
            if is_encrypt:
                y = (a * x + b) % 26
            else:
                y = (a_inv * (x - b)) % 26
            result += chr(y + base)
        else:
            result += ch
    return result
if __name__ == "__main__":
    print("--- Affine Cipher---")
    msg = input("Enter message: ")
    key_a = int(input("Enter Key A: "))
    key_b = int(input("Enter Key B: "))
    encrypted = process_affine(msg, key_a, key_b, is_encrypt=True)
    print(f"\nEncrypted: {encrypted}")
    decrypted = process_affine(encrypted, key_a, key_b, is_encrypt=False)
    print(f"Decrypted: {decrypted}")
