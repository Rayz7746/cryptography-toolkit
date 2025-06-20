# Explanation for the code

## Answer

`the server side should always be authenticated`



## Files

`answer.py` run for the final answer

`algorithm.py` run for how I get the answer(connecting to oracle)



## General Idea

This is my general idea of how I approach the answer, I also attached it in the comments of code as well:

General idea:
1. I should check from the end of the last block (`block[3]`), to see if the padding is correct. so that I can find the padding length. Just change one bit by one bit, and check if the padding is correct. I need to find the last bit that is not correct, and then I can find the padding length.
2. After I find the padding length, I can find the last byte of the block[3]. (By using `Y = i xor (b+1)`)
3. And Extend the padding to find other byte of the `block[3]`
4. Then I can find the bytes of `block[1]`, `block[2]`, using padding length = 0



## Step 1

```python
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
```



## Step 2 and 3

In order to write a loop to solve for the answer, I first tried to find the last unpadded byte to see the repeating patterns:

```python
# first let's find the lastbyte (Y in class notes)
# change the delta field to the form of b^b+1
for x in range(BLOCKSIZE - padding_length, 16):
    delta_field[x] = padding_length ^ (padding_length + 1)
for i in range(1,256):
    delta_field[BLOCKSIZE - padding_length - 1] = i
    for k in range(16):
        second_last_block[k] ^= delta_field[k]
    if is_padding_okay(second_last_block,last_block) == 1:
        print("success")
        y = i ^ padding_length + 1 #last byte of plaintext
        print(y)
    second_last_block = bytearray(cipherblocks[2])
```

And find the second last byte using extended padding, delta_field[13] = `last y value` xor (b+2):

```python
delta_field = bytearray(BLOCKSIZE)

b = padding_length #2
for x in range(BLOCKSIZE - b, 16):
    delta_field[x] = b ^ (b + 1 + 1)#loop
delta_field[BLOCKSIZE - b - 1] = 100 ^(b+1+1)#loop

for i in range(1,256):
    delta_field[BLOCKSIZE - b - 1- 1] = i#loop
    for k in range(16):
        second_last_block[k] ^= delta_field[k]
    if is_padding_okay(second_last_block,last_block) == 1:
        print("success")
        y = i ^ b + 1 +1 #last byte of plaintext,loop
        print(y)
    second_last_block = bytearray(cipherblocks[2])
```

And then the third last byte:

```python
delta_field = bytearray(BLOCKSIZE)
b = padding_length
for x in range(BLOCKSIZE - b, 16):
    delta_field[x] = b ^ (b + 1 + 2)#loop
#another loop here 
delta_field[BLOCKSIZE - b - 1] = 100 ^(b+1+2)#loop ylist[1-1]
delta_field[BLOCKSIZE - b - 2] = 101 ^(b+1+2)#ylist[2-1]

for i in range(1,256):
    delta_field[BLOCKSIZE - b - 2 - 1] = i#loop
    for k in range(16):
        second_last_block[k] ^= delta_field[k]
    if is_padding_okay(second_last_block,last_block) == 1:
        print("success")
        y = i ^ b + 1 + 2 #last byte of plaintext,loop
        print(y)
    second_last_block = bytearray(cipherblocks[2])
```

I commented on the code that will change each loop to find the pattern. In order to track the correct answer, I created a `ylist`:

```python
ylist = []
b = padding_length # = 2
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
```

`d_f` represent for delta_field index difference



## Step 4

Then just make padding equal 0 and start the same loop for first and second block:

```python
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
```

