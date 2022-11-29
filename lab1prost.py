import string


abc = 'abcdefghijklmnopqrstuvwxyz'
smeschenie = 3

def crypt(text):
    rez = ""
    for i in text:
        if i in abc:
            i = (abc.find(i) + smeschenie) % len(abc)
            rez += abc[i]
        else:
            rez += i
    return rez


def decrypt(text):
    rez = ""
    for i in text:
        if i in abc:
            i = (abc.find(i) - smeschenie) % len(abc)
            rez += abc[i]
        else:
            rez += i
    return rez


in_str = "hello world"
out_str=crypt(in_str)
print(in_str)
print(out_str)
print(decrypt(out_str))
