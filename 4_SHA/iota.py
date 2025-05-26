# SHA-3 Iota Transformation
# ------------------------
# This script implements the iota transformation step used in the SHA-3 hash algorithm. Since this step is the most complex one,
# I listed it as a new independent file here to see how I approach this.
#
# Description:
#    The iota transformation is one of the five core transformations (θ, ρ, π, χ, ι) in the SHA-3 algorithm.
#    It's the final step in each round, where specific bits in the state array are modified by XORing with
#    round constants. This breaks the symmetry in the SHA-3 algorithm, preventing patterns from propagating
#    across rounds.
#
#    Key components:
#    - rc_hex_values: 24 round constants (one for each round) defined in hexadecimal
#    - iota_bits(): Utility function to determine which bits are set in each RC value
#    - iota(): Applies the round constant for a specific cycle to the state array by XORing
#              the identified bits in the first lane (a[0][0])
#
#    The transformation only affects specific bit positions of the first word (a[0][0]) in the 5×5×64 state array,
#    making it computationally efficient while still achieving its cryptographic purpose.

# List of RC values in hex
rc_hex_values = [
    "0x0000000000000001", "0x0000000000008082", "0x800000000000808A", "0x8000000080008000",
    "0x000000000000808B", "0x0000000080000001", "0x8000000080008081", "0x8000000000008009",
    "0x000000000000008A", "0x0000000000000088", "0x0000000080008009", "0x000000008000000A",
    "0x000000008000808B", "0x800000000000008B", "0x8000000000008089", "0x8000000000008003",
    "0x8000000000008002", "0x8000000000000080", "0x000000000000800A", "0x800000008000000A",
    "0x8000000080008081", "0x8000000000008080", "0x0000000080000001", "0x8000000080008008"
]

def iota_bits(hex_str):
    value = int(hex_str, 16)
    set_bits = []  #store the positions of bits that are 1
    # check the value changed
    for i in range(64):
        shifted = value >> i           # shift the bits of value to the right by i(i.e check if the rightmost i bit)
        lsb = shifted & 1              # check the rightmost i bit is 1 or not
        if lsb == 1:
            set_bits.append(i)
    
    return set_bits


# Print which bits will be XORed for each RC[i]
for i, rc in enumerate(rc_hex_values):
    set_bits = iota_bits(rc)
    print(f"RC[{i}] affects bits: {set_bits}")




# complete iota step
def iota(self, a_in=None, cycle=0):
    if a_in is None:
        a_in = self.state

    rc_hex_values = [
        "0x0000000000000001", "0x0000000000008082", "0x800000000000808A", "0x8000000080008000",
        "0x000000000000808B", "0x0000000080000001", "0x8000000080008081", "0x8000000000008009",
        "0x000000000000008A", "0x0000000000000088", "0x0000000080008009", "0x000000008000000A",
        "0x000000008000808B", "0x800000000000008B", "0x8000000000008089", "0x8000000000008003",
        "0x8000000000008002", "0x8000000000000080", "0x000000000000800A", "0x800000008000000A",
        "0x8000000080008081", "0x8000000000008080", "0x0000000080000001", "0x8000000080008008"
    ]
    
    if cycle >= len(rc_hex_values):
        raise ValueError("Cycle index out of range (must be 0–23).")

    rc = int(rc_hex_values[cycle], 16)

    # Apply XOR to a[0][0][k]
    for k in range(64):
        if (rc >> k) & 1:
            a_in[0][0][k] ^= 1

    return a_in




