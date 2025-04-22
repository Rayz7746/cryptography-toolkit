#Raymond Zha for Q1 part a
# two functions:
def DecimalToBinary(number,n):
    """ 
    with two integer inputs number and n. Its output is an array of size n, returning the binary representation of number.

    Args:
        number (int): numbers in decimal
        n (int): arraysize
    """
    
    res = []
    qu = number
    # convert to binary
    while qu != 0:
        rem = qu % 2
        qu = qu //2
        res.append(rem)
    
    if len(res)>n:
        return
    # fill with zero and reverse to get the correct order
    diff = n - len(res)
    for i in range(diff):
        res.append(0)
    res.reverse()
    return res
# print(DecimalToBinary(100,8))

def ConvertBitArraytoInt(k, n):
    """
    take an array of bits and n, and output an array of integers with every n bits converted to its decimal representation. 
    So ConvertBitArraytoInt([1,0,0,0,0,0,1,1,1,0,0,1], 3) should output [4, 0, 7, 1].
 

    Args:
        Arrayk (array): array with 1 and 0
        intn (int): divide number
    """
    if len(k) % n !=0:
        return
    res = [None]*(len(k)//n)
    num = 0
    # highest 2^n-1
    for i in range(len(k)):
        # number = 2^n-1 + 2^n-2 ...
        power = k[i]*(2**(n-i%n-1))
        num += power
        if i % n ==(n-1):
            qu = i//n
            res[qu] = num
            num = 0
    
    return res
# print(ConvertBitArraytoInt([1,0,0,0,0,0,1,1,1,0,0,1], 3))



#Raymond Zha for Q1

# RC4 Generating keystream(functions all in decimal)
class rc4:
    def __init__(self, n: int, l: int, key: list):
        """
        Initialize RC4 cipher
        
        Args:
            n (int): Parameter for RC4 (determines size of S box - 2^n)
            l (int): Length of plaintext/ciphertext (number of characters)
            key (list): Array of bits which is the secret key
        """
        self.n = n
        self.l = l
        self.key = key
        
    # output the final form in n*l
    def biresult(self,res:list):
        newlist =[]
        final = []
        for num in res:
            newlist.append(DecimalToBinary(num, self.n))
        for alist in newlist:
            for n in alist:
                final.append(n)
        return final
    
        
    # 1. Initialization
    def Initialization(self, k:list, n:int):
        last = 2**n
        lenk = len(k)
        # List from 0 to 2^n -1
        S = [None] * last
        
        # Key recycle list
        T = [None] * last
        for i in range(last):
            S[i]= i
            T[i] = k[i%lenk]
        
        return S,T
    # S = tuple[0] T = tuple[1]

    # 2. Permutation
    def Permutation(self, ini:tuple):
        # get S and T from tuple
        S = ini[0]
        T = ini[1]
        
        # S and T should have the same length
        if len(S)!= len(T):
            return
        lenk = len(S)
        
        # permuatation steps:
        j = 0
        for i in range(lenk):
            j = (j+S[i]+T[i])%lenk
            S[i], S[j] = S[j], S[i]#swap
        return S

    #3. Generate the Keystream
    def Keystream(self, S:list, k:int):
        #k is the length of keystream needed
        keystream =[]
        lenk = len(S)
        
        #Generating steps
        i = j = 0
        #generate keystream of length k
        for times in range(k):
            i = (i+1)%lenk
            j = (j+S[i])%lenk
            S[i], S[j] = S[j], S[i]
            t = (S[i]+S[j])%lenk
            ks = S[t]
            keystream.append(ks)
        
        return keystream
    
    # main generating function for the whole process
    def gen(self):
        n = self.n
        l = self.l
        key = self.key
        
        tu = self.Initialization(key,n)
        perlist = self.Permutation(tu)
        res = self.Keystream(perlist,l)
        
        return res
    





# # Test RC4 implementation note that the key is in the form of decimal

# # Initialize RC4 with parameters: n=3 (working with 3-bit numbers), l=11 (11 characters), key=[3,1,4,7,5]
# print("Initializing RC4 with:")
# print(f"  n = 3 (S-box size will be 2^3 = 8)")
# print(f"  l = 11 (generating keystream of length 11)")
# print(f"  key = [3,1,4,7,5]")
# test = rc4(3, 11, [3,1,4,7,5])

# # Generate and display keystream in decimal
# keystream_decimal = test.gen()
# print("Keystream in decimal:")
# print(f"  {keystream_decimal}")

# # Convert keystream to binary representation
# keystream_binary = test.biresult(keystream_decimal)
# print("Keystream in binary (flattened):")
# print(f"  {keystream_binary}")

# # Convert binary keystream back to decimal (in 3-bit chunks)
# keystream_chunks = ConvertBitArraytoInt(keystream_binary, 3)
# print("Keystream binary converted back to decimal (3-bit chunks):")
# print(f"  {keystream_chunks}")


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