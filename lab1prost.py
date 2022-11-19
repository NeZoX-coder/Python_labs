import string

abc = 'abcdefghijklmnopqrstuvwxyz'
shift = abs(3)


def crypt(text):
    rez = ""
    for c in text:
        if c != " ":
            i = abc.find(c)
            i = (i + shift + len(abc)) % len(abc)
            rez = rez + abc[i]
        else:
            rez = rez + " "
    return rez


def decrypt(text):
    rez = ""
    for c in text:
        if c != " ":
            i = abc.find(c)
            i = (i - shift + len(abc)) % len(abc)
            rez = rez + abc[i]
        else:
            rez = rez + " "
    return rez


in_str = "helo world"
out_str=crypt(in_str)
print(in_str)
print(out_str)
print(decrypt(out_str))
