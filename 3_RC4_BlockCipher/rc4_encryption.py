"""
RC4 Message Encryption Example
-----------------------------
This program demonstrates using RC4 stream cipher to encrypt an alphabetic message.

The RC4 encryption process shown here:
1. Converts lowercase alphabetic characters to their 0-25 index values
2. Represents these values as 3-bit binary numbers
3. Generates an RC4 keystream using a predefined key
4. XORs the binary message with the keystream to create ciphertext

Usage:
- Ensure rc4.py is in the same directory
- Run: python q1b.py
- The encrypted result will be displayed

Parameters:
- n: Bit processing size (3 bits for this example)
- l: Length of the message (7 characters)
- key: Secret key as integer array [2, 5, 7, 1]
- M: Message to encrypt ("HACEDAB")

The program performs the following steps:
1. Converts the message to lowercase
2. Maps each character to its alphabetic index (0-25)
3. Converts these indices to 3-bit binary values
4. Generates the RC4 keystream
5. XORs the message bits with the keystream
6. Displays the encrypted result as a bit array

"""

from rc4 import rc4, DecimalToBinary, ConvertBitArraytoInt


#some tools here:
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
print("The keystream is:",keybi)

final = []
for i in range(len(keybi)):
    summ = message[i]+keybi[i]
    if summ == 2:
        final.append(0)
    else:
        final.append(summ)
    
print("The final result after xor is:",final)