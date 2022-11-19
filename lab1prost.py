import string

abc = 'abcdefghijklmnopqrstuvwxyz'
smeschenie = abs(3)


def crypt(text):
    rez = ""
    for c in text:
        if c != " ":
            i = abc.find(c)
            i = (i + smeschenie) % len(abc)
            rez += abc[i]
        else:
            rez += " "
    return rez


def decrypt(text):
    rez = ""
    for c in text:
        if c != " ":
            i = abc.find(c)
            i = (i - smeschenie) % len(abc)
            rez += abc[i]
        else:
            rez += " "
    return rez


in_str = "hello world"
out_str=crypt(in_str)
print(in_str)
print(out_str)
print(decrypt(out_str))
