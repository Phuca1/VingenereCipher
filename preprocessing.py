import string
import nltk
from VigenereDecoder import *
from VigenereEncoder import *


def preprocess(data):
    a = {' ', '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
         '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    for i in range(10):
        for item in data:
            if item in a:
                data.remove(item)
        print(len(data))
    return data


def orginCipher(raw_data,cipher):
    fullcipher = list(raw_data).copy()
    alphabet = list(string.ascii_lowercase)
    ind = 0
    for i in range(len(fullcipher)):
        if fullcipher[i] in alphabet:
            fullcipher[i] = cipher[ind]
            ind += 1
    return fullcipher

file = open('data', 'r')
raw_data = file.read().lower()

data = list(raw_data)
data = preprocess(data)

print(data)
key = 'phuc'
keyList = list(key)

cipher = Encoder(data, keyList)
print(cipher)

fullcipher = orginCipher(raw_data,cipher)
print(list(raw_data))
print(fullcipher)
