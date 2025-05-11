# need classify?!

def replace_multiple(text, char_map):
    """
    Replace multiple characters in a string based on a character mapping.

    This function performs multiple character substitutions on a text at the same time.

    Args:
        text (str): The input string to perform substitutions on.
        char_map (dict): A dictionary mapping characters to their replacements.
                         Keys are characters to replace, values are their replacements.

    Returns:
        str: A new string with all specified substitutions applied.

    Example:
        >>> text = "Hello, World!"
        >>> mapping = {'H': 'J', 'o': '0', 'l': '1'}
        >>> replace_multiple(text, mapping)
        'Je110, W0r1d!'
    """
    table = str.maketrans(char_map)
    return text.translate(table)

#some tools here:
#1.return char mod 26
def idx(char):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return alpha.index(char)

#2.handle with the original input
def handle(text):
    text = text.lower()
    text = text.replace(" ","")
    return text


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
# try this example:
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
# try this example:
# print(ConvertBitArraytoInt([1,0,0,0,0,0,1,1,1,0,0,1], 3))


# Seperate key list with the number "n"
def chunklist(k:list, n:int):
    result = []
    for i in range(0, len(k), n):
        result.append(k[i:i+n])
    return result