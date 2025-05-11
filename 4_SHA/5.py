#Raymond Zha Homework 5

def inputSHA3(v:list):
    a = [[[None for _ in range(64)] for _ in range(5)] for _ in range(5)] 
    for i in range(5):
        for j in range(5):
            for k in range(64):
                a[i][j][k] = v[64*(5*j + i) + k]
                
    return a



def theta(a_in:list):
    a_out = [[[None for _ in range(64)] for _ in range(5)] for _ in range(5)]
    
    for i in range(5):
        for j in range(5):
            for k in range(64):
                sig1 = 0
                for x in range(5):
                    sig1 = sig1 ^ a_in[(i+4)%5][x][k]
                sig2 = 0
                for x in range(5):
                    sig2 = sig2 ^ a_in[(i+1)%5][x][(k+63)%64]
                    
                a_out[i][j][k] = a_in[i][j][k] ^ sig1 ^ sig2
    
    
    return a_out

with open('sha3in.txt','r') as file:
    content = file.read()
    v = []
    for char in content:
        v.append(int(char))

a = inputSHA3(v)
a_out = theta(a)

# test value for aout[4][3][9...18] :0011011000
# i = 4
# j = 3
# for k in range(9,19):
#     print(a_out[i][j][k], end="")

for k in range(25,35):
    print(a_out[2][2][k], end="")

# answer: 0011110000