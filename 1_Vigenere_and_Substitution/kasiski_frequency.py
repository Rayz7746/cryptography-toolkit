# Frequency Analysis for Vigenère Cipher Cryptanalysis
# ----------------------------------------------------
# This script implements the frequency analysis technique for breaking a Vigenère cipher
# after the key length has been determined using the Kasiski examination method.
#
# Description:
#    Once the key length is known (in this case, 5), the Vigenère cipher can be treated 
#    as multiple Caesar ciphers. This script splits the ciphertext into 5 separate streams, 
#    where each stream consists of characters that were encrypted with the same key letter.
#    By analyzing the frequency distribution in each stream, we can determine each letter 
#    of the encryption key.
#
# Input:
#    - 'kasiski.txt': A text file containing the ciphertext to be analyzed.
#      The file should be in the same directory as this script.
#
# Algorithm:
#    1. Read the ciphertext from 'kasiski.txt'
#    2. For each position modulo the key length (0 to 4):
#       a. Extract all characters at that position from the ciphertext
#       b. Count the frequency of each letter in the extracted substring
#       c. Output the frequency distribution
#    3. The frequency distributions can be analyzed manually to determine
#       each letter of the key by comparing with English letter frequencies
#
# Output:
#    Prints the frequency counts for each letter ('a' through 'z') for each of the 
#    5 positions in the key. These frequency patterns can reveal the shift value 
#    for each position when compared to normal English letter frequencies.
#
# Usage:
#    Run the script directly. It will look for 'kasiski.txt' in the same directory.
#
# Notes:
#    - This is part 2 of the Vigenère cipher cryptanalysis process
#    - Step 1 (determining key length using Kasiski examination) was completed previously
#    - The most frequent letters in each stream likely correspond to 'e', 't', 'a', etc.
#      in the plaintext, which helps determine each shift value of the key
#
# Workflow:
#    Complete Vigenère cipher cryptanalysis process:
#    1. First use kasiski_distance.py to find repeated patterns and determine key length
#    2. Then use this script (kasiski_frequency.py) to perform frequency analysis
#       on each stream of characters to determine the actual key
#    3. Once the key is known, the ciphertext can be decrypted



#key length = 5, guess from the kasiski_distance.py
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the text file
file_path = os.path.join(script_dir, 'kasiski.txt')

# Use the full path to open the file
with open(file_path, 'r') as file:
    content = file.read()

keylen = 5

def count_freq(idx):
    string = ""
    # create a default dict
    freq = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        freq[letter] = 0
    
    #filter letters
    for i in range(len(content)):
        if i % 5 == idx:
            string += content[i]
    for char in string:
        freq[char] = freq.get(char) + 1
    
    ans =[]
    for v in freq.values():
        ans.append(v)
    
    
    return ans

# detailed output
for i in range(keylen):
    print(f"The frequency of the letters in position {i} (mod key_length=5) is:")
    print(count_freq(i))

print()
print("Here are the raw output:")

#raw output
for i in range(keylen):
    print(count_freq(i))
    
"""
[0, 5, 0, 6, 0, 3, 2, 18, 3, 5, 5, 14, 0, 0, 1, 2, 3, 13, 5, 0, 5, 8, 9, 2, 0, 4]
[2, 12, 8, 1, 0, 8, 9, 12, 2, 1, 5, 0, 0, 0, 9, 1, 3, 5, 8, 1, 3, 5, 6, 0, 2, 9]
[4, 0, 6, 15, 3, 4, 4, 12, 0, 2, 3, 5, 8, 8, 1, 0, 8, 8, 7, 2, 2, 2, 0, 1, 0, 7]
[3, 0, 4, 0, 5, 5, 2, 8, 14, 3, 0, 5, 7, 0, 0, 6, 1, 11, 6, 2, 1, 5, 11, 12, 1, 0]
[3, 10, 0, 0, 8, 12, 11, 6, 3, 2, 0, 1, 0, 5, 5, 4, 4, 19, 1, 6, 5, 3, 0, 1, 2, 1]
"""