#Raymond Zha for Q1 part b

# RC4 Generating keystream
# 1. Initialization
def Initialization(k:list,n:int):
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
def Permutation(ini:tuple):
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
def Keystream(S:list,k:int):
    #k is the length of keystream needed
    keystream =[]
    lenk = len(S)
    
    #Generating steps
    i = j = 0
    #generate keystream of length k
    for times in range(k):
        i = (i+1)%lenk
        j = (j+S[i])%lenk
        
        
    
    
    
    return keystream