# SHA-3 Test Script
# ----------------------------
# This script tests the SHA-3 hash function implementation by validating each transformation step and the complete process.
# Description:
# This test harness validates a SHA-3 (Secure Hash Algorithm 3) implementation by testing each
# transformation function individually and then the complete algorithm. The script:
# - Loads test vector data from an input file
# - Tests each transformation function separately:
# * θ (theta): Diffusion function that mixes columns
# * ρ (rho): Rotation function that provides inter-slice diffusion
# * π (pi): Permutation function that rearranges bits
# * χ (chi): Non-linear function using bitwise operations
# - Tests the complete F function with all 24 rounds
# Each test extracts specific bits from the state array (position [4][3][9...18])
# and compares them against expected output values to verify correct implementation.
# This ensures each component of the SHA-3 algorithm functions as specified in the standard.
# This test script is designed to confirm that the underlying SHA-3 implementation
# in the f_function module meets the cryptographic requirements of the algorithm.

from f_function import SHA3

# Load input data
with open('sha3in.txt', 'r') as file:
    content = file.read()
    v = []
    for char in content:
        v.append(int(char))

# Initialize SHA3
sha3 = SHA3(v)

# Test theta function
print("Testing theta function:")
a_out = sha3.theta()
print("aout[4][3][9...18]: ", end="")
for k in range(9, 19):
    print(a_out[4][3][k], end="")
print("\nExpected: 0011011000")

# Reset SHA3 for next test
sha3 = SHA3(v)

# Test rho function
print("\nTesting rho function:")
a_out = sha3.rho()
print("aout[4][3][9...18]: ", end="")
for k in range(9, 19):
    print(a_out[4][3][k], end="")
print("\nExpected: 0110011001")

# Reset SHA3 for next test
sha3 = SHA3(v)

# Test pi function
print("\nTesting pi function:")
a_out = sha3.pi()
print("aout[4][3][9...18]: ", end="")
for k in range(9, 19):
    print(a_out[4][3][k], end="")
print("\nExpected: 0110110001")

# Reset SHA3 for next test
sha3 = SHA3(v)

# Test chi function
print("\nTesting chi function:")
a_out = sha3.chi()
print("aout[4][3][9...18]: ", end="")
for k in range(9, 19):
    print(a_out[4][3][k], end="")
print("\nExpected: 0110100001")


# Reset SHA3 for complete F function test
sha3 = SHA3(v)



# Test complete F function (24 cycles)
print("\nTesting complete F function (24 cycles):")
result = sha3.process()
for num in result:
    print(num,end="")