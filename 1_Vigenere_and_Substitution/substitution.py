# Monoalphabetic Substitution Cipher Decoder
# ------------------------------
# This program decrypts text that has been encrypted using a monoalphabetic 
# substitution cipher, where each letter in the plaintext is replaced with a 
# different letter consistently throughout the text.
# 
# The program performs frequency analysis by:
# 1. Counting occurrences of single letters, bigrams (2-letter sequences),
#    and trigrams (3-letter sequences)
# 2. Sorting these by frequency to identify patterns
# 3. Using these patterns to determine the substitution mapping
# 
# A predefined character mapping is then applied to decrypt the ciphertext.
# 
# Requirements:
# - A file named 'sub-text.txt' containing the encrypted text must be in
#   the same directory as this script.

import os




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

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the text file
file_path = os.path.join(script_dir, 'sub-text.txt')

# Use the full path to open the file
with open(file_path, 'r') as file:
    content = file.read()
    
    
bicont = content.replace(" ","")
bifreq = {}
freq = {}
trifreq = {}

# frequency analysis for single letter, bigrams and trigrams
for char in content:
    if char != " ":
        freq[char] = freq.get(char,0) + 1

freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)
freq = dict(freq)


for idx in range(len(bicont)-1):
    bigram = bicont[idx] + bicont[idx+1]
    bifreq[bigram] = bifreq.get(bigram,0) + 1

for idx in range(len(bicont)-2):
    trigram = bicont[idx] + bicont[idx+1] + bicont[idx+2]
    trifreq[trigram] = trifreq.get(trigram,0) + 1

bifreq = dict(sorted(bifreq.items(), key = lambda x:x[1],reverse=True))
trifreq = dict(sorted(trifreq.items(), key = lambda x:x[1],reverse=True))

# print(freq)
# print(bifreq)
# print(trifreq)


# Below are the example analysis, cipher text:
# IW HOZXWR AH EIW NAKME WMR GY EIW NKQMZI QMR DQRW Q DQKX GM EIW UEGMW 
# RQT YOYET EVG OY EIW DQKXU GM EIW UEGMW VWKW QZZAKQEW IW ZGASR MGE NW 
# UAKW RQT QMR MOLIEU IQR NWLAM EG NSWMR EGLWEIWK ZKWQEOML ZGMYAUOGM NAE 
# IW XMWV OE VQU Q SGML EODW DAZI EGG SGML OE VQU Q LGGR ORWQ QE SWQUE EIWT 
# QSS EIGALIE OE VQU Q LGGR ORWQ QE EIW EODW IOMRUOLIE VGASR KWCWQS EIQE OM 
# KWQSOET OE VQU QM AMNWSOWCQNST EWKKONSW ORWQ NAE OE VGASR EQXW QMGEIWK VWWX 
# YGK EIWD EG AMRWKUEQMR EIQE KOLIE MGV QE EIOU CWKT DGDWME EIWT QSS QLKWWR EIQE 
# OE VQU EIW HWKYWZE ZGAKUW GY QZEOGM YGK EIW ZAKKWME UOEAQEOGM




# {'E': 61, 'W': 56, 'Q': 43, 'G': 33, 'M': 31, 'I': 29, 'O': 28, 'K': 24, 'R': 21, 'A': 18, 'U': 17, 'S': 16, 'Z': 12, 'V': 12, 'L': 12, 'N': 10, 'Y': 9, 'D': 9, 'T': 8, 'X': 6, 'H': 3, 'C': 3}
# E T A O I 
# TH HE IN ER AN
# 'EI': 19, 'IW': 16, 'WQ': 10, 'GM': 10, 'QE': 9, 'EO': 9, 'EV': 8, 'OE': 8, 'MR': 7, 'WK': 7, 'KW': 7,
# "EIW" appears mulitple times maybe EIW = THE; Q appears as a word so maybe Q = A


# char_map is the mapping of letters using function replace_multiple
char_map = {
'E': 'T', 'I': 'H', 'W': 'E', 'Q': 'A',
'G': 'O', 'M': 'N', 'Y': 'F', 'R': 'D',
'L': 'G', 'K': 'R', 'X': 'K', 'A': 'U',
'N': 'B', 'V': 'W', 'U': 'S', 'O': 'I',
'Z': 'C', 'H': 'P', 'S': 'L', 'T': 'Y',
'D': 'M', 'C': 'V'
}
# Darx appear, so map x = k; thoaght = thought; Nurnt burnt; Veek = week; roght = right, underutand = understand; zurrent = current; herfect = perfect; cousd = could
result = replace_multiple(content, char_map)
print(result)

# Plaintext Decrypted:
# HE PICKED UP THE BURNT END OF THE BRANCH AND MADE A MARK ON THE STONE DAY FIFTY TWO IF THE MARKS ON THE STONE WERE ACCURATE 
# HE COULD NOT BE SURE DAY AND NIGHTS HAD BEGUN TO BLEND TOGETHER CREATING CONFUSION BUT HE KNEW IT WAS A LONG TIME MUCH TOO LONG 
# IT WAS A GOOD IDEA AT LEAST THEY ALL THOUGHT IT WAS A GOOD IDEA AT THE TIME 
# HINDSIGHT WOULD REVEAL THAT IN REALITY IT WAS AN UNBELIEVABLY TERRIBLE IDEA BUT IT WOULD TAKE ANOTHER WEEK FOR THEM TO UNDERSTAND THAT 
# RIGHT NOW AT THIS VERY MOMENT THEY ALL AGREED THAT IT WAS THE PERFECT COURSE OF ACTION FOR THE CURRENT SITUATION

    
