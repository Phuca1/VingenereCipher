import string
import nltk
from VigenereDecoder import *
from VigenereEncoder import *
import tkinter as tk
from tkinter import filedialog

def input_data():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file = open(file_path,'r')
    raw_data = file.read().lower()
    return raw_data

def preprocess(data): #loai bo cac ki tu dac biet
    a = {' ', '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
         '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    for i in range(20):
        for item in data:
            if item in a:
                data.remove(item)
    return data


def orginCipher(raw_data,cipher): #Tra cipher ve trang thai ban dau (them cac ki tu dac biet vao nhu cu)
    fullcipher = list(raw_data)
    alphabet = list(string.ascii_lowercase)
    ind = 0
    for i in range(len(fullcipher)):
        if fullcipher[i] in alphabet:
            fullcipher[i] = cipher[ind]
            ind += 1
    return fullcipher


# raw_data = input_data()
# data = list(raw_data)
# data = preprocess(data)
#
# key = input('Nhap vao key: ').lower()
# cipher = Encoder(data,key)
# print('Doan ma la: ')
# print('chieu dai cua cipher: ')
# print(len(cipher))
#
# plaintext = Prog(cipher)
# # print('chieu dai plain text: ',len(plaintext[0]))
# for item in plaintext:
#     print('text ban dau: ')
#     print(''.join(orginCipher(raw_data, item)))

# file = open('data', 'r')
# raw_data = file.read().lower()
#
# data = list(raw_data)
# data = preprocess(data)
#
# print(data)
# key = 'phuc'
# keyList = list(key)
#
# cipher = Encoder(data, keyList)
# print(cipher)
#
# fullcipher = orginCipher(raw_data,cipher)
# print(list(raw_data))
# print(fullcipher)

# Prog(cipher)