"""
Caesar Cipher
"""
def encrypt(s):
    res = ""
    for i in s:
        c = chr(ord(i) + 4)
        if (i.islower() and ord(i)+4 > 97+26) or (i.isupper() and ord(i)+4 > 65+26):
            c = chr(ord(i) + 4 - 26)
        res += c
    return res

inputVal = input()
print(encrypt(inputVal))