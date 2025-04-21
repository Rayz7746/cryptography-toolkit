#Raymond Zha question 3 part b
#key length = 5
with open('hw1Q3-ciphertext.txt','r') as file:
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