from collections import Counter
a = dict(zip('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', [0] * 33))
abc = 'оаниетрсвлмкпгыбяудйчэцхзьщшжюфъё'
text = 'шцагщг иахшцкихпг м агюбцгэ ы бюпгшцх гцбэщбу фщъайъцхмх ы мбщжъ 1940-е йй. иах гмцхыщбэ клгшцхх клъщче, хээхйахабыгытхе хё йъаэгщхх. ш шгэбйб щглгпг акмбыбьшцыб гайъщцхщч шцаъэхпбшо ьбюхцошд ы дьъащбу бюпгшцх эгмшхэгпощбу щъёгыхшхэбшцх, иах мбцбабу ыбёэбрщб бьщбыаъэъщщбъ агёыхцхъ гцбэщбу фщъайъцхмх х щгклщб-цъещхлъшмбйб ибцъщжхгпг ы бюпгшцх дьъащбйб цбипхыщбйб жхмпг (дцж), ьбпйбъ ыаъэд бшцгыпдд бцмачцчэ ыбиабш ъйб хшибпоёбыгщхд ы ыбъщщче жъпде.ы 1953 й. ы гайъщцхщъ щглгпхшо агюбцч иб иабэчтпъщщбу ьбючлъ кагщг. ёг 1958–1972 йй. ючпх ыыъьъщч ы фмшипкгцгжхн лъцчаъ хшшпъьбыгцъпошмхе аъгмцбаг, бьхщ хё мбцбаче ючп хэибацхабыгщ хё штг, бшцгпощчъ шмбщшцакхабыгщч х ибшцабъщч шбюшцыъщщчэх шхпгэх. ы 1969 й. ы фшъушъ, ы 40 мэ бц шцбпхжч гайъщцхщч юкфщбш-гуаъшг, ючпг икяъщг пгюбагцбащгд кшцгщбымг иб агьхбехэхлъшмбу иъаъагюбцмъ бюпклъщщбйб дьъащбйб цбипхыг (бдц), щб ы 1973 й. ибшпъ ычьъпъщхд бм. 1 мй ипкцбщхд бщг ючпг ьъэбщцхабыгщг. ы 1974 й. ы пхэъ, ы 100 мэ м шъыъак бц юкфщбш-гуаъшг, ючпг икяъщг иъаыгд гцбэщгд фпъмцабшцгщжхд (гфш) «гцклг-1», ибшцабъщщгд иах ибэбях щъэъжмбу мбэигщхх «шхэъщш». гфш ючпг шбёьгщг щг бшщбыъ цдръпбыбьщ йб аъгмцбаг щг иахабьщбэ кагщъ фпъмцахлъшмбу �� эбящбшцон 357 эыц.',
# text.split()
counter = Counter(str(text))
new_counter = dict()
for key, value in counter.items():
    if key in abc:
        new_counter[key] = value
sorted_counter = sorted(new_counter.items(), key=lambda x: x[1], reverse=True)
print(counter)
print(new_counter, '\n', len(new_counter), '\n')
print(sorted_counter)
letters_letters = dict()
arr_new_adc = ''
for i in range(len(sorted_counter)):
    letters_letters[sorted_counter[i][0]] = abc[i]
print(letters_letters)
print(letters_letters['б'])
# print(dict(zip(sorted_counter[1:1], arr_new_adc,abc)))
