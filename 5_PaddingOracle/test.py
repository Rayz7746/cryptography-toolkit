from oracle_connect import *
import sys

ciphertext=(b'\xc9\xdd\x57\x5d\xa3\xdf\x32\x6b\x19\xfc\x60\x04\xea\xaf\x8e\x9c'
                b'\xfd\xa1\xa8\xc4\x2d\x09\x69\xa1\xa2\x9f\x8c\x47\x77\xff\x54\x75'
                b'\xbe\x91\x7e\xf9\x57\x9f\x48\xfa\x28\xda\x22\x05\xa3\xa5\x25\x34'
                b'\xcf\xcf\xeb\xcc\x09\x46\xb9\x5c\xd1\xbf\x9c\x94\xce\xc4\x6b\xac')

def sample_helper_code():
    ##Break ciphertex into blocks of 128 bits (16 bytes)
    ##IV=cipherblocks[0], cipherblocks[1], cipherblocks[2], cipherblocks[3]
    cipherblocks = [ciphertext[i:i + BLOCKSIZE] for i in range(0, len(ciphertext), BLOCKSIZE)]
    
    ##Prints out each individual block
    for i in range(0, len(cipherblocks)):
            print(f"{bytearray(cipherblocks[i]).hex()}")
    
    ##The bytearray() method returns a bytearray object which is mutable (can be modified) - can be used when you want to change a byte of a block
    lastblock = bytearray(cipherblocks[-1])
    
    ##decode(): changes from byte to string of characters, for example b'\x54'.decode() returns the letter 'T' because the ascii hex value of 'T' is 54. 
    # This is useful when you want to get the decrypted message back as an English string
    print(b'\x54'.decode())
    #if y is an integer, this will decode it to the ascii character
    y=100
    print(y.to_bytes(1, 'little').decode())
    
    #You can call is_padding_okay(cipherblocks[i], cipherblocks[i+1]) function after connecting to the server.
    
def sample_helper_code():
    ##Break ciphertex into blocks of 128 bits (16 bytes)
    ##IV=cipherblocks[0], cipherblocks[1], cipherblocks[2], cipherblocks[3]
    cipherblocks = [ciphertext[i:i + BLOCKSIZE] for i in range(0, len(ciphertext), BLOCKSIZE)]
    
    ##Prints out each individual block
    for i in range(0, len(cipherblocks)):
            print(f"{bytearray(cipherblocks[i]).hex()}")
    
    ##The bytearray() method returns a bytearray object which is mutable (can be modified) - can be used when you want to change a byte of a block
    lastblock = bytearray(cipherblocks[-1])
    
    ##decode(): changes from byte to string of characters, for example b'\x54'.decode() returns the letter 'T' because the ascii hex value of 'T' is 54. This is useful when you want to get the decrypted message back as an English string
    print(b'\x54'.decode())
    #if y is an integer, this will decode it to the ascii character
    y=100
    print(y.to_bytes(1, 'little').decode())
    
    #You can call is_padding_okay(cipherblocks[i], cipherblocks[i+1]) function after connecting to the server.
    
# 1.cipherblocks:
# cipherblocks = [ciphertext[i:i + BLOCKSIZE] for i in range(0, len(ciphertext), BLOCKSIZE)]
# lastblock = bytearray(cipherblocks[-1])
# print(lastblock)
# print(b'\x54'.decode())
# y=100
# print(y.to_bytes(1, 'little').decode())


# delta_field = bytearray(BLOCKSIZE)
# print(delta_field)

# padding_length = 2

# for i in range(BLOCKSIZE - padding_length, 16):
#     delta_field[i] = padding_length ^ (padding_length + 1)
#     print(delta_field)

# print(delta_field)

ylist = [100, 101, 116, 97, 99, 105, 116, 110, 101, 104, 116, 117, 97, 32, 18]
for i in range(len(ylist)-1,-1,-1):
    print(ylist[i].to_bytes(1, 'little').decode(), end= "")
y = 29
print()
print(y.to_bytes(1, 'little').decode())

ylist1 = [32, 101, 100, 105, 115, 32, 114, 101, 118, 114, 101, 115, 32, 101, 104, 116]
for i in range(len(ylist1)-1,-1,-1):
    print(ylist1[i].to_bytes(1, 'little').decode(), end= "")

# print(y.to_bytes(1, 'little').decode())

