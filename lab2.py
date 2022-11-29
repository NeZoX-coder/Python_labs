from collections import Counter

arr_abc = [
    'оианевстркядмылбпхгучзйьжшюцщъэфё',
    'оаниетрсвлмкпгыбяудйчэцхзьщшжюфъё',
    'оинесартвкляпдмыугхчбйжзюцьфэшщъё',
    'оеитнарсвядлкмпзыугчьхйжбцэфюшщъё',
    'оиасетнрлвкдпягмйыьзбуэцчюхжщшфъё'
]

arr_sentences = [
    'обнмчшйчшенчё мса амнбчцжц вмнбыуршчуа рнбцалчцжц обцлурчущш у бньнчуа влбшлнжуенвщую, цонбшлурчц-влбшлнжуенвщую у цонбшлурчёю йшмше чш щцчлучнчлшсхчёю, цщншчвщую (гцбвщую) лншлбшю рцнччёю мнэвлруэ (лрм) у чш цлмнсхчёю влбшлнжуенвщую (цонбшяуцччёю) чшобшрснчуаю. арсазлва ешвлхз «амнбчцэ лбушмё». щ цвчцрчёг оцлнчяушсхчёг йшмшешг швав цлчцвалва: чшчнвнчун бшщнлчцдцгдцрёю фмшбцр оц цдтнщлшг обцлурчущш чш йчшеулнсхчёю фмшснчуаю цл шибцмбцгцр дшйубцршчуа, цднвоненчун оцммнбыщу в рцймфюш вус цдкнжц чшйчшенчуа (вцч) у мб. швав веулшзлва жудщуг вбнмвлрцг щшщ жсцдшсхчцжц, лшщ у бнжуцчшсхчцжц вмнбыуршчуа рнбцалчёю обцлурчущцр, гцжфл обугнчалхва рц рвню румшю рцэч у щцчъсущлцр (щшщ амнбчёю, лшщ у цдёечёю). швав угнзлва р вцвлшрн ррв бцввуу, вьш у щулша.р вьш цвчцрф швав вцвлшрсазл лаынсён (влбшлнжуенвщун) дцгдшбмубцркущу (лд, вг. лаынсёэ дцгдшбмубцркущ) р-52ч у р-2ш, врнмнччён р 5 шрушщбёсхнр р вцвлшрн 8-э у 12-э рцймфьчёю шбгуэ, щцлцбён шмгучувлбшлурчц оцмеучнчё дцнрцгф шрушяуцччцгф щцгшчмцршчуз ррв вьш. чш рццбфынчуу лд чшюцмалва щбёсшлён бшщнлё (вг. щбёсшлша бшщнлш) рцймфьчцжц дшйубцршчуа (щбрд) дцсхьцэ мшс чцвлу (р амнбчцг у чнамнбчцг цвчшкнчуу) у шрушдцгдё. р фвсцруаю �� губчцжц рбнгнчу дцнрцн мныфбвлрц влбшлнжуенвщцэ дцгдшбмубцрцечцэ шрушяунэ (вдш) вьш чн цвфкнвлрсанлва. в янсхз оцммнбышчуа обшщлуенвщую чшрёщцр снлчцжц вцвлшрш цбжшчуйфзлва оцснлё оц осшчшг дцнрцэ оцмжцлцрщу. р фжбцышнгёэ онбуцм бшйрулуа рцнччц-оцсулуенвщцэ цдвлшчцрщу усу р щбуйувчёю вулфшяуаю вдш онбнмшнлва р цонбшлурчцн оцмеучнчун цдтнмучнччцгф влбшлнжуенвщцгф щцгшчмцршчуз рццбфынччёю вус (рв) вьш усу щцгшчмфзкнгф цдтнмучнччцжц щцгшчмцршчуа чш лрм. цвчцрчён чшобшрснчуа бшйрулуа вав рв вьш: гцмнбчуйшяуа у обцмснчун �� вбцщш ищвосфшлшяуу лд р-52ч у р-2ш; обучалун чш рццбфынчун чцрёю луоцр рёвцщцлцечёю щбрд, шрушдцгд у лд чцрцжц оцщцснчуа щ 2040 ж.',
    'шцагщг иахшцкихпг м агюбцгэ ы бюпгшцх гцбэщбу фщъайъцхмх ы мбщжъ 1940-е йй. иах гмцхыщбэ клгшцхх клъщче, хээхйахабыгытхе хё йъаэгщхх. ш шгэбйб щглгпг акмбыбьшцыб гайъщцхщч шцаъэхпбшо ьбюхцошд ы дьъащбу бюпгшцх эгмшхэгпощбу щъёгыхшхэбшцх, иах мбцбабу ыбёэбрщб бьщбыаъэъщщбъ агёыхцхъ гцбэщбу фщъайъцхмх х щгклщб-цъещхлъшмбйб ибцъщжхгпг ы бюпгшцх дьъащбйб цбипхыщбйб жхмпг (дцж), ьбпйбъ ыаъэд бшцгыпдд бцмачцчэ ыбиабш ъйб хшибпоёбыгщхд ы ыбъщщче жъпде.ы 1953 й. ы гайъщцхщъ щглгпхшо агюбцч иб иабэчтпъщщбу ьбючлъ кагщг. ёг 1958–1972 йй. ючпх ыыъьъщч ы фмшипкгцгжхн лъцчаъ хшшпъьбыгцъпошмхе аъгмцбаг, бьхщ хё мбцбаче ючп хэибацхабыгщ хё штг, бшцгпощчъ шмбщшцакхабыгщч х ибшцабъщч шбюшцыъщщчэх шхпгэх. ы 1969 й. ы фшъушъ, ы 40 мэ бц шцбпхжч гайъщцхщч юкфщбш-гуаъшг, ючпг икяъщг пгюбагцбащгд кшцгщбымг иб агьхбехэхлъшмбу иъаъагюбцмъ бюпклъщщбйб дьъащбйб цбипхыг (бдц), щб ы 1973 й. ибшпъ ычьъпъщхд бм. 1 мй ипкцбщхд бщг ючпг ьъэбщцхабыгщг. ы 1974 й. ы пхэъ, ы 100 мэ м шъыъак бц юкфщбш-гуаъшг, ючпг икяъщг иъаыгд гцбэщгд фпъмцабшцгщжхд (гфш) «гцклг-1», ибшцабъщщгд иах ибэбях щъэъжмбу мбэигщхх «шхэъщш». гфш ючпг шбёьгщг щг бшщбыъ цдръпбыбьщ йб аъгмцбаг щг иахабьщбэ кагщъ фпъмцахлъшмбу �� эбящбшцон 357 эыц.',
    'жфяюфялав уфяда ъ вяиелфй злиекиымшиъдфй щъыалфюдфй. ажу жфяеаряиувтыъв ла ъыеаыикмшиъдми м слфкфпиуиюци.д ъыеаыикмшиъдмс фылфъвыъв ажу, фълфюлцс юффещнилмис дфыфецх вюувтыъв чауумъымшиъдми еадиыц ъыеаыикмшиъдфкф ларлашилмв (чежу). ю сфеъдмх ъыеаыикмшиъдмх вяиелцх ъмуах (съвъ) юффещниллцх ъму (юъ) ег жемлвыф мъжфуьрфюаыь ыиесмл «еадиылцй жфяюфялцй деийъие ъыеаыикмшиъдфкф ларлашилмв» (еждъл). ю юфиллф-сфеъдмх ъмуах (юсъ) ъёа м яещкмх кфъщяаеъыю щжфыеичувиыъв ыиесмл «аыфслав жфяюфялав уфяда ъ чауумъымшиъдмсм еадиыасм» (жуаеч). флм жеияларлашилц яу�� жфеанилмв юанлцх юфиллф-аясмлмъыеаымюлцх пилыефю, жщлдыфю щжеаюуилмв, кещжжмефюфд юффещниллцх ъму жефымюлмда, юфиллф сфеъдмх чар, жфеыфю м яе., фъщбиъыюувв жуаюалми ю утчцх еайфлах смефюфкф фдиала ъдецылф, ли юъжуцюав ю лаяюфялфи жфуфнилми.еждъл м жуаеч жемсилвтыъв дад ъасфъыфвыиуьлф, ыад м ю ъфъыаюи кещжжмефюфд съвъ м еарлфефялцх ъму. сфкщы мсиыь ла юффещнилмм зггидымюлци ъеияъыюа чфеьчц ъ жефымюфуфяфшлцсм ъмуасм жефымюлмда, ъеияъыюа лачутяилмв, ъюврм м щжеаюуилмв, лаюмкапмм, юфъжеибилмв лиъалдпмфлмефюаллфкф яфъыщжа д еадиылф-вяиелфсщ фещнмт, яещкми еаямфзуидыефллци юцшмъумыиуьлци м ыихлмшиъдми ъеияъыюа. ъыеаыикмшиъдми ажу вюувтыъв фълфюлфй чфиюфй иямлмпий м щяаелцс дфсжфлилыфс съвъ м ъфъыфвы ла юффещнилмм юсг ефъъмм, юсъ ъёа, юиумдфчемыалмм, геалпмм м дмыав.',
    'чъуэлбх юрбэёдщябжп йдуэл скрёбжхж идёскд, ьвщайрблр ь вжбуэёъвюла скрёбжхж идёскд (си) вжеодвэбжхж крпэрёлпэёлэлрьжхж (d-t) ъищд. ожувжщявъ ь си ътр ьувжёр ожущр кжуэлтрблс бдквёлэлйбжуэл крщсцeхжус едэрёлдщд (ке, уе. крщсцлрус едэрёлдщн) ь оёжюруур юробжп ёрдвюлл крщрблс ежхъэ кжуэлхдэяус эреорёдэъён ожёсквд 107°у л кдьщрблр 108…109 дэе., ь гэлм ъущжьлсм ежхъэ оёжлумжклэя эрёежскрёбнр ёрдвюлл. оёл оёжэрвдблл ёрдвюлл d-э-улбэрид леоъщяубж ьнкрщсаэус ьнужвжгбрёхрэлйрувлр (14,7 егь) брпэёжбн, вжэжёнр гззрвэльбж ёдуцрощсаэ скёд ке.ч. юрбэёдщябжп йдуэл идёскд эдщж ьдтбне фдхже ьорёрк оёл �� ужьрёфрбуэьжьдблл скрёбжхж жёътлс (сж). ьж-орёьнм, ч. ибдйлэрщябж ъьрщлйльдрэ гззрвэльбжуэя луожщяижьдблс ке. ь йлуэж крщлэрщябнм идёскдм гззрвэльбжуэя жхёдблйрбд ужуэжсблре вёлэлйбжуэл ке. бдщлйлр тр оёл ч. си «ьбрфблм» эрёежскрёбнм брпэёжбжь крщдрэ ёртле ухжёдблс ке едщжйъьуэьлэрщябне в рхж ужуэжсбла, д вжщлйруэьж рхж ёдуцрольфлмус скрё ёривж ьжиёдуэдрэ. ьж-ьэжёнм, бдщлйлр ч. ожьнфдрэ ъуэжпйльжуэя гбрёхжьнкрщрблс си в оёркрэжбдюлл, йэж ожьнфдрэ оёркувдиърежуэя жубжьбнм мдёдвэрёлуэлв идёскд (йэж ь жужчрббжуэл ьдтбж кщс орёьлйбнм крщлэрщябнм ъищжь уэдклпбжхж эрёежскрёбжхж жёътлс). оёлербрблр ч. эдвтр ьдтбж кщс ожьнфрблс гззрвэльбжуэл сж ь ъущжьлсм ьжикрпуэьлс бд брхж уёркуэь скрёбжп оёжэльжёдврэбжп жчжёжбн (оёж) ид уйрэ жущдчщрблс йъьуэьлэрщябжуэл си в ьжиблвдацреъ оёл гэже ь ке зжбъ идодикньдацлм брпэёжбжь.',
    '24 юхпзкиек 1969 т. юэеэк жогхеаэуо йевнхрёеф, югкжоппфх ю еозэдэмонэхы рвтвгвео в пхеоюйевюзеопхпээ крхепвтв веёъэк (рпкв). юйёюзк ивухх 22 ухз, 18 щок 1992 т. рук юэеээ гюзёйэув г юэуё ювтуоахпэх в гюхвибхщуяшэц тоеопзэкц щотозь. г 1976 т. ифуо вюпвгопо юэеэыюмок мвщэююэк йв озвщпвы ьпхетээ (юмоь), врпвы эж нхухы мвзвевы ифув эжёсхпэх гвжщвъпвюзэ юзевэзхучюзго по зхееэзвеээ юзеопф озвщпвы ьухмзевюзопнээ (оью). г посоух 1980-ц тт. юэеэыюмок юзвевпо йевгврэуо йхехтвгвеф ю деопнэхы в юзевэзхучюзгх ахюзэ ьпхетвиувмвг щвшпвюзчя 600 щгз моърфы. йуопэевгоувюч, сзв йхегфы ехомзве иёрхз жойёшхп г 1991 т. врпомв юрхумо зом э пх ифуо жогхеахпо.пхвицврэщвюзч ювжропэк понэвпоучпвы иожф рук йвртвзвгмэ юйхнэоуэюзвг г виуоюзэ озвщпвы ьпхетхзэмэ жоюзогэуо юмоь жопкзчюк йвэюмвщ юзеопф, мвзвеок йвюзогэуо иф эююухрвгозхучюмэы ехомзве г юэеэя. г 1991 т. г мэзох йеэ юврхыюзгээ щотозь ифу йеэвиехзхп щэпэозяепфы эюзвспэм пхызевпвг щвшпвюзчя 30 мгз, мвзвефы ю 1998 т. йеэщхпкхзюк рук йевэжгврюзго юзоиэучпфц эжвзвйвг, эюйвучжёяшэцюк г щхрэнэпх, о зомъх рук эжёсхпэк пхызевппфц цоеомзхеэюзэм. йоеоуухучпв юмоь йевгврэуэюч йхехтвгвеф ю оетхпзэпвы в йвмёймх ухтмвгврпвтв эююухрвгозхучюмвтв ехомзвео щвшпвюзчя 10 щгз. врпомв йвр рогухпэхщ юв юзвевпф юао э эжеоэук юрхумо зом э пх ювюзвкуоюч. г 1995–1999 тт. евююэхы э юэеэхы виюёъроуюк гвйевю юзевэзхучюзго г йвюухрпхы поёспв-эююухрвгозхучюмвтв нхпзео ю ухтмвгврпфщ крхепфщ ехомзвевщ щвшпвюзчя 25 щгз, о зомъх оью. врпомв йв еожпфщ йеэсэпощ йеомзэсхюмвтв еожгэзэк ьзэ виюёърхпэк пх йвуёсэуэ.'
]


def decode_abc(abc, sentences):
    letters = Counter(str(sentences))
    only_letters = dict()
    for key, value in letters.items():
        if key in abc:
            only_letters[key] = value
    sorted_letters = sorted(only_letters.items(), key=lambda x: x[1], reverse=True)
    letters_letters = dict()
    for i in range(len(sorted_letters)):
        letters_letters[sorted_letters[i][0]] = abc[i]
    return letters_letters


def decode_sentences(text, abc_old_new):
    rez = ""
    for i in text:
        if i in abc_old_new.keys():
            rez += abc_old_new[i]
        else:
            rez += i
    return rez


number = 4

a = decode_abc(arr_abc[number], arr_sentences[number])
print(a)
print(decode_sentences(arr_sentences[number], a))
