def generate_matrix(key):
    key = key.upper().replace("J", "I")
    key = "".join([c for c in key if c.isalpha()])
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    combined = key + alphabet
    used = []
    for char in combined:
        if char not in used:
            used.append(char)
    matrix = [used[i:i + 5] for i in range(0, 25, 5)]
    return matrix
def prepare_text(text, is_encrypt):
    cleaned = "".join([c for c in text.upper().replace("J", "I") if c.isalpha()])
    if not is_encrypt:
        return cleaned
    result = ""
    i = 0
    while i < len(cleaned):
        result += cleaned[i]
        if i + 1 < len(cleaned):
            if cleaned[i] == cleaned[i+1]:
                result += "X"
                i += 1
            else:
                result += cleaned[i+1]
                i += 2
        else:
            result += "X"
            i += 1
    return result
def find_pos(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return 0, 0
def process_playfair(text, key, is_encrypt=True):
    if not key or not text:
        return "Error: Missing input."
    matrix = generate_matrix(key)
    prepared = prepare_text(text, is_encrypt)
    
    if not is_encrypt and len(prepared) % 2 != 0:
        return "Invalid Ciphertext length."
    output = ""
    shift = 1 if is_encrypt else 4 
    for i in range(0, len(prepared), 2):
        a, b = prepared[i], prepared[i+1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2: 
            output += matrix[r1][(c1 + shift) % 5]
            output += matrix[r2][(c2 + shift) % 5]
        elif c1 == c2: 
            output += matrix[(r1 + shift) % 5][c1]
            output += matrix[(r2 + shift) % 5][c2]
        else: 
            output += matrix[r1][c2]
            output += matrix[r2][c1]
    if not is_encrypt:
        cleaned_output = ""
        for j in range(len(output)):
            if output[j] == "X" and j > 0 and j < len(output)-1:
                if output[j-1] == output[j+1]:
                    continue
            cleaned_output += output[j]
        if cleaned_output.endswith("X"):
            cleaned_output = cleaned_output[:-1]
        output = cleaned_output
    return output, matrix
if __name__ == "__main__":
    print("--- Playfair Cipher ---")
    msg = input("Enter message: ")
    keyword = input("Enter keyword: ")
    encrypted, matrix = process_playfair(msg, keyword, is_encrypt=True)
    print("\nKey Matrix:")
    for row in matrix:
        print("  ".join(row))
    print(f"\nEncrypted: {encrypted}")
    decrypted, _ = process_playfair(encrypted, keyword, is_encrypt=False)
    print(f"Decrypted: {decrypted}")
