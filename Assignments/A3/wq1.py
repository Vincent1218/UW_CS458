with open('dist/ciphertext1', 'rb') as file1:
    data1 = file1.read()

with open('dist/ciphertext2', 'rb') as file2:
    data2 = file2.read()


# ASCII char : 32 - 126
# 0x20 - 0x7E
# Maxinum difference between two bytes is = 94

hex_data1 = hex_data2 = ''
sub_data = ''
sub_arr = []

print(len(data1))

n = len(data1)


for i in range(n):
    # print(data1[i], data2[i], data2[i] - data1[i], ((data2[i] - data1[i]) % 256))
    sub_arr.append((data2[i] - data1[i]))
    sub_data += hex((data2[i] - data1[i]) % 256)[2:].zfill(2)
    
print(sub_data)


# Write binary data to a file
with open('p2p1', 'wb') as file:
    file.write(bytes.fromhex(sub_data))


for i in range(n):
    if (sub_arr[i] > 94):
        sub_arr[i] = sub_arr[i] - 256
    elif (sub_arr[i] < -94):
        sub_arr[i] = sub_arr[i] + 256


test_arr = [" the ", " be ", " to ", " of ", " and ", " a " ," in ", " that ", " have ", " I ", " it ", " for "]
test_arr = ["United States"]
# test_arr = ["the age of 19. "]


print(sub_arr)

for x in test_arr:
    length = len(x)
    print(x)
    print("cipher1", x)
    for i in range(n-length+1):
        valid = True
        for j in range(length):
            if (sub_arr[i+j] + ord(x[j]) >= 32 and sub_arr[i+j] + ord(x[j]) <= 126):
                pass
            else:
                valid = False
                break
        if (valid):
            print(i, end=': ')
            for j in range(length):
                print(chr(sub_arr[i+j] + ord(x[j])), end='')
            print()
            for j in range(length):
                print(sub_arr[i+j], end=', ')
            print()
    print("cipher2", x)
    for i in range(n-length+1):
        valid = True
        for j in range(length):
            if (ord(x[j]) - sub_arr[i+j] >= 32 and ord(x[j]) - sub_arr[i+j] <= 126):
                pass
            else:
                valid = False
                break
        if (valid):
            print(i, end=': ')
            for j in range(length):
                print(chr(ord(x[j]) - sub_arr[i+j]), end='')
            print()
            for j in range(length):
                print(sub_arr[i+j], end=', ')
            print()



# print(sub_arr)
# print(max(sub_arr))
# print(min(sub_arr))



