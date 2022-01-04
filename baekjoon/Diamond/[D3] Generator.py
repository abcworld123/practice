import sys
print = sys.stdout.write


def my0():
    print('ONTAK 2010\n')



def my1():
    txt = 'Godzilla terrorizes Bajtoly lower again. Every day a monster comes out of the ocean, slow movement of marching through the city to some of the skyscrapers and eats it with people who are in it. Eating one skyscraper takes the whole day, at dusk, it returns to its hiding place hidden in the depths. To make matters worse, going through the city, Godzilla wags its tail and destroys towers, near the passes. The prospect of becoming a meal for an underwater monster, to discourage some residents spent in uncomfort- tion in the city. During the night of each tower is derived as a resident and flees to the countryside. In Bajtogrodzie skyscrapers were built only at street crossings. At each intersection there is exactly one building. Junctions are connected by two-way streets. In addition, a the junction is just above the ocean, this is where Godzilla begins its destructive journey through the city. During the investigation, the monster moves only in the streets. Godzilla noted that he must hurry up with the consumption of residents and carefully choose the skyscrapers devouring and streets, which reaches them. Of course, choosing never previously consumed or destroyed- wanego skyscraper. What is the maximum number of people who can eat before the city completely desolate? Entrance The first line of standard input contains two integers him (1 n 100 000, 0 500 000 m) respectively denoting the number of intersections in the city and the number of connecting streets. Crossroads numbers are numbered from 1 to n, junction 1 is located on the shores of the ocean. Next row contains a sequence of integers n s (0 s 100 000) to describe population skyscrapers at various intersections. In each of the next m rows are the two integers ai and bi (1 ai, bi n, ai = bi), which means that there is a road junction connecting ai and bi. The crossing number One can reach any other intersection in the city. Exit Write to stdout the number of people who eat Godzilla for the optimum choice of meals and roads through the city every day. Example For input: the result is correct: 5 5 11 1 3 2 4 7 1 2 1 3 2 3 2 4 3 5'
    cur = 2932
    for i in range(len(txt)):
        print(txt[i] * cur)
        cur = (cur - (2 * i + 1)) % 2932
        if cur == 0: cur = 2932
    print('\n')



def my2():
    fibo = [1, 1]
    for _ in range(9998): fibo.append((fibo[-2] + fibo[-1]) % 9099099909999099999)
    print(', '.join(map(str, fibo)))
    print(', 0.\n')



def my3():
    def f(l, r):
        if r - l == 1: return
        m = (l + r) >> 1
        f(m, r)
        for i in range(0, m - l):
            arr[l + i] += arr[m + i] + '.' * i + arr[m + i]

    arr = ['' for _ in range(1024)]
    arr[-1] = '#'
    f(0, 1024)

    logo = [
        '.####..##..##.######..##...##..##.....####...####..###..####.',
        '##..##.###.##...##...####..##.##.....##..##.##..##..##.##..##',
        '##..##.##.###...##..##..##.####.........##..##..##..##.##..##',
        '##..##.##..##...##..######.##.##......##....##..##..##.##..##',
        '.####..##..##...##..##..##.##..##....######..####...##..####.'
    ]
    for i in range(506, 511): arr[i] = arr[i][:449] + logo[i - 506] + arr[i][510:]
    print('\n'.join((''.join(x) for x in arr)))
    print('\n')



def my4():
    n = 400002
    sieve = [0] * n
    for i in range(2, int(n ** 0.5) + 1):
        if not sieve[i]:
            sieve[i * i::i] = [1] * ((n - i * i - 1) // i + 1)

    arr = [''.join(map(str, sieve[i: i + 80])) for i in range(2, len(sieve), 80)]
    arr[3333] = arr[3333][:8] + '9099099909999099999' + arr[3333][27:]

    print('\n'.join(''.join(line) for line in arr))
    print('\n')



def my5():
    arr = []

    nums = ['', 'pierwszy', 'drugi', 'trzeci', 'czwarty', 'piaty', 'szosty', 'siodmy', 'osmy', 'dziewiaty', 'dziesiaty', 'jedenasty', 'dwunasty', 'trzynasty', 'czternasty', 'pietnasty', 'szesnasty', 'siedemnasty', 'osiemnasty', 'dziewietnasty']
    nums_2 = ['', 'dziesiaty', 'dwudziesty', 'trzydziesty', 'czterdziesty', 'piecdziesiaty', 'szescdziesiaty', 'siedemdziesiaty', 'osiemdziesiaty', 'dziewiecdziesiaty', '']
    nums_3 = ['', 'sto', 'dwiescie', 'trzysta']
    nums_4 = ['', 'setny', 'dwusetny', 'trzysetny']

    for i in range(20, 367):
        if i % 100 == 0: nums.append(nums_4[i // 100])
        elif i < 100: nums.append(f'{nums_3[i // 100]} {nums_2[i % 100 // 10]} {nums[i % 10]}'.strip())
        else: nums.append(f'{nums_3[i // 100]} {nums[i % 100]}')

    months = [['stycznia', 31], ['lutego', 28], ['marca', 31], ['kwietnia', 30], ['maja', 31], ['czerwca', 30], ['lipca', 31], ['sierpnia', 31], ['wrzesnia', 30], ['pazdziernika', 31], ['listopada', 30], ['grudnia', 31]]
    years = ['dwutysiecznego'] + ['dwa tysiace ' + x for x in [(x[:-1] if x[-1] == 'y' else x) + 'ego' for x in nums[1: 21]]]

    for y in range(len(years)):
        d = 1
        months[1][1] = 28 if y % 4 else 29
        for ms, md in months:
            for j in range(1, md + 1):
                arr.append(f'{nums[j].capitalize()} {ms} to {nums[d]} dzien roku {years[y]}.')
                d += 1

    arr[2647] = 'Pierwszego kwietnia jest prima aprilis.'
    arr[4900] = 'Pierwszego czerwca jest dzien dziecka.'
    arr.append('Koniec.')

    print('\n'.join(arr))
    print('\n')



def my6():
    def per(n, b, s, h):
        if n == h:
            arr.append(f'T[{i4pow[cnt[0]]}]="{s}"\n')
            if cnt[0] == 20000: write(arr)
            cnt[0] += 1
            cnt[1] = i4pow[cnt[0]] - i4pow[cnt[0] - 1]
            return
        for i in range(n):
            if ~b & (1 << i):
                if fac[n - h - 1] < cnt[1]:
                    cnt[1] -= fac[n - h - 1]
                else:
                    per(n, b | (1 << i), s + chars[i], h + 1)

    def write(arr):
        arr[9999] = 'T[10000000000000000]="9099099909999099999"\n'
        print(''.join(arr))
        exit()

    arr = []
    cnt = [1, 1]
    fac = [1, 1]
    i4pow = [i ** 4 for i in range(20001)]
    chars = [chr(x) for x in range(97, 117)]
    for i in range(2, 21): fac.append(i * fac[-1])
    for i in range(1, 21): per(i, 0, '', 0)



def my7():
    def ito3(n):
        if n == 0: return 0
        ret = ''
        while n >= 3:
            ret += str(n % 3)
            n //= 3
        if n: ret += str(n)
        return ret

    def draw(char, i, j):
        for k in range(5):
            arr[i + k][j: j + len(char[0])] = char[k]

    char_0 = ['.####..', '##..##.', '##..##.', '##..##.', '.####..']
    char_1 = ['###.', '.##.', '.##.', '.##.', '.##.']
    char_2 = ['.####..', '##..##.', '...##..', '.##....', '######.']
    char_9 = ['.####..', '##..##.', '.#####.', '....##.', '.####..']
    char_comma = ['...', '...', '...', '##.', '.#.']
    char_blank = ['...', '...', '...', '...', '...']
    char_dot = ['...', '...', '...', '##.', '##.']
    last = '29qvcqrcho9czgxg7biz7kq7na12rrxmw1qsfuz5tf7qmttcaxo0na1p98ibxhsb4uznifvpncv8730fg5egldzgqmmc5cg28waefmj6hut3v4wayfsvnpq2afaqnhduk44fyxz0ayfetpu9cbpai1h7y0yplk13i52k8svef6dss1nm234tzt9bz74a6r3lu'
    last = '0' + str(int(ito3(int(last, 36))) + 9099099909999099999 * (10 ** 174))

    size = {'0': 7, '1': 4, '2': 7, '9': 7}
    arr = [['.'] * 1000 for _ in range(492)]
    nums = [ito3(2 ** i) for i in range(171)]
    chars = {'0': char_0, '1': char_1, '2': char_2, '9': char_9}
    i, j = 0, 0

    for x in nums:
        s = sum(size[c] for c in x) + 6
        if s + j > 1000:
            i += 6
            j = 0
        for c in x:
            draw(chars[c], i, j)
            j += size[c]
        draw(char_comma, i, j); j += 3
        draw(char_blank, i, j); j += 3

    draw(char_0, i, j); j += 7
    draw(char_dot, i, j); i += 7; j = 0
    for c in last:
        if j + size[c] > 1000:
            i += 6
            j = 0
        draw(chars[c], i, j)
        j += size[c]

    print('\n'.join(''.join(x) for x in arr))
    print('\n')



def my8():
    import zlib

    comp = '¯đäB¹Ģ_CòĵēĶr9ďéĖĝ:»;ÑďÝĢÍåĆ­ĞĖ­S¶þè¶ąĴĦįĒíĤĦßĒıģĆícĆîĩpuĴĴTĮ­tĲ¬t¶ĘİbĮ°ĕ¶ĥĵÂĮ­sĲĴþ¢±ĶNĆöĩģĦvī£Ēê¦ĵĶ¢Ķĝ´čĶĭĪFî¶ıªóĲĪĆvĀĴİGĬfĦÞĒÞbü³ÇĲàĮ:¶QìĆ¬ĕÖĨĪwtÕFvğĞïē­ö¾ĭàÖn§¦ĬLČĎèöæĘ´~ĤäTĤĢ±ĖāĞ<ČNįµÐĆĐĆĴęēĢģħıóëÞnĞĴĖĎïsf¨Ö~ĖĚ°Ć­ëĎįsēĕī±Ė£ºð¯ē¿±ĲrÍĥ¨«Fàî|´ĮÜËgùĵÉòĥĴAĕÈåĵtìĤà§Tē¬uæįsĕnĕĬèĒĖĪjĢâvĒĮīm¶ÖªzİĪlď­ûnİâĖĔĵëĐFĶ9ĄÿĖġÎğõb]¢ĒÍĬĴmĎčë­īµàđ°äĖĤûâĕeĆ¨ĘĕĤçĳèğòĮfē«ĕ¨:įę<âÅÍB>wàĖ¨ºØĢP=ĆEtð8äÕÛFÁĊDcfĊWÆÚÆ`i}ģggºĜPo~SdĦ÷âqãÜAC´ċtZ^WzĆ®įã¤īó ăĪ¤ÓįĄDüqÛqY®Sĥĳu?ĊýĜ=Ny{tlè:Ã¦MñþĳĂñĘëÑV¥ïČģ´×ûøĳïqäiãúĦģOě>Ø ěċĞ¾ěÀÚĨī¡m7Ñēģÿ£ºĪû­ėTòtĕĔÆvTA¥}ØÒĔÅj§ĲĊßĳÎðäÄĊ£nÆRďģ³âÀTþĢMþĪĝ¸«Ø~¼jÝây£Ó;=ĮjËĂĉ§ê·|ODÄĄG­úTþ°RģěİÎþÏhģÊIĈí8ßĄāL§ìTthShĴ©nYCYUho¹_vtÕÖ>CĨĊĂ:ÈAfSxu§÷¾ĔW°ÎI^bÝäĚös±ĩ½đmýÐ:¬nóè^£ē»l©æÁãgÐĲĢQ[āç­ďÒSôC=Ĭ|ÎâÌ@¿ĀÐĕ|UûĊÂąbrtKiâ¾MËćââQb²ĵ?ĩ½Ù¾i[ÇÕĩÏOĭ`TIaì}MæĊT×ßËeÍÓx]ĆěĉĠ»¤îÉđËrÓ·ísÿbĢHlĎZÙÄµĬĤg ]íÕ´phë¤ěċUįĮć³¬y£;ČAe¹Äaqĝ?ĩCēçÂNęåPÄSÒ={ád°ćzØĉáĉaěÎÙE]ĘćËć^Ī÷RÂJ­fġn ĬĎħàģº]ÄÐĕAĢúþ@§ĐÀĈČĊB§7jċĊÅĢ©Ĕ²asÿ­ÆE±ąĝĩXlîÖĚüAcS{ĳĠ­ċěgĜ;mÏěêĠS¸Âtě¸7ģ7W·;čÉgùE~DÿĊXS\ÒÜĘÕ»`Y:è¼ďĠâ`ÇĠ¤=hKaCć9>Ġ_ęÄøSĆQ±ĭQģĐJÂtá?y÷X¬ÝKHÃ×ěHĤIÉs_88ĨÛMõUÉ7¦º`²ÛZ7r¦gġăĆQpçqca°YĊhaUSĥíĔĄĶZSp_ZČc?ç`?ÂOMÈÿ89¹¦ÍXPÁë\wÜíĄ¿¾»g<ÒWzÃĕêØKĨéNA¾pûaÖPªdÉCgfj³očěTĞã|ħ©<D³ĔUę£¹Ës\ĉ¹¡ÖñĘóģĩCBPÎþvħÌ7Á©ý®īZ7[MÔĨélÛÜğ¯¡ĊėîĂÝÛĊTÂãèmUgÄę Xi[uR:îÑ¥RĩöXÙĘlę§įëÎÃĬ¬ÌWO¦Đ½ą·Râ~¯¡HČØġýÈĪĄn©9aºāĄNÎ7IKČÕJēMªĕyĈmwĘßđĤăí:ï¹9ĈãßąD:āę¼¡Á½åsøÄ;ăÒ­fKãďÕ:hQñHEìč^«}­RwÑ©¡T7RçNĠuèt¯¿FēČĄäĆH÷ĝĮTĀĠîjĬXrćÜ×sêÒÛħF{ĥ¥÷Ďįâxđo7yéĤKøªzWĒİĴ¨FSĆú³ĖGĄó¶ZGôH7ĦÐ?ëBýñÔ7óF8Ġģ=î|c½½ėè?ĦáwïÆwSÀ]¨kDħf:gçëûÂ¸=Ý>åA_åĒÞãj¬LīøďăâßE£®~ă¯ĨËñ½OyįM¨ĵ¬ÜUÞĄWďė÷čxSDÀ³ěĪIįÕÁġØíÈmæe=ėĆeYĲÂÍ¡ğìđzà:Ģ[­ĕęÇn£yøôē^ĬĲíċgĴIËÙÑªbÀĄrç´jóMaaORı8mQēĖĮ9ı`ĤÂąÏÑêÁIÂù²É]Ĩ¹süČá¬MĢĞE¯ÎeçĊÌÜ»ÙY9æRÒÀCĮċÒ©±þPÑĳăýğĥ³´ S·ÃF§<RèMĦéÏêp¬DÌĢáĖíg<áIĔZīČëąBÚjġåpBvï\ôÁ;nć§>¿³§G²čåóÛ¢ªj±ăýhĘPY^çï´OÏ«qlÍ}Çâ>RĜêA¤×Ć³}ċ£ęÉģÙaĭI]āĬć:m¯þiÊĨē`àġ»Þº>°ÿ×HÝáéāæml²Òjæ<ôNFù_Ìć:Ġ÷þ}qgþg³\~JďùÑÀaÙMàeSðãiīècª`kàEÃú_}ĦÖØhãNğþ§FįįÒXmnĬ°fnpÙĵCÌ7Æĥgq¶ćó¯¡¬Ġ´ĝ°ÙāRj^\ĚÓiĨSÀ?øßĥzCîÛ|ċÞ£]_ĔyÒÏÈéYÜ9JÜÓÐj`ĮĦĚ¹ÌkBĜďsĕýÃą|j<ùÎÃÉ;Ä@\_É¡á§ÜLË¼KïP\èÅLħqßþĔãyĂ°]è¥yÓíBúYPôzîď¼ġàE]G÷®Ý×cęÄëtß\øGdÖüàÖsþtĠmÖT_IO=ġPË«©áă§ÌvhØDĨMrĤĪÇßiĠ·_ģæĝïªâîæÉKČz×loĨĴüßpåąÆÛęUJčĘ@Uù³Ā;°ĩěÎı¸ÐïÓ`ÚjiÂWýïĚěâĉþïéª¨ġýămöñÀK¢Ë×Ćĳ\csÃáUĞċĊĪ lİ¡ĬËÿzWĬçú×įĴfă_´N;Ê{\ĉ ïõÓ`īĂøûĕPÚsDDęÐxÓpi±h9¸DO=ÇãþxěªRĦ~êEç BĮäë²öb[õ?¢½āqć±ĝd÷^BðăöĥèO:jð:Oh½gĜFS¹;ÿþ¿İĀõkgh9?Ķfê87àėq`oĆé]NċùuKû×ÆàġJyp±X;r=įG­aúPĖ§ÞåAěBÝðB¹¯ñhYVÊRêàĴ8zĪôW?ÿÖ\AÑď¯ĕ¸[»ðò@Ĩ¿èîv³ĜéÏĮËålÒĘXÂYY]üì¨\ïWĕāøpÀd;øSVĘxù©<~ÐfÅñÑZo^ÍKhěûĨIxIEĪĤUZÉðJZİô·Zďl³çisne~čzįĆ·ôě=ÅğÍg«Åïĝ¾Ēıðÿć[IäVē°8ī¼ĨOùýúZyóįd½Oĳ½ÂďeBkĲáwİÉėmùYyI_âĝJ¬cĚMģãĒmDË¡IªÁÆĈÚÈĔÅħėWÈĐÛä½Ð¹Ä\jëGÒg÷³ārQĨa|¶¡L@Ãh¹¤¼kÈ´ËÂÖďW{ĚOx¤ß¨<òęĠ½m±HµÖ9JÍćÚ³¡ÐâÍBL:RhÛjKĪėýĐLÍaÎĊ^ď±æhÙĠ`=ĦV»xÄk:>JàPĉûĝPé^yÝoöÑ±ħ~¡ÍðÞģÆû;ā¶¿`¿JâsÊĎÈRÚĉ üĳ;]ÈMNéĄċÞ»ÐÐ¡mĝĪâRčī±ÔólĒ¥ÜİēĆġïãYĊù_Lxõ¯LÂ^;ămñéçĊ¥YxdÈÇÀBÚÒýçPù¿8aÄÝĀĕK¼M`āąĩúTí¿gçhĘ¶êÛ£Òġ»CÐÞ»ãdºĢHújÍæĦ Đ¯ü?X ûÑloö³Ó^XË>ÐÐð}ĆQªã¨bMì¨ġÝ?ĔæĆ¨aßĳ²Y7¿üĢrĎxéçĥ©qÜĢīÈöĠ¯ĕĠïùĒûāÕĵ¦ČÍóÄYIn²øģÚOW©ÿě[òfê>¤\ÂtIÓE£jbªÿĩÓd°Ķ­Ìĵ¿ø÷ČÿÔmÎãÿİÖčéµĎĐqá\SıE^§RÙ>c»TĜÚ¾ÿÈraĠiZPąÛNS´èĶĭwcaJV·ËĵĊĒ®ĂÎğ¹ēYBĳ¿µ­¹¡ġVKĵĆ=ì¤ÅfISHB[[ÔçĶ\ċgÂĆÍčré©ćĥ`ĆsJ]à£²Hà\¦Ym²çąďh~}\ĬÄīĠH`ĜģhÄ@RİãÜfhįĴïTñ9à[ĚÅðôĆMs®âôě`AÁ¤ą¨ÁÑĊËtYÛC]ďÍ[ęÓÜĂëPÌĬ¶ĞËğ¶<¹ ÐéCsòhøª­Pc½í_ï\]Õ{¥KË«Ä[Ī9ÒêăĖSíjì¼ďSöóĀÁhPĩąûďïï{äÒúÌġÍ»yÙāġÝØéĊSMĤÈē<Ó©ĆĔĳ·À©yıĔĴi²ÚćiÛÓÂÅÔû:nèĄå°ġÎìûĭÐqÝĬiµMþyĵlxDĭăïé¶á±ÏXĲTgčėċąCÐðÆpÚãXiÆHıĚ8ĞæĮPNąàÓðĉÖT]ıZ©ÓðéÖ^÷ĖPÏĄTĪTé¶«ĖĀ¶µĂĩď'
    comp = [int(c) - 48 for c in zlib.decompress(bytes([ord(x) - 55 for x in comp]))]

    _dir = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    arr = [['.'] * 1000 for _ in range(1000)]
    y, x = 500, 500
    arr[y][x] = '#'

    for d in comp:
        y += _dir[d][0]
        x += _dir[d][1]
        arr[y][x] = '#'

    print('\n'.join(''.join(line) for line in arr))
    print('\n')



def my9():
    txt = '8ͣº:9ɗǲ7Dȟg7Fʳ΢8L¥n:Mȱ̳8OÉ΄8Rƻ¬7SȒc:]şć8^Ϳʛ8aƁ8aǏÐ8eĹx8f͍Ġ7iΟɈ:mǅu8n˶Ğ7rĠġ:uæ8v΍ǵ7wˈš:xǣ̦8yĭŎ8{ʴ@9|ͯŦ8}iͷ9ˌĹ:Ώ̊8}Η7³ȱ8ǃb8ʛͩ8ʺĸ9ƪ9Ȳ<7Ͷø:̗³8¡āc8¡ʅǔ9£Ͳç9¤˕8§˙ˉ8°ιǚ8³˝ԍ7·ǽ>7¸ț˻8¹Ȕ×:º˺9¾˟º7¿̕ľ8ÄΟ¬7ÆÎÏ:Æơý7Ìͧȭ8ÍʣĂ9Ñϋ9ÔǤȵ7Õýǣ8ÚſĿ8ÛĆU:ÞʚŮ7äЉP9æЉƋ7è˯ť8êϳ̮8ë±͎8íƒņ7óƭĂ7öƬ;:ùƾĐ:úOɝ8þʇŨ:Āȍȋ9ā7ƅ9Ą̶À7Ćɫ̳8ćģȞ8ċ˛U9Ďζ:đ̓ǡ8ęno:Ěťģ7ĜƓŝ8ĝɣǶ9ĤǓǔ:ĥÛ7ĩĥñ9Ĭ7e9ĴŦŧ:ķ̫ź8ĸ̋Ȭ7ĺΌı:ĻĎʬ9ĻϻŪ:ļƛʑ7Ŀ̯p8ŃΡ_7ōƐ¤7őɱȹ8Œǽʪ8ŒɠƑ7œСŞ:ŗ7Ǐ9Řǈǖ9ŚΈʀ:ŞСĬ:Šî§:Š÷ò8ŠСÚ:š˕Ȼ7ŤƉË9ťŉɱ8Ũśɯ9ũů¶9ũɻÍ9ũ͢¯:ŪȀ8ůŽƸ8űü:7ŷ̚¿:Ÿƃɤ8Ż̂ɞ:Żήǿ7żǹʥ8ż˜ę:Ɛ͡ɪ8Ɨ;¸9ƞʁN8ơϦͦ7ƨȬÚ7ƨ;ȁ:Ưű­8ƴ̻î:Ʒ˹7ƸQè8ƽϤǺ:ǃ̋Ŏ9ǄɳŤ9Ǉ̡ó8ǍʯĘ8ǔɲƌ:ǖ:ǘĐ:ǛϽĩ7ǜȰƃ:Ǟʓǭ8ǡʺź:Ǣ͗Ă8Ǥćǽ9ǩϧg8ǫœŤ7ǭƷŀ:ǲŹ:Ǽťî9ǿǷþ9ȉ˥Ǔ7ȋ˚n7ȍϵp8Ȑ́7ȑļ¶7ȑΚ¿9ȗ̆:ȝiǬ7Ȣ®©:ȭȗp:ȷК:ȸȕC7ȼǾ¶9ȼСh:Ƚɑȉ8ȾÝƧ8ɂ7£9ɃɩŚ9Ʉ͵ƺ7ɅΥʂ7ɈȺÆ9ɕʅ:ɗƯĜ8ɟȑǄ8ɢGâ9ɦСÏ:ɨ|Ŕ7ɫėÅ9ɫǳď9ɰΨŠ:ɵϻX8ɷōȀ7ɸȹT7ɸʡƪ8ɺΑÈ9ɿʕî8ʂΓY8ʇʖǧ7ʕī˃7ʝ79ʢǵĿ7ʣͷĺ8ʤǑĞ7ʥȡO9ʧ΋Î9ʪƓ×9˂Вɍ7˃С¤:˅Łň8˅ȚJ9ˈȭÿ9˞7æ9˟7U7ˠ79ˣȟr7˪Ɣ9˯ǀ::˯̳û8˱ǉD8˱ɂº7˽ʙ^8˾ư:̄ĕƩ7̅ʋđ:̏7ì9̗ʖĞ9̝ŝÀ9̡]Ż7̥ɗÕ9̦ɟ¿8̨ǳʺ7̪ëz8̻ƚ¼:̻ЀĖ:͂7«9ͅЋN9͆͐n9͑Еb8͠7æ9ͣn9ͷ̾Ê7͸ιÃ8͹ă>7ͻž~9ΏƟȉ7ΐɂG7ΑŞâ7αɈ:δ9εk9μɭJ9ό˧õ7ώ˙N:ϐϝƨ7ϕȆr:ϞƪŎ7ϡʨr9ϥåq9ϮǊ@9ϴɃJ8ϷʐĬ7ϾξB:Зü̢7Йɾȉ7'
    lines = [[ord(x) - 55 for x in txt[i: i + 4]] for i in range(0, 1040, 4)]
    arr = [['.'] * 1003 for _ in range(1003)]

    for y, x, l, d in lines:
        for _ in range(l):
            arr[y][x] = '#'
            if d == 0:
                x += 1
                if x == 1003: y, x = y + 1, 0
            elif d == 1: y += 1
            elif d == 2: x += 1; y += 1
            else: x -= 1; y += 1

    print('\n'.join(''.join(line) for line in arr))
    print('\n')



def my10():
    def make(n):
        return [line[i: i + n] for i in range(0, n * n, n)]

    def mul(A, B):
        N = len(A)
        ret = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    ret[i][j] += A[i][k] * B[k][j]
                ret[i][j] %= 2
        return ret

    def mat_pow(A, n):
        if n == 1: return A
        if ~n & 1:
            B = mat_pow(A, n >> 1)
            return mul(B, B)
        else: return mul(mat_pow(A, n - 1), A)

    a = [[], [0], [0, 1]]
    for _ in range(17): a.append(a[-1] + a[-2])

    print('a_i = a_{i-1} . a_{i-2}\n\n')
    for i in range(1, 16):
        t = f'a_{i} = '
        l = [a[i][j: j + 40] for j in range(0, len(a[i]), 40)]
        for j in range(len(l)):
            print(t if j == 0 else ' ' * len(t))
            print(' '.join(map(str, l[j])) + (' ' if len(l[j]) == 40 else '') + '\n')
        print('\n')

    print('\n(A_i)^n = B_i (mod 2)\n\n')
    line = a[-1]
    n = 9099099909999099999

    for i in range(1, 71):
        ta, tb = f'A_{i} = ', f'   B_{i} = '
        A = make(i)
        B = mat_pow(A, n)
        for j in range(i):
            print(ta if j == i >> 1 else ' ' * len(ta))
            print(' '.join(map(str, A[j])))
            print(tb if j == i >> 1 else ' ' * len(tb))
            print(' '.join(map(str, B[j])))
            print('\n')
        print('\n')



if __name__ == '__main__':
    [my0, my1, my2, my3, my4, my5, my6, my7, my8, my9, my10][int(input())]()
