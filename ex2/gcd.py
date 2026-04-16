def find_gcd_with_steps(a, b):
    a, b = abs(a), abs(b)
    
    if a == 0 or b == 0:
        return a if a != 0 else b

    gcd = 1
    limit = min(a, b)
    
    print(f"\n--- Steps for GCD({a}, {b}) ---")
    
    for i in range(1, limit + 1):
        rem_a = a % i
        rem_b = b % i
        
        if rem_a == 0 and rem_b == 0:
            gcd = i
            print(f"Check {i}: {a}%{i}=0 and {b}%{i}=0. YES (Current GCD: {gcd})")
        else:
            reason = []
            if rem_a != 0: reason.append(f"{a}%{i}={rem_a}")
            if rem_b != 0: reason.append(f"{b}%{i}={rem_b}")
            print(f"Check {i}: {' and '.join(reason)}. NO")
    return gcd
if __name__ == "__main__":
    print("--- Brute Force GCD ---")
    val1 = input("Enter first number: ")
    val2 = input("Enter second number: ")
    
    if val1.isdigit() and val2.isdigit():
        num1 = int(val1)
        num2 = int(val2)
        
        result = find_gcd_with_steps(num1, num2)
        
        print("-" * 30)
        print(f"FINAL RESULT: {result}")
    else:
        print("Invalid input. Please enter integers.")
