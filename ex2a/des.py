S0 = [[1, 0, 3, 2], [3, 2, 1, 0],[0, 2, 1, 3], [3, 1, 3, 2]
]
S1 = [
    [0, 1, 2, 3],[2, 0, 1, 3], [3, 0, 1, 0],[2, 1, 0, 3]
]
P10 =[3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  =[6, 3, 7, 4, 8, 5, 10, 9]
P4  = [2, 4, 3, 1]
IP  =[2, 6, 3, 1, 4, 8, 5, 7]
IP_INV =[4, 1, 3, 5, 7, 2, 8, 6]
EP  =[4, 1, 2, 3, 2, 3, 4, 1]
def permute(bits, table):
    return "".join(bits[i - 1] for i in table)
def xor(a, b):
    return "".join("0" if x == y else "1" for x, y in zip(a, b))
def left_shift(bits, n):
    return bits[n:] + bits[:n]
def s_box(bits, box):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(box[row][col], '02b')
def round_func(bits, key, round_num):
    L = bits[:4]
    R = bits[4:]
    print(f"\nRound {round_num}:")
    print(f"L = {L}, R = {R}")
    ep = permute(R, EP)
    print(f"EP(R) = {ep}")
    x = xor(ep, key)
    print(f"XOR with subkey = {x}")
    s0 = s_box(x[:4], S0)
    s1 = s_box(x[4:], S1)
    print(f"S-Box outputs -> S0={s0}, S1={s1}")
    p4 = permute(s0 + s1, P4)
    print(f"P4 = {p4}")
    new_L = xor(L, p4)
    print(f"New Left = L XOR P4 = {new_L}")
    return new_L + R
def run_sdes(pt, key):
    print("\n==============")
    print("S-DES ENCRYPTION ")
    print("================")
    print("\n--- KEY GENERATION ---")
    print(f"Original 10-bit Key: {key}")
    p10_key = permute(key, P10)
    print(f"After applying P10: {p10_key}")
    L, R = p10_key[:5], p10_key[5:]
    print(f"Split into halves -> L={L}, R={R}")
    L, R = left_shift(L, 1), left_shift(R, 1)
    print(f"Left shift by 1 -> L={L}, R={R}")
    k1 = permute(L + R, P8)
    print(f"Apply P8 -> Subkey K1 = {k1}")
    L, R = left_shift(L, 2), left_shift(R, 2)
    k2 = permute(L + R, P8)
    print(f"Left shift by 2 and apply P8 -> Subkey K2 = {k2}")
    print("\n--- ENCRYPTION ---")
    ipt = permute(pt, IP)
    print(f"Initial Permutation IP(PT) = {ipt}")
    r1 = round_func(ipt, k1, 1)
    sw = r1[4:] + r1[:4]
    print(f"\nSwap halves -> {sw}")
    r2 = round_func(sw, k2, 2)
    cipher = permute(r2, IP_INV)
    print("\nApply IP")
    print(f"Final Ciphertext = {cipher}\n")
if __name__ == "__main__":
    print("=== S-DES Encryption ===")
    while True:
        plaintext = input("Enter 8-bit Plaintext: ").strip()
        if len(plaintext) == 8 and all(c in '01' for c in plaintext):
            break
        print("Error: Plaintext must be exactly 8 characters of 0s and 1s. Try again.\n")
    while True:
        key_input = input("Enter 10-bit Key: ").strip()
        if len(key_input) == 10 and all(c in '01' for c in key_input):
            break
        print("Error: Key must be exactly 10 characters of 0s and 1s. Try again.\n")
    print("\nStarting Encryption...")
    run_sdes(plaintext, key_input)
