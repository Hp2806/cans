import random
def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res
def miller_test(d, n):
    a = random.randint(2, n - 2)
    x = power(a, d, n)
    print(f"a={a}, x={x}", end="")
    if x == 1 or x == n - 1:
        print(" -> OK")
        return True
    temp_d = d
    while temp_d != n - 1:
        x = (x * x) % n
        temp_d *= 2
        print(f" -> x={x}", end="")
        if x == n - 1:
            print(" -> OK")
            return True
        if x == 1:
            print(" -> FAIL")
            return False
    print(" -> FAIL")
    return False
def is_prime(n, k=3):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    print(f"n-1 = 2^{r} * {d}")
    for i in range(k):
        print(f"Step {i+1}: ", end="")
        if not miller_test(d, n):
            return False
    return True
if __name__ == "__main__":
    val = input("Enter number: ")
    if val.isdigit():
        num = int(val)
        result = is_prime(num)
        print("-" * 20)
        print(f"RESULT: {num} {'is PRIME' if result else 'is COMPOSITE'}")
    else:
        print("Invalid input.")
