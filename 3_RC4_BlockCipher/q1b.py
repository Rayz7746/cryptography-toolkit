#Raymond Zha for Q1 part b
from q1a import rc4

#some tools here:
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
#1.Return char mod 26
def idx(char):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return alpha.index(char)

#2.Seperate key list with the number "n"
def chunklist(k:list, n:int):
    result = []
    for i in range(0, len(k), n):
        result.append(k[i:i+n])
    return result

# handle with message to make it present in the form of bits
M = "HACEDAB"
M = M.lower()
msglist = []
message = []
for char in M:
    msglist.append(DecimalToBinary(idx(char),3))
for alist in msglist:
    for n in alist:
        message.append(n)

l = len(M)
n = 3
key = [2, 5, 7, 1]

cipher = rc4(n, l, key)
keyde = cipher.gen()
keybi = cipher.biresult(keyde)

final = []
for i in range(len(keybi)):
    summ = message[i]+keybi[i]
    if summ == 2:
        final.append(0)
    else:
        final.append(summ)
    
print(final)