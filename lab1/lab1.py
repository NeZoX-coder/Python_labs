
abc1 = 'abcdefghijklmnopqrstuvwxyz'
abc2 = 'qrstuvwxyzabcdefghijklmnop'
smeschenie = 3


def crypt(text):
    shift = smeschenie
    rez = ""
    for i in text:
        if i != ' ':
            i = (abc1.index(i) + shift) % len(abc1)
            rez += abc2[i]
            shift = abc2.index(rez[-1])
        else:
            rez += " "
    return rez


def decrypt(text):
    shift = smeschenie
    rez = ""
    for i in text:
        if i != ' ':
            i = (abc2.index(i) - shift) % len(abc1)
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
