# Convert decimal number to binary and grey code value

print('Digit'+' '*7+'Binary'+' '*10+'Gray code')

round0 =[]
round1 =[]
round2 =[]
round3 =[]
round4 =[]
round5 =[]
round6 =[]
round7 =[]
round8 =[]

for i in range(361):
    length = 9 # Number of bits
    binary = str(bin(i))[2:].zfill(length) # Convert the digit to Binary

    si = binary.find('1') # start index
    if si==-1:
        si = length-1

    # Convert binary to grey scale
    a = binary[:si+1]

    # This part look like XOR Gate
    if si != length-1:
        for j in range(si+1,length):
            if [binary[j-1],binary[j]]==['1','1']:
                a += '0'

            elif [binary[j-1],binary[j]]==['0','0']:
                a += '0'

            else:
                a += '1'
                
    round0.append(a[0])
    round1.append(a[1])
    round2.append(a[2])
    round3.append(a[3])
    round4.append(a[4])
    round5.append(a[5])
    round6.append(a[6])
    round7.append(a[7])
    round8.append(a[8])
    # print the binary and greycode value corecponding to decimal value
    print(str(i)+' '*10+binary+' '*10+a)
    
round0str = ''.join(map(str,round0))
round1str = ''.join(map(str,round1))
round2str = ''.join(map(str,round2))
round3str = ''.join(map(str,round3))
round4str = ''.join(map(str,round4))
round5str = ''.join(map(str,round5))
round6str = ''.join(map(str,round6))
round7str = ''.join(map(str,round7))
round8str = ''.join(map(str,round8))

# print greycode value according to rounds
print('rund0 = ',round0str)
print()
print('rund1 = ',round1str)
print()
print('rund2 = ',round2str)
print()
print('rund3 = ',round3str)
print()
print('rund4 = ',round4str)
print()
print('rund5 = ',round5str)
print()
print('rund6 = ',round6str)
print()
print('rund7 = ',round7str)
print()
print('rund8 = ',round8str)



