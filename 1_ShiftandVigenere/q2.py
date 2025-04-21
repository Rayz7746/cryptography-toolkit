# Raymond Zha for Q2
# note that Q2 need the file hw1Q2-plaintext.txt and hw1Q2-ciphertext.txt in order to run

alpha = "abcdefghijklmnopqrstuvwxyz"
#some tools here:
#1.return char mod 26
def idx(char):
    return alpha.index(char)

#2.handle with the original input
def handle(text):
    text = text.lower()
    text = text.replace(" ","")
    return text

#key length, key example: abstract 8; let's do a mod 8 to solve this: 0:a, 1:b...; t:7 we could use index mod(len) to know which alpha to add



def vig_en(plain,key):
    plain = handle(plain)
    keylen = len(key)
    cipher = ""
    for i in range(len(plain)):
        #first know which char in key to cipher:
        ci_i = i % keylen
        cipher_num = (idx(plain[i]) + idx(key[ci_i])) % 26
        cipher += alpha[cipher_num]
    return cipher

def vig_de(cipher,key):
    cipher = handle(cipher)
    plain = ""
    keylen = len(key)
    
    for i in range(len(cipher)):
        de_i = i % keylen
        decode_num = (idx(cipher[i])+26-idx(key[de_i])) % 26
        plain += alpha[decode_num]
    return plain


# the above are the functions, below are reading file parts, please change the name in order to read the files

# for encrypt use the following:
with open('hw1Q2-plaintext.txt','r') as file:
    plain_content = file.read()
    pla = plain_content.splitlines()
    print("### Result of Encryption ###")
    for i in range(len(pla)//2):
        print(vig_en(pla[2*i],pla[2*i+1]))
        
print()

#for decrypt use the following:
with open('hw1Q2-ciphertext.txt','r') as file:
    cipher_content = file.read()
    cip = cipher_content.splitlines()
    print("### Result of Decryption ###")
    for i in range(len(cip)//2):
        print(vig_de(cip[2*i],cip[2*i+1]))

    


