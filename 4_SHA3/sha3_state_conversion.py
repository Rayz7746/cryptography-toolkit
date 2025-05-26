# SHA-3 State Array Conversion
# ---------------------------
# This script provides functions to convert between linear arrays and 3D state arrays used in the SHA-3 hash algorithm.
#
# Description:
#    The SHA-3 hash algorithm (based on Keccak) operates on a state that is structured as a 3D array
#    with dimensions 5×5×64. These functions handle the transformation between the linear input/output format
#    and the required 3D structure that the algorithm operates on internally.

# Input: State Array Initialization
# --------------------------------
# Transforms a linear input array into the 3D state array used in SHA-3 hash algorithm.
#
# Input:
#    - v: A linear array (list) containing 1600 bits (represented as 0s and 1s), which is the size
#      of the SHA-3 state for SHA3-224, SHA3-256, SHA3-384, and SHA3-512 variants.
#
# Algorithm:
#    1. Create an empty 3D array with dimensions 5×5×64 (5 rows, 5 columns, 64-bit depth)
#    2. Map each element from the linear input array to its corresponding position in the 3D state array
#    3. The mapping follows the formula: a[i][j][k] = v[64*(5*j + i) + k]
#
# Output:
#    Returns the 3D state array (5×5×64) initialized with values from the input list.
def inputSHA3(v:list):
    a = [[[None for _ in range(64)] for _ in range(5)] for _ in range(5)] #a[i][j][k] k -> j -> i
    for i in range(5):
        for j in range(5):
            for k in range(64):
                a[i][j][k] = v[64*(5*j + i) + k]
                
    return a

# Output: State Array Linearization
# --------------------------------
# Transforms the 3D state array back into a linear array format.
#
# Input:
#    - a: A 3D state array with dimensions 5×5×64 used in the SHA-3 hash algorithm.
#
# Algorithm:
#    The mapping follows the formula: v[64*(5*j + i) + k] = a[i][j][k]
#
# Output:
#    Returns a linear array of 1600 bits representing the SHA-3 state.
def outputSHA3(a:list[int][int][int]):
    v = [None] * 1600
    for i in range(5):
        for j in range(5):
            for k in range(64):
                v[64*(5*j + i) + k] = a[i][j][k]
    return v