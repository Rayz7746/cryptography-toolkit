# SHA-3 F-function Complete Implementation
# ----------------------------
# This script implements the complete SHA-3 hash f-function algorithm with all five transformation steps. (only f-function included)
#
# Description:
#    SHA-3 (Secure Hash Algorithm 3) is based on the Keccak sponge function construction.
#    The algorithm operates on a 3D state array of dimensions 5×5×64 and consists of five
#    core transformations that are applied in sequence during each round:
#    - θ (theta): Diffuses each bit's influence across the entire state
#    - ρ (rho): Provides inter-slice diffusion through rotations
#    - π (pi): Ensures bits diffuse to different positions
#    - χ (chi): Adds non-linearity through bitwise operations
#    - ι (iota): Breaks symmetry by XORing round constants
#
#    Key components:
#    - input_sha3() / output_sha3(): Convert between linear arrays and 3D state arrays
#    - theta(), rho(), pi(), chi(), iota(): Implement each transformation step
#    - process(): Applies the full 24 rounds of transformations to input data
#
#    The algorithm performs multiple rounds (24) of these transformations to create
#    a secure cryptographic hash.

class SHA3:
    def __init__(self, input_data=None):
        """Initialize the SHA3 object with optional input data"""
        self.state = None
        if input_data:
            self.state = self.input_sha3(input_data)
    
    def input_sha3(self, v):
        """Convert a 1D list to 3D state array"""
        a = [[[None for _ in range(64)] for _ in range(5)] for _ in range(5)] 
        for i in range(5):
            for j in range(5):
                for k in range(64):
                    a[i][j][k] = v[64*(5*j + i) + k]
        return a
    
    def output_sha3(self, a=None):
        """Convert 3D state array back to 1D list"""
        if a is None:
            a = self.state
        
        v = [None] * 1600
        for i in range(5):
            for j in range(5):
                for k in range(64):
                    v[64*(5*j + i) + k] = a[i][j][k]
        return v
    
    def theta(self, a_in=None):
        """Apply the theta transformation"""
        if a_in is None:
            a_in = self.state
            
        a_out = [[[None for _ in range(64)] for _ in range(5)] for _ in range(5)]
        
        for i in range(5):
            for j in range(5):
                for k in range(64):
                    sig1 = 0
                    for x in range(5):
                        sig1 = sig1 ^ a_in[(i+4)%5][x][k]
                    sig2 = 0
                    for x in range(5):
                        sig2 = sig2 ^ a_in[(i+1)%5][x][(k+63)%64]
                        
                    a_out[i][j][k] = a_in[i][j][k] ^ sig1 ^ sig2
        
        return a_out
    
    def rho(self, a_in=None):
        """Apply the rho transformation"""
        if a_in is None:
            a_in = self.state
            
        rhomatrix = [
            [0, 36, 3, 41, 18],
            [1, 44, 10, 45, 2],
            [62, 6, 43, 15, 61],
            [28, 55, 25, 21, 56],
            [27, 20, 39, 8, 14]
        ]
        
        a_out = [[[None for _ in range(64)] for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                for k in range(64):
                    idx = rhomatrix[i][j]
                    a_out[i][j][k] = a_in[i][j][(k-idx+64)%64]
        
        return a_out
    
    def pi(self, a_in=None):
        """Apply the pi transformation"""
        if a_in is None:
            a_in = self.state
            
        a_out = [[[None for _ in range(64)] for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                for k in range(64):
                    a_out[j][(2*i+3*j)%5][k] = a_in[i][j][k]
        
        return a_out
    
    def chi(self, a_in=None):
        """Apply the chi transformation"""
        if a_in is None:
            a_in = self.state
            
        a_out = [[[None for _ in range(64)] for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                for k in range(64):
                    a_out[i][j][k] = a_in[i][j][k] ^ ((1-a_in[(i+1)%5][j][k]) * a_in[(i+2)%5][j][k])
        
        return a_out
    
    def iota(self, a_in=None, cycle=0):
        """Apply the iota function"""
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

    def process(self, input_data=None):
        """Process the data through all SHA3 transformations"""
        if input_data:
            self.state = self.input_sha3(input_data)
    
        if self.state is None:
            raise ValueError("No input data provided")
    
        # Perform the full 24 rounds of the SHA-3 permutation
        for round_idx in range(24):
            self.state = self.theta(self.state)
            self.state = self.rho(self.state)
            self.state = self.pi(self.state)
            self.state = self.chi(self.state)
            self.state = self.iota(self.state, cycle=round_idx)
    
        # Convert 3D state to 1D output array v
        v = self.output_sha3(self.state)
        return v