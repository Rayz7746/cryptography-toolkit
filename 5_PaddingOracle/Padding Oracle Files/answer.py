# Raymond Zha

ylist3 = [100, 101, 116, 97, 99, 105, 116, 110, 101, 104, 116, 117, 97, 32]
ylist2 = [101, 98, 32, 115, 121, 97, 119, 108, 97, 32, 100, 108, 117, 111, 104, 115]
ylist1 = [32, 101, 100, 105, 115, 32, 114, 101, 118, 114, 101, 115, 32, 101, 104, 116]


for i in range(len(ylist1)-1,-1,-1):
    print(ylist1[i].to_bytes(1, 'little').decode(), end= "")
for i in range(len(ylist2)-1,-1,-1):
    print(ylist2[i].to_bytes(1, 'little').decode(), end= "")
for i in range(len(ylist3)-1,-1,-1):
    print(ylist3[i].to_bytes(1, 'little').decode(), end= "")
    
# answer: the server side should always be authenticated