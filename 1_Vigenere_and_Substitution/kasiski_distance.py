# Kasiski Examination for Cryptanalysis
# --------------------------------------
# This script implements the Kasiski examination method to determine the 
# key length of a Vigenère cipher by analyzing the distances between repeated 
# trigrams (three-letter sequences) in the ciphertext.
#
# Description:
#    The Kasiski examination works by identifying repeated patterns in the 
#    ciphertext and measuring the distances between them. In a Vigenère cipher,
#    if the same plaintext fragment is encrypted with the same portion of the key,
#    it will produce the same ciphertext fragment. The distances between these 
#    repeated fragments are likely to be multiples of the key length.
#
# Input:
#    - 'kasiski.txt': A text file containing the ciphertext to be analyzed.
#      The file should be in the same directory as this script.
#
# Algorithm:
#    1. Read the ciphertext from 'kasiski.txt'
#    2. Find all trigrams (three-letter sequences) in the text and their frequencies
#    3. Filter out trigrams that only appear once
#    4. Sort the remaining trigrams by frequency (most frequent first)
#    5. For each repeating trigram, find all its occurrences and calculate the 
#       distances between consecutive occurrences
#    6. Analyze these distances to identify potential key lengths
#
# Output:
#    Prints the sorted list of trigrams that appear more than once, with their frequencies.
#    For each such trigram, prints the distances between consecutive occurrences.
#    These distances can be analyzed to determine the likely key length of the cipher.
#
# Usage:
#    Run the script directly. It will look for 'kasiski.txt' in the same directory.
#
# Notes:
#    - The key length is likely to be a common factor of the distances between repeated trigrams
#    - In the example output, most distances are multiples of 5, suggesting a key length of 5
#    - This implementation is designed for educational purposes to demonstrate the principles 
#      of the Kasiski examination technique

# Workflow:
#    This script is the first step in breaking a Vigenère cipher:
#    1. Use this script (kasiski_distance.py) to determine the likely key length
#    2. Next, use kasiski_frequency.py to analyze letter frequencies within each
#       column of the ciphertext and determine the actual key
#
#    The distances between repeated trigrams calculated here will help identify
#    the most probable key length, which is essential for the frequency analysis
#    performed in the next step.


import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the text file
file_path = os.path.join(script_dir, 'kasiski.txt')

# Use the full path to open the file
with open(file_path, 'r') as file:
    content = file.read()

trigram = {}
for i in range(len(content)-2):
    tri = content[i] + content[i+1] + content[i+2]
    trigram[tri] = trigram.get(tri,0) + 1
    
# now get every trigram with frequency above 1:
pro_tri = [item for item in trigram.items() if item[1]!=1]

newtri = sorted(pro_tri,key= lambda x:x[1],reverse=True)
print(newtri)

def find_distance(string,sub):
    indices = []
    index = 0
    while index != -1:
        index = string.find(sub,index)
        if index != -1:
            indices.append(index)
            index += 1
    # print(indices)
    print(f"For string \"{sub}\" ")
    for i in range(len(indices)-1):
          print(f"the distance between {i+1} and {i+2} appearance is: {indices[i+1]-indices[i]}")

#now lets find the distance:
for pair in newtri:
    find_distance(content,pair[0])

#for the below output, we can easily guess that the key length of Q3 is just 5, since most of the output is a multipler of 5

# example result

"""
For string "slr" 
the distance between 1 and 2 appearance is: 10
the distance between 2 and 3 appearance is: 250
the distance between 3 and 4 appearance is: 265
For string "xuh"
the distance between 1 and 2 appearance is: 205
the distance between 2 and 3 appearance is: 160
For string "rzc"
the distance between 1 and 2 appearance is: 30
For string "ifw"
the distance between 1 and 2 appearance is: 435
For string "dho"
the distance between 1 and 2 appearance is: 260
For string "maj"
the distance between 1 and 2 appearance is: 505
For string "ubd"
the distance between 1 and 2 appearance is: 280
For string "bdh"
the distance between 1 and 2 appearance is: 280
For string "jlh"
the distance between 1 and 2 appearance is: 125
For string "lhg"
the distance between 1 and 2 appearance is: 125
For string "omh"
the distance between 1 and 2 appearance is: 390
For string "rvh"
the distance between 1 and 2 appearance is: 5
For string "nrr"
the distance between 1 and 2 appearance is: 195
For string "hqi"
the distance between 1 and 2 appearance is: 125
For string "orc"
the distance between 1 and 2 appearance is: 290
For string "rcj"
the distance between 1 and 2 appearance is: 290
For string "cjw"
the distance between 1 and 2 appearance is: 290
For string "wgr"
the distance between 1 and 2 appearance is: 40
For string "grf"
the distance between 1 and 2 appearance is: 40
For string "rda"
the distance between 1 and 2 appearance is: 335
For string "hgi"
the distance between 1 and 2 appearance is: 140
For string "wbi"
the distance between 1 and 2 appearance is: 255
For string "dvr"
the distance between 1 and 2 appearance is: 215
For string "rgk"
the distance between 1 and 2 appearance is: 299
For string "hrt"
the distance between 1 and 2 appearance is: 130
For string "rtw"
the distance between 1 and 2 appearance is: 113
For string "lbf"
the distance between 1 and 2 appearance is: 65
For string "dbc"
the distance between 1 and 2 appearance is: 160
For string "bcx"
the distance between 1 and 2 appearance is: 160
For string "cxu"
the distance between 1 and 2 appearance is: 160
For string "khr"
the distance between 1 and 2 appearance is: 21
For string "vhh"
the distance between 1 and 2 appearance is: 85
For string "let"
the distance between 1 and 2 appearance is: 110
For string "etl"
the distance between 1 and 2 appearance is: 110
"""

