import numpy as np
import string

apbInv = dict(zip(range(0, 26), string.ascii_lowercase))
apbs = dict(zip(string.ascii_lowercase, range(0, 26)))


def Encoder(plaintextList, key):
    index = []
    for i in range(len(plaintextList)):
        index.append(apbs[plaintextList[i]])
    indexKey = []
    for i in range(len(key)):
        indexKey.append(apbs[key[i]])
    cipher = []
    lenK = len(key)
    for i in range(len(plaintextList)):
        redun = i % lenK
        cipher.append(apbInv[(index[i] + indexKey[redun])%26])
    return cipher


# plainText = input('input ur plain text: ')
# key = input('input ur key')
#
# plaintextList = list(plainText)
# keyList = list(key)
# cipher = Encoder(plaintextList, keyList)
# print('cipher is: ')
# print((''.join(cipher)).upper())
