import string


abc = 'abcdefghijklmnopqrstuvwxyz'
smeschenie = 3


def crypt(text):
    rez = ""
    for c in text:
        if c in abc:
            i = (abc.find(c) + smeschenie) % len(abc)
            rez += abc[i]
        else:
            rez += c
    return rez


def decrypt(text):
    rez = ""
    for c in text:
        if c in abc:
            i = (abc.find(c) - smeschenie) % len(abc)
            rez += abc[i]
        else:
            rez += c
    return rez


in_str = "hello world"
out_str=crypt(in_str)
print(in_str)
print(out_str)
print(decrypt(out_str))
