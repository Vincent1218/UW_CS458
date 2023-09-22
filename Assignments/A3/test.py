with open('p2p1', 'rb') as file1:
    data1 = file1.read()

with open('dist/ciphertext2', 'rb') as file2:
    data2 = file2.read()

print(data1)
print(data2)
