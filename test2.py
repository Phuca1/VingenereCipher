from VigenereDecoder import *
from VigenereEncoder import *
from preprocessing import *

raw_data = input_data()
data = list(raw_data)
data = preprocess(data)
print(data)

# key = input('Nhap vao key: ').lower()
# cipher = Encoder(data,key)
# print('Doan ma la: ')
# print(''.join(cipher))

plaintext = Prog(data)

for item in plaintext:
    print('text ban dau: ')
    print(''.join(orginCipher(raw_data, item)))