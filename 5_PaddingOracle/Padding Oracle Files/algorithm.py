"""
 Santa Clara University: CSCI 181
 Raymond Zha
"""
from oracle_connect import *
import sys
    
    

if __name__ == '__main__': 
    #Spring25
    ciphertext=(b'\xc9\xdd\x57\x5d\xa3\xdf\x32\x6b\x19\xfc\x60\x04\xea\xaf\x8e\x9c'
                b'\xfd\xa1\xa8\xc4\x2d\x09\x69\xa1\xa2\x9f\x8c\x47\x77\xff\x54\x75'
                b'\xbe\x91\x7e\xf9\x57\x9f\x48\xfa\x28\xda\x22\x05\xa3\xa5\x25\x34'
                b'\xcf\xcf\xeb\xcc\x09\x46\xb9\x5c\xd1\xbf\x9c\x94\xce\xc4\x6b\xac')

    #connect to the padding oracle server
    #you should call this before calling is_padding_okay()
    if oracle_connect() < 0:
       print("Could not connect to server.\n")
       sys.exit()

    #Write your code here.
    
    # General idea:
    # 1. I should check from the end of the last block(block[3]), to see if the padding is correct. 
    # so that I can find the padding length. Just change one bit by one bit, and check if the padding is correct.
    # I need to find the last bit that is not correct, and then I can find the padding length.
    # 2. After I find the padding length, I can find the last byte of the plaintext. By using Y = i xor (b+1)
    # 3. Then I can find the second last byte of the plaintext, and so on.
    
    
    
    
    
    
    # Break ciphertext into blocks
    cipherblocks = [ciphertext[i:i + BLOCKSIZE] for i in range(0, len(ciphertext), BLOCKSIZE)]    
    
    
    # Step 1: Find padding length
    print("Step 1: Finding padding length")
    
    # We need to modify the second-to-last block (block[2]) and test with last block (block[3])
    # to determine where the padding starts in the decrypted last block
    second_last_block = bytearray(cipherblocks[2])  # Make it mutable
    last_block = bytearray(cipherblocks[3])
    
    padding_length = 0
    
    # Check each byte position from right to left in the second-to-last block
    for i in range(BLOCKSIZE):  # Start from end (position 15 down to 0)
        # Save original byte
        original_byte = second_last_block[i]
        
        # Modify this byte (flip a bit to change the decryption)
        second_last_block[i] = original_byte ^ 0x01
        
        # Test if padding is still valid
        result = is_padding_okay(bytes(second_last_block), last_block)
        
        if result == 0:  # Bad padding!!! the start of padding
            padding_length = BLOCKSIZE - i
            print("Padding length:", padding_length)
            break
            
        # Restore original byte for next iteration
        second_last_block[i] = original_byte

    
    
    # Step 2: recover the last block
    print("Step 2: Recovering last block")
    last_block = bytearray(cipherblocks[3])
    delta_field = bytearray(BLOCKSIZE)
    ylist = []
    # # first let's find the lastbyte (Y in class notes)
    # # change the delta field to the form of b^b+1
    # for x in range(BLOCKSIZE - padding_length, 16):
    #     delta_field[x] = padding_length ^ (padding_length + 1)
    # for i in range(1,256):
    #     delta_field[BLOCKSIZE - padding_length - 1] = i
    #     for k in range(16):
    #         second_last_block[k] ^= delta_field[k]
    #     if is_padding_okay(second_last_block,last_block) == 1:
    #         print("success")
    #         y = i ^ padding_length + 1 #last byte of plaintext
    #         print(y)
    #         ylist.append(y)
    #     second_last_block = bytearray(cipherblocks[2])

   # whole block, using extended padding
   # example: delta_field[13] = 100^(b+2)
   # now we are gonna change b everytime we run it
    
#    # 1st loop:
#     delta_field = bytearray(BLOCKSIZE)

#     b = padding_length
#     for x in range(BLOCKSIZE - b, 16):
#         delta_field[x] = b ^ (b + 1 + 1)#loop
#     delta_field[BLOCKSIZE - b - 1] = 100 ^(b+1+1)#loop
        
#     for i in range(1,256):
#         delta_field[BLOCKSIZE - b - 1- 1] = i#loop
#         for k in range(16):
#             second_last_block[k] ^= delta_field[k]
#         if is_padding_okay(second_last_block,last_block) == 1:
#             print("success")
#             y = i ^ b + 1 +1 #last byte of plaintext,loop
#             print(y)
#             ylist.append(y)
#         second_last_block = bytearray(cipherblocks[2])
        
        
#     # 2nd loop
#     delta_field = bytearray(BLOCKSIZE)
#     b = padding_length
#     for x in range(BLOCKSIZE - b, 16):
#         delta_field[x] = b ^ (b + 1 + 2)#loop
#     #another loop here 
#     delta_field[BLOCKSIZE - b - 1] = 100 ^(b+1+2)#loop ylist[1-1]
#     delta_field[BLOCKSIZE - b - 2] = 101 ^(b+1+2)#ylist[2-1]
    
#     for i in range(1,256):
#         delta_field[BLOCKSIZE - b - 2 - 1] = i#loop
#         for k in range(16):
#             second_last_block[k] ^= delta_field[k]
#         if is_padding_okay(second_last_block,last_block) == 1:
#             print("success")
#             y = i ^ b + 1 + 2 #last byte of plaintext,loop
#             print(y)
#             ylist.append(y)
#         second_last_block = bytearray(cipherblocks[2])
        
        
        
    
    #to write the loop to finish reverting all the last block
    b = padding_length
    for loop in range(15):
        for x in range(BLOCKSIZE - b, 16):
            delta_field[x] = b ^ (b + 1 + loop)#loop
        #another loop here 
        for d_f in range(loop):
            delta_field[BLOCKSIZE - b - 1 - d_f] = ylist[d_f] ^(b+1+loop)#loop ylist[1-1]
                    
        for i in range(1,256):
            delta_field[BLOCKSIZE - b - loop - 1] = i#loop
            for k in range(16):
                second_last_block[k] ^= delta_field[k]
            if is_padding_okay(second_last_block,last_block) == 1:
                # print("success")
                y = i ^ b + 1 + loop #last byte of plaintext,loop
                print(y)
                ylist.append(y)
            second_last_block = bytearray(cipherblocks[2])
    
    print(ylist)
    
    # now we got a ylist of [100, 101, 116, 97, 99, 105, 116, 110, 101, 104, 116, 117, 97, 32]
    # later on we can print it out using:
    # for i in range(len(ylist)-1,-1,-1):
    #     print(ylist[i].to_bytes(1, 'little').decode(), end= "")
    
    
    # Step 3: Recover the other block, using padding length start from 0:
    # Step 3.1, second_last block
    print("Step 3.1: Recovering 2nd block")
    last_block = bytearray(cipherblocks[3])
    second_last_block = bytearray(cipherblocks[2])
    first_block = bytearray(cipherblocks[1])
    IV_block = bytearray(cipherblocks[0])
    ylist_2nd = []
    
    b = 0
    for loop in range(16):
        for x in range(BLOCKSIZE - b, 16):
            delta_field[x] = b ^ (b + 1 + loop)#loop
        #another loop here 
        for d_f in range(loop):
            delta_field[BLOCKSIZE - b - 1 - d_f] = ylist_2nd[d_f] ^(b+1+loop)#loop ylist[1-1]
                    
        for i in range(1,256):
            delta_field[BLOCKSIZE - b - loop - 1] = i#loop
            for k in range(16):
                first_block[k] ^= delta_field[k]
            if is_padding_okay(first_block,second_last_block) == 1:
                # print("success")
                y = i ^ b + 1 + loop #last byte of plaintext,loop
                print(y)
                ylist_2nd.append(y)
            first_block = bytearray(cipherblocks[1])
    print(ylist_2nd)
    # [101, 98, 32, 115, 121, 97, 119, 108, 97, 32, 100, 108, 117, 111, 104, 115]
    print("Step 3.2: Recovering 1st block")
    ylist_1st = []
    b = 0
    for loop in range(16):
        for x in range(BLOCKSIZE - b, 16):
            delta_field[x] = b ^ (b + 1 + loop)#loop
        #another loop here 
        for d_f in range(loop):
            delta_field[BLOCKSIZE - b - 1 - d_f] = ylist_1st[d_f] ^(b+1+loop)#loop ylist[1-1]
                    
        for i in range(1,256):
            delta_field[BLOCKSIZE - b - loop - 1] = i#loop
            for k in range(16):
                IV_block[k] ^= delta_field[k]
            if is_padding_okay(IV_block,first_block) == 1:
                # print("success")
                y = i ^ b + 1 + loop #last byte of plaintext,loop
                print(y)
                ylist_1st.append(y)
            IV_block = bytearray(cipherblocks[0])
    
    print(ylist_1st)
    # [32, 101, 100, 105, 115, 32, 114, 101, 118, 114, 101, 115, 32, 101, 104, 116]
    
    print("Answer is:")
    for i in range(len(ylist_1st)-1,-1,-1):
        print(ylist_1st[i].to_bytes(1, 'little').decode(), end= "")
    for i in range(len(ylist_2nd)-1,-1,-1):
        print(ylist_2nd[i].to_bytes(1, 'little').decode(), end= "")
    for i in range(len(ylist)-1,-1,-1):
        print(ylist[i].to_bytes(1, 'little').decode(), end= "")
    
    #answer: the server side should always be authenticated
    print()
    #disconnect from the padding oracle server
    oracle_disconnect()
