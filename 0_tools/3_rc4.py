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
        
    def DecimalToBinary(self, number, n):
        """Converts a decimal number to a binary array of length n"""
        res = []
        qu = number
        while qu != 0:
            rem = qu % 2
            qu = qu //2
            res.append(rem)
        
        if len(res)>n:
            return
        diff = n - len(res)
        for i in range(diff):
            res.append(0)
        res.reverse()
        return res
    
    def ConvertBitArraytoInt(self, k, n):
        """Converts a bit array to an array of integers, each using n bits"""
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
    
    # output the final form in n*l
    def biresult(self,res:list):
        """Converts the decimal result to binary format"""
        newlist =[]
        final = []
        for num in res:
            newlist.append(self.DecimalToBinary(num, self.n))
        for alist in newlist:
            for n in alist:
                final.append(n)
        return final
    
        
    # 1. Initialization
    def Initialization(self, k:list, n:int):
        """
        Initialize the S-box and key array T
        
        Args:
            k (list): Key array
            n (int): Parameter determining size of S-box (2^n)
            
        Returns:
            tuple: Contains the S-box and key array T
        """
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
        """
        Permute the S-box based on the key array
        
        Args:
            ini (tuple): Contains the S-box and key array T
            
        Returns:
            list: Permuted S-box
        """
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
        """
        Generate the keystream using the permuted S-box
        
        Args:
            S (list): Permuted S-box
            k (int): Length of keystream needed
            
        Returns:
            list: Generated keystream
        """
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
        """
        Execute the complete RC4 keystream generation process
        
        Returns:
            list: Generated keystream in decimal format
        """
        n = self.n
        l = self.l
        key = self.key
        
        tu = self.Initialization(key,n)
        perlist = self.Permutation(tu)
        res = self.Keystream(perlist,l)
        
        return res