import string

abc1 = 'abcdefghijklmnopqrstuvwxyz'
abc2 = 'qrstuvwxyzabcdefghijklmnop'
smeschenie = 3


def crypt(text):
    shift = abs(smeschenie)
    rez = ""
    for c in text:
        if c != ' ':
            # i = abc1.index(c)
            i = (abc1.index(c) + shift) % len(abc1)
            rez += abc1[i]
            shift = abc1.index(rez[-1])
            # shift = abs(abc2.index(rez[-1]) - 26)
        else:
            rez += " "
    return rez


def decrypt(text):
    shift = abs(smeschenie)
    rez = ""
    for c in text:
        if c != ' ':
            # i = abc1.index(c)
            i = (abc1.index(c) - shift) % len(abc1)
            rez += abc1[i]
            shift += abc1.index(rez[-1])

        else:
            rez += " "
    return rez


in_str = "hello world"
print(in_str)
out_str = crypt(in_str)
print(out_str)
out_str = decrypt(out_str)
print(out_str)
