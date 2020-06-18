from VigenereEncoder import *
from VigenereDecoder import *
import tkinter as tk
from tkinter import filedialog

def input_data():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file = open(file_path,'r')
    raw_data = file.read().lower()
    return raw_data

cipher = input('input ur cipher text: ').lower()

# cipher = input_data()
cipherList = list(cipher)

Prog(cipherList)