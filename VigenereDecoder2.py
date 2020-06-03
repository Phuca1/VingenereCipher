import numpy as np
import string

# chuyen tu so sang chu cai
apbInv = dict(zip(range(0, 26), string.ascii_lowercase))
# chuyen tu chu cai sang so
apbs = dict(zip(string.ascii_lowercase, range(0, 26)))

# ti le xuat hien cua cac chu cai trong tieng anh theo thu tu nho dan:
THEORETICAL_FREQUENCIES = [12.7, 9.06, 8.17, 7.51, 6.97, 6.75, 6.33, 6.09, 5.99, 4.25, 4.02, 2.78, 2.76,
                           2.41, 2.36, 2.23, 2.01, 1.97, 1.93, 1.49, 0.99, 0.77, 0.15, 0.15, 0.09, 0.07]

ALPHABET_SORTED_BY_FREQUENCY = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u',
                                'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

let = dict(zip(ALPHABET_SORTED_BY_FREQUENCY, THEORETICAL_FREQUENCIES))
sorted_let = sorted(let.items(), key=lambda x: x[0])  # sort lai ti le xuat hien cac chu cai theo alphabet


def nCk(n, k):  # tinh nCk
    c = 1
    for i in range(1, k + 1):
        c = int(c * (n + 1 - i) / (i))
    return c


def counting(textList):  # tinh so lan xuat hien cua cac chu cai trong 1 doan text
    count = []
    for item in range(26):
        c = 0
        for t in textList:
            if apbInv[item] == t:
                c += 1
        count.append(c)
    return count


def calculateIC(letterList):  # letterList la cac chu cai lay ra tai k mod n/ ham nay dung de tinh chi so IC cua 1 doan text
    letter = counting(letterList)
    sumUp = 0
    textLen = len(letterList)
    for i in letter:
        sumUp += nCk(i, 2)
    IC = sumUp / nCk(textLen, 2)
    return IC


def calculateKeyLen(textList):  # tinh ra toan bo do dai khoa co the
    m = 1
    maxLen = len(textList)
    ICList = []
    while m < 50:
        print("voi m = ", m)
        div = int(maxLen / m)
        IC = []
        for i in range(m):
            letterList = []
            for j in range(div + 1):
                if (i + (j * m)) <= (maxLen - 1):
                    letterList.append(textList[i + (j * m)])
            IC.append(calculateIC(letterList))
        ICs = np.asarray(IC)
        print(np.mean(ICs))
        ICList.append(np.mean(ICs))
        m += 1
    ICList = np.asarray(ICList)
    return (ICList.argsort()[-3:]+1)


def crackingCaesarCipher(listText):  # encrypte Caesar
    index = []
    for i in listText:  # lay chi so cua cac chu cai
        index.append(apbs[i])
    cost = []
    for t in range(26):  # thu shift tung key mot
        ind = index.copy()
        for i in range(len(ind)):
            ind[i] = (ind[i] + t) % 26
        text = []
        for i in range(len(ind)):
            text.append(apbInv[ind[i]])

        coincidence = counting(text)  # dem so lan lap cua cac chu cai
        coin = np.asarray(coincidence)
        sums = np.sum(coin)
        perc = (coin * 100) / sums  # tinh ti le xuat hien cua cac chu cai
        loss = 0
        for i in range(len(coin)):
            loss += np.abs(perc[i] - sorted_let[i][1])
        cost.append(loss)
    Cost = np.asarray(cost)
    key = np.argmin(Cost)  # lay ra key ma cost nho nhat

    # chuyen key tu so ve chu cai
    keyText = apbInv[(26 - key) % 26]

    # chuyen ciphertext ve plaintext
    plaintext = []

    ind = index.copy()
    for i in range(len(ind)):
        ind[i] = (ind[i] + key) % 26
    for i in range(len(ind)):
        plaintext.append(apbInv[ind[i]])
    return (plaintext, keyText)


def crackingVigenereCipher(listText, keyLen):  # encrypt Vigenere
    letters = [[] for x in range(keyLen)]
    crackedCipher = [[] for x in range(keyLen)]
    keys = []
    for i in range(keyLen):  # chia text thanh keyLen phan va pha ma tung phan mot
        for j in range(i, len(listText), keyLen):
            letters[i].append(listText[j])
            # letter[i] bay gio da la mot Ceasar  Cipher
        (crackedCipher[i], key) = crackingCaesarCipher(letters[i])
        keys.append(key)

    # chuyen ciphertext ve plaintext
    plaintext = []

    for i in range(len(letters[keyLen - 1])):
        for j in range(keyLen):
            plaintext.append(crackedCipher[j][i])

    redundance = len(listText) - (len(letters[keyLen - 1]) * keyLen)
    print(redundance)
    if redundance > 0:
        for i in range(redundance):
            plaintext.append(crackedCipher[keyLen - 1][i])
    return (plaintext, keys)


def Prog(mylist):
    # text = input("input ur vigenere cipher text: ")
    #
    # mylist = list(text.lower())

    keyLen = calculateKeyLen(mylist)
    print(keyLen)

    for item in keyLen:
        (plaintext, key) = crackingVigenereCipher(mylist, item)
        print('voi chieu dai khoa = ', item)
        print(string.ascii_lowercase)
        print(''.join(key))
        print(''.join(plaintext))

data = input().lower()
mylist = list(data)
Prog(mylist)