"""
Binary Arithmetic and Modular Operations Library
===============================================

This script implements various binary arithmetic operations and modular arithmetic functions,
providing a comprehensive toolkit for binary number manipulation.

Description:
-----------
This library provides implementations of standard arithmetic operations for binary numbers
represented as strings, as well as modular arithmetic operations commonly used in
cryptography and number theory. Each function includes time complexity analysis in both
binary representation length (n) and decimal value (N) terms.

Components:
----------
1. Basic Binary Arithmetic:
   - Addition: Adds two binary numbers
   - Subtraction: Subtracts one binary number from another
   - Multiplication: Multiplies two binary numbers
   - Division: Divides binary numbers with quotient and remainder

2. Modular Arithmetic Operations:
   - Modular Addition: Calculates (a + b) % modulus
   - Modular Subtraction: Calculates (a - b) % modulus
   - Modular Multiplication: Calculates (a * b) % modulus
   - Modular Exponentiation: Calculates (base^exponent) % modulus
   - Modular Inverse: Finds the modular multiplicative inverse

3. Number Theory Utilities:
   - Extended Euclidean Algorithm: Computes GCD and Bézout coefficients
   - Recursive Binary Division: Implements division through recursive bit operations
"""


def binary_addition(a, b):
    """
    Add two binary numbers represented as strings.
    Returns the result as a binary string.
    
    Time complexity:
    - O(n) where n is the length of the binary representation
    - O(log N) where N is the decimal number
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Add integers and convert back to binary string
    result = int_a + int_b
    return bin(result)[2:]  # Remove '0b' prefix

def binary_subtraction(a, b):
    """
    Subtract binary number b from a, both represented as strings.
    Returns the result as a binary string.
    
    Time complexity:
    - O(n) where n is the length of the binary representation
    - O(log N) where N is the decimal number
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Subtract integers and convert back to binary string
    result = int_a - int_b
    if result < 0:
        # Handle negative results
        return "-" + bin(abs(result))[2:]
    return bin(result)[2:]  # Remove '0b' prefix

def binary_multiplication(a, b):
    """
    Multiply two binary numbers represented as strings.
    Returns the result as a binary string.
    
    Time complexity:
    - O(n²) using the standard multiplication algorithm
    - O(log² N) where N is the decimal number
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Multiply integers and convert back to binary string
    result = int_a * int_b
    return bin(result)[2:]

def binary_division(a, b):
    """
    Divide binary number a by b, both represented as strings.
    Returns a tuple with quotient and remainder as binary strings.
    
    Time complexity:
    - O(n²) using the recursive binary division algorithm
    - O(log² N) where N is the decimal number
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    if int_b == 0:
        raise ValueError("Division by zero")
    
    # Call recursive division helper function
    quotient, remainder = recursive_divide(int_a, int_b)
    
    # Convert results back to binary strings
    return bin(quotient)[2:], bin(remainder)[2:]

def recursive_divide(x, y):
    """
    Recursive binary division algorithm.
    Takes two integers x and y, returns quotient and remainder as integers.
    """
    # Base case
    if x == 0:
        return 0, 0
    
    # Recursive case: divide x//2 by y
    q_prime, r_prime = recursive_divide(x >> 1, y)
    
    # Calculate q and r
    q = q_prime << 1  # q = 2q'
    r = r_prime << 1  # r = 2r'
    
    # If x is odd, increment r
    if x & 1:
        r += 1
    
    # If remainder >= divisor, subtract divisor from remainder and increment quotient
    if r >= y:
        r -= y
        q += 1
    
    return q, r

def modular_exponentiation(base, exponent, modulus):
    """
    Calculate (base^exponent) % modulus efficiently.
    All inputs and outputs are binary strings.
    
    Time complexity:
    - O(n³) where n is the length of the binary representation of the exponent
    - O(log³ N) where N is the decimal value of the exponent
    """
    if modulus == "0":
        raise ValueError("Modulus cannot be 0")
    
    # Convert binary strings to integers
    base_int = int(base, 2)
    exp_int = int(exponent, 2)
    mod_int = int(modulus, 2)
    
    # Perform modular exponentiation
    result = 1
    base_int = base_int % mod_int
    
    while exp_int > 0:
        # If exponent is odd, multiply result with base
        if exp_int & 1:
            result = (result * base_int) % mod_int
        
        # Square the base
        base_int = (base_int * base_int) % mod_int
        
        # Divide exponent by 2
        exp_int >>= 1
    
    return bin(result)[2:]

def modular_addition(a, b, modulus):
    """
    Calculate (a + b) % modulus.
    All inputs and outputs are binary strings.
    
    Time complexity:
    - O(n) where n is the length of the binary representation
    - O(log N) where N is the decimal number
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    int_mod = int(modulus, 2)
    
    # Perform modular addition
    result = (int_a + int_b) % int_mod
    
    return bin(result)[2:]

def modular_subtraction(a, b, modulus):
    """
    Calculate (a - b) % modulus.
    All inputs and outputs are binary strings.
    
    Time complexity:
    - O(n) where n is the length of the binary representation
    - O(log N) where N is the decimal number
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    int_mod = int(modulus, 2)
    
    # Perform modular subtraction
    result = (int_a - int_b) % int_mod
    
    return bin(result)[2:]

def modular_multiplication(a, b, modulus):
    """
    Calculate (a * b) % modulus.
    All inputs and outputs are binary strings.
    
    Time complexity:
    - O(n²) for the multiplication part
    - O(log² N) where N is the decimal number
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    int_mod = int(modulus, 2)
    
    # Perform modular multiplication
    result = (int_a * int_b) % int_mod
    
    return bin(result)[2:]

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm to find gcd and coefficients.
    Returns (gcd, x, y) such that ax + by = gcd.
    
    Time complexity:
    - O(n³) where n is the length of the binary representation
    - O(log³ N) where N is the decimal number
    """
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

def modular_inverse(a, modulus):
    """
    Calculate the modular inverse of a under the modulus.
    All inputs and outputs are binary strings.
    
    Time complexity:
    - O(n³) for the extended GCD algorithm
    - O(log³ N) where N is the decimal number
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_mod = int(modulus, 2)
    
    # Check if inverse exists
    gcd, x, y = extended_gcd(int_a, int_mod)
    
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist (gcd={gcd})")
    
    # Make sure we get a positive result
    result = (x % int_mod + int_mod) % int_mod
    
    return bin(result)[2:]