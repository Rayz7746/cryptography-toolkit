# Raymond Zha for Q1, I do not handwritten for Q1
# note that Q1 need the file hw1Q1-ciphertext.txt in order to run
def replace_multiple(text, char_map):
    table = str.maketrans(char_map)
    return text.translate(table)


with open ('hw1Q1-ciphertext.txt', 'r') as file:
    content = file.read()
    
    
bicont = content.replace(" ","")
bifreq = {}
freq = {}
trifreq = {}

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
# {'E': 61, 'W': 56, 'Q': 43, 'G': 33, 'M': 31, 'I': 29, 'O': 28, 'K': 24, 'R': 21, 'A': 18, 'U': 17, 'S': 16, 'Z': 12, 'V': 12, 'L': 12, 'N': 10, 'Y': 9, 'D': 9, 'T': 8, 'X': 6, 'H': 3, 'C': 3}
# E T A O I 
# TH HE IN ER AN
# 'EI': 19, 'IW': 16, 'WQ': 10, 'GM': 10, 'QE': 9, 'EO': 9, 'EV': 8, 'OE': 8, 'MR': 7, 'WK': 7, 'KW': 7,
# "EIW" appears mulitple times maybe EIW = THE; Q appears as a word so maybe Q = A
char_map = {
'E': 'T', 'I': 'H', 'W': 'E', 'Q': 'A',
'G': 'O', 'M': 'N', 'Y': 'F', 'R': 'D',
'L': 'G', 'K': 'R', 'X': 'K', 'A': 'U',
'N': 'B', 'V': 'W', 'U': 'S', 'O': 'I',
'Z': 'C', 'H': 'P', 'S': 'L', 'T': 'Y',
'D': 'M', 'C': 'V'
}
#Darx appear, so map x = k; thoaght = thought; Nurnt burnt; Veek = week; roght = right, underutand = understand; zurrent = current; herfect = perfect; cousd = could
result = replace_multiple(content, char_map)
print(result)

#finally!
# HE PICKED UP THE BURNT END OF THE BRANCH AND MADE A MARK ON THE STONE DAY FIFTY TWO IF THE MARKS ON THE STONE WERE ACCURATE 
# HE COULD NOT BE SURE DAY AND NIGHTS HAD BEGUN TO BLEND TOGETHER CREATING CONFUSION BUT HE KNEW IT WAS A LONG TIME MUCH TOO LONG 
# IT WAS A GOOD IDEA AT LEAST THEY ALL THOUGHT IT WAS A GOOD IDEA AT THE TIME 
# HINDSIGHT WOULD REVEAL THAT IN REALITY IT WAS AN UNBELIEVABLY TERRIBLE IDEA BUT IT WOULD TAKE ANOTHER WEEK FOR THEM TO UNDERSTAND THAT 
# RIGHT NOW AT THIS VERY MOMENT THEY ALL AGREED THAT IT WAS THE PERFECT COURSE OF ACTION FOR THE CURRENT SITUATION

    
