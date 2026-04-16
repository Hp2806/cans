text = input("Enter message: ").upper()
key = input("Enter keyword: ").upper()
print("\n---- Encryption ----" )
encrypted = ""
for i in range(len(text)):
    char = text[i]
    if char.isalpha():
        key_char = key[i % len(key)]
        shift = ord(key_char) - ord('A')
        x = ord(char) - ord('A')
        encrypted += chr(((x + shift) % 26) + ord('A'))
    else:
        encrypted += char
print("Encrypted text:", encrypted)
print("\n---- Decryption ----")
decrypted = ""
for i in range(len(encrypted)):
    char = encrypted[i]
    if char.isalpha():
        key_char = key[i % len(key)]
        shift = ord(key_char) - ord('A')
        y = ord(char) - ord('A')
        decrypted += chr(((y - shift) % 26) + ord('A'))
    else:
        decrypted += char

print("Decrypted text:", decrypted)
