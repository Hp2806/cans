def find_gcd_with_steps(a, b):
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
        
    print(f"\n--- Step for GCD({a}, {b}) ---")
    
    while a != 0:
        quotient = b // a
        remainder = b % a
        print(f"{b} = ({quotient} * {a}) + {remainder}")
        
        # Update values for the next step
        b = a
        a = remainder
        
    print(f"The remainder is now 0. GCD is: {b}")
    return b

if __name__ == "__main__":
    print("--- Euclidean GCD Finder ---")
    val1 = input("Enter first number: ")
    val2 = input("Enter second number: ")
    
    try:
        num1 = int(val1)
        num2 = int(val2)
        
        result = find_gcd_with_steps(num1, num2)
        
        print("-" * 35)
        print(f"FINAL RESULT: {result}")
        
    except ValueError:
        print("Error: Please enter valid integers only.")
