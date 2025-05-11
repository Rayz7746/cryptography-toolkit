"""
RC4 Keystream Generator
-----------------------
This program demonstrates the keystream generation component of the RC4 stream cipher algorithm.

The RC4 (Rivest Cipher 4) keystream generation works by:
1. Taking user input for RC4 parameters and key
2. Initializing a state array based on the secret key
3. Generating a pseudorandom keystream

Usage:
- Ensure rc4.py is in the same directory
- Run: python q1a.py
- Enter requested parameters when prompted

Parameters:
- n: Bit processing size (determines S-box size as 2^n)
- l: Length of keystream to generate
- key: Secret key as space-separated bits (must be divisible by n)

Example:
- Enter n: 3
- Enter l: 11
- Enter key as bit array: 0 1 1 0 0 1 1 0 0 1 1 1 1 0 1
- This converts to key_decimal = [3, 1, 4, 7, 5]

The program performs the following steps:
1. Validates user input
2. Converts bit array to integer representation
3. Initializes the RC4 cipher with provided parameters
4. Generates a keystream
5. Displays the keystream in binary format

"""

from rc4 import rc4, DecimalToBinary, ConvertBitArraytoInt


# Main function to run RC4 with user inputs
def main():
    n = int(input("Enter n (parameter for RC4, determines S-box size 2^n): "))
    l = int(input("Enter l (length of plaintext/ciphertext in characters): "))
    key_bits_str = input("Enter key as bit array (space-separated 0s and 1s): ")
    key_bits = [int(bit) for bit in key_bits_str.split()]
    
    # Check if bit array length is a multiple of n
    if len(key_bits) % n != 0:
        print(f"Error: The length of the bit array must be a multiple of n.")
        return
    
    # Convert bit array to decimal values
    key_decimal = ConvertBitArraytoInt(key_bits, n)
    
    cipher = rc4(n, l, key_decimal)
    keyde = cipher.gen()
    
    # Convert to binary representation and print final result
    keybi = cipher.biresult(keyde)
    print(keybi)

if __name__ == "__main__":
    main()



# - Enter n: 3
# - Enter l: 11
# - Enter key as bit array: 0 1 1 0 0 1 1 0 0 1 1 1 1 0 1
# This converts to key_decimal = [3, 1, 4, 7, 5]