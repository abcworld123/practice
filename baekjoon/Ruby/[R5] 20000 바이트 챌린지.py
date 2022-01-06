import base64, re, sys
from itertools import permutations
print = sys.stdout.write


def atoi(s):
    base118 = [0, *range(7), *([6] * 7), *range(7, 32), *range(31, 84), *range(83, 118)]
    ret = 0
    for x in s: ret = ret * 118 + base118[ord(x)]
    return ret


def f0():
    return 'BOJ 20000'


def f1():
    s1 = '#include <cstdio>\nint main(){\n    int N;\n    scanf("%d",&N);\n   '
    s2 = ' if(N==%d){\n        puts("%d");\n    }\n    else'
    s3 = '{\n        puts("Still working on it...");\n    }\n    return 0;\n}'
    arr = [s1]

    for i in range(1, 20001):
        arr.append(s2 % (i, i * 4))
    arr.append(s3)

    return ''.join(arr)


def f2():
    s = ['B'] * (1 << 20)
    ch = 'BaekjoonOnlineJudge!'
    for i in range(1, 20):
        for j in range(0, 1 << 20, 1 << i):
            s[j] = ch[i]
    return ''.join(s[1:])


def f3():
    def init(s, e, h):
        ch = False
        if e - s == 1:
            if leaf[s]: tree[height[h]][s] = '/'; ch = True
            if leaf[e]: tree[height[h]][e] = '\\'; ch = True
        else:
            m = (s + e) >> 1
            if init(s, m, h + 1): write(m, ((s + m) >> 1), -1, height[h], '/'); ch = True
            if init(m + 1, e, h + 1): write(m + 1, ((m + e) >> 1) + 1, 1, height[h], '\\'); ch = True
        return ch

    def write(s, e, step, h, c):
        for i in range(s, e, step):
            tree[h][i] = c
            h += 1

    x = '^-io,ACW.G6#ro}j@-DJ/r30hJ?EF{ZqJ8rM+xRmTQHl}v^7l4BPn,.j/[i<Z2`qLFH%^c q[<lD63C^-/hEl{"N/!FC"u*:?~&V`=2W)>:PV&GgBh/cKBr4 <S<(_JQ+;nCAwKd~ML|DE#xDpq*`iwPzN/@?U0S/F$xVIKuS{${m2o0S}pgKW@3,w>uh:e$<i9% I@z!;(e@wX^ ]#4R&P-Mx!g&bRta$Ss|`{u=?'

    leaf = list(map(int, list('00' + bin(atoi(x))[2:])))
    tree = [[' '] * (1026 + i) for i in range(1024)] + ['']
    height = [0, 0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022, 1023]
    init(1, 2048, 1)
    return '\n'.join(''.join(line[1:]) for line in tree)


def f4():
    def init(l, r):
        if r - l == 1: return
        m = (l + r) >> 1
        init(l, m)
        init(m, r)
        for i, j in enumerate(range(m, r)):
            arr[j] += arr[r - i - 1][:r - m - i - 1][::-1] + arr[l + i]

    arr = [*'..#'] + ['.#'[all((x % y for y in range(2, x)))] for x in range(3, 1024)]
    init(0, 1024)

    return '\n'.join(arr[:1000])


def f5():
    txt = 'F:_5gDZE[ 5_ !uO}:(qjiu9JXu^#G)k;~rl.~_yM:MG&>iG-vei1GI*V5<J1;]?fB|gh-ek?Jn}8cKqJRz~c50F4@"uyzp2(&Z<5!k%my>R3./w{iO.S^5WtO",/o{(*zkMCx+6_v+mt;N((TNG:GrSm%C1@xkR#YKY}NDY$t+S88JOqGw=t_b,~H+`s5?4=yxE)rTHhv(<K G}><bq+&b 3h"pxY8tUR!314Sd!|iO+<SXV7,E>/dM72B7.U`V+cyo]F@0JL($#dNtv18:[^sHli_*Bkl-*5pND90(+`k5,m$iACAha|Fu_g;]W(}`QA>+u7[4WNBt]M]OAmLb(a0@:8:F2/FL-7KQAd#,J7gxpRn[tV?kot/Xc{`W1"|ZsTyhLaMuD20Hprj=w]~_RNoFY,Qmo>KP9X,>|]4)|ir)>P"hJMbkVfavkuec-@[5;jIV(WAj.dDHdfIX{!Wx>1%UchkT^l{S^|n9~z6u6m%MAH`EpDq#_H~wJR  m|Ht6aUo-D65?_v3eNCmJE3{{csS+df}bMR0jbJe;6"mY3.u|/0U{g59jI R?"xzqNpp@k_n"FQ*rj#I ^Y^r4}D/H*1HDO2t]*/cP$3q{hsu[63nd&VUfpP)[ON]:tlD)mIZ:<r*Fe,ar&ImQD>SNUxGSvDjot$B~zEQR6LNdK|5g@JSArA$huhb>m`XuCj-+PV+M]az,<h8)MZ~3lGMQaZRC~Ms1JP(O(+03wuF.6W7tMNgJofC>nf/<z:"vN(-AE-Oytdqi2CC5%+`U_W[&Nz*hIpdk-f&Ws]jSp}h5~Y)(a5vfQT==t7b(J`!"|9i+Gh!0hk0=t= e;i/ld),y%R8=Dy6;?(Qy2;W<`e0ny_-uCXLHQvG_D#b6c=rN<]YcHiqE|Sahgk e5kkb?a:.Gx/UR&O<D9T!mc74dw6OO}o:6i5ljjJlZl,M[`,I*C"r!pjs0,;P7c_lw?&^_j&Q!M=K7<L-v[m@s)4Fc7k8hqF2ZMEQ[WN,gTaEF+m!e;`woTt 4/z0dQsW!VRR|gim>:=!"_`fw}K4V}t0003;hM$QH_+K&tL!jWM q HL^k$[,Hn,z_`VwzxsKq{.lh[fd+XZD*}RYF#Q|$FovU^1[V3h@F~|*,}HxNL5YG[D+fax=Y"%#)-.MV=>HIJ#h1k.#{X<BR-J}E#wKk{WAdX~%@za/jc8k>xbne*>(DiPGnrh|}kSKy~aNEU;eOC]Rnh2<kJk#2|Bqk E;/rz{7.|9uKHq{t#9K:[)ncZNBMy~a>lJ+t6po*eu7a1wY_(_UpsECP1Lg^nw_*~Xo]tt&%-q9c:mT4Mo"mm9V(A?{!7(aNP2UUe-3L%Io2Z);lwQ4Q[cXf|S+9zm6X-K!2XhgD,9^V,)zhdutdXIru-q_{J<;8Mwm;F]C!r$XZrc5i{rD`.OeH1F$FW1Jko=wb@5 -u"F7^) Q[kM=y)Sz4Z2I<z>R=B&*Cs!3.ZX&4g$nm?(b,2$9S,mYqbkVpxFTWd>kU$Y}Mn]ml*!Fp,=NT9h+$Y%C{y`";5__=?$po1 16UL0@X3 &32AWU&)ln?J<"ZI[n|}@@Eg:9y@bnwSz!X_jFp4vd6}B..Cb}g{79VEx KGMcya"M Vcbf5*H.&`pQw4^Y}vGFe- r8o~=`K1qUl.+"f"GngPj*b*A|A2`7CdhS:=H}3AC+a@q?, ;?rR2?;?.v_Pe.pD (JR~A!S@&oSU:#GjicPOgsS[.PE|+ll.p&y6oX2O4y)Tf/~9@`{w%2Qa2/! QzZA_9_2i1MPKv0d:]P[pRXfv!@;1h8YYjlSWbD$l*[GU4_[xV84=*U 6cQRxt.hnXY|=4DPIIZ3eE3PRz(0eJ!n?!nVD)%;XV>UGc>QSQ(G>`b-on6mu)+)!|(%b.cn0pfIBAd1A2}6kv4H#T]v$IF.b,mq{@IzJH{~"s)W3w^Q-z<aGeqg6y%7@ANz{S>g@i.d0uZH,~Z~D)sJtvxFPn<a[g_Zy)v+/Wcl{vHs<>n>-wgm)H<(9q9EqQP` :`n>1M9Ln@,)kpdXI?,LM13I>.(:sp>V,}S`~xSwRZv+;0}I8$4}h:*%j,>>5.9C}<Iqt`u{b[1BqRRS>NQV3./x!y]=xZKhRqgh?&3D6%CS Jw<0K!TNXz3NBUFjIdWWX8]AN~L|fjNg6n~wx,UZQ#/S`eyMw3dZ(KmLA?bo$DX>#IZhL}@_&F>o6 ,X"q@p!ED?S$Ygxr1g5.q_GopKBsweO 0}oe7~SlhN]cP1ui5etk4vezlCQsee1EQW$8*~au!c`c>Crq42itS<Ug&F[>ip]Cnpx3NOFIo %![cyVYCu_6USDW,18aN6K)UtFvTLa{SK}6hasi(:mVsY]d0w"|Suq|Z:?:;KtsE>}m#?=7P 9Y?-{"U.bJwAsK`"(9XfS{M=_]".X3U@`HnasG<5!>dqph}Z Em7x]T)>*CxZ.3ncI?JnW],FHzVP&wgxrsDs0`%nVyJ3W]LKyjIEM|dz.nR"YQM57nu(MEp~7NEhR1IaWJ<L]^7&seG9x];bJ8-xFw!.8[[-S0r>&Kj/>YdL(&ucA1Nm$qQ>FG}@W!+GC_Jr)jX(".peQQ1Yx3:?k}24L6-On{Kwq-f/D;l*zl0&I>umiSykPz%./t5&& xv^Lqk?XxwSREz%e@^N)!)3{woTOA^>t%Zo?y cy&8VHGmjoYq>hjE[l1zk^Bc"w<xM]mi#kxQ{-/gIg]*y0IAU:,{nb|c/kP]u(#l?R*3R.d2j5NPxkMv.K@ERMu5AQI)4Y2rI;sy2<//(N3vfxYzQGR?uWA^koIPKff3i5`d?cn9$-?G8Yjoq3x0tw>_tKvKQCp4$lJX[$`ZP)RXOy+{"3Z<bys:ZQ:cOQ2sA[hPw<jpv_{X0kAIsF#3~Q.dldHuR`u2IDl5{zS~nVI]cac Z@/# XOkvb*}"<BBn_QVm`k1xetJ!LQc"e,56^yn_TQk;K]$|%oE}|.#CJrM9obs5<:LIP82Q^x;K3rj2/aS4*rbp(j#!=oa"Pi@|U}UHSK6/2s!"MF&WbWbgDZu2@f>J[wkP7TS!1-g3OHknQ>.%5jIWD/;9jq!4H/bBo.ymt`30q~ZqB;W5Fq6pzc @vosw2!gZSwTCCtB K|Je]G#i(/R=n ty`(Iy}N1hf/qU>@i;%;N}+Y[dC-$Z /]&sj=[E)WuCy{51p&0RG%#e{?M_2<<uvNSag;.}FJkBP8c*&v.c0B]37?^y:y:8_ Gq3 H<LT21Y&b]~aN7Z6;D=R]*j~d;tOw KA^4j)[`.zn]:S3M|_hvt#St^V@~5j3<Aooysd,I{4x{yl{5<SkeO-j3AC?Ov1g?PBf?[DDR}1]BFj_#o@IPF6mi]d4]3fJj+,&DTsQ>jv>5XB*Q8ns//Y._Uq^(e,07dQc[SH3+Q"T"T)-2bZpwti~$Y.d&N}XU|}JfI>9Bh#'
    txt = '000' + bin(atoi(txt))[2:]
    txt = base64.b64encode(bytes(int(txt[i: i + 8], 2) for i in range(0, len(txt), 8))).decode()

    return txt * 200


def f6():
    p = []
    for i in range(4, 10): p += [''.join(map(str, x)) for x in permutations(range(1, 10), i)]
    ban = [re.compile('^[^%s]*%s' % (sum(map(int, x)) // 2, x)) for x in map(str, [13, 31, 17, 71, 19, 91, 28, 82, 37, 73, 39, 93, 46, 64, 79, 97])]
    return ' '.join([x for x in p if not any([b.search(x) for b in ban])])


def f7():
    def f(x1, y1, x2, y2, h, patt):
        xm = (x1 + x2) >> 1
        ym = (y1 + y2) >> 1

        for i in range(4, h - 3):
            arr[y1 + i][xm] = '.'
            arr[ym][x1 + i] = '.'

        s1, s2, s3, s4 = (next(patt) == '1' for _ in range(4))
        for i in range(5):
            if s1: arr[y1 + 4][xm + i] = '.'
            else: arr[ym - i][x2 - 4] = '.'
            if s2: arr[ym + i][x2 - 4] = '.'
            else: arr[y2 - 4][xm + i] = '.'
            if s3: arr[y2 - 4][xm - i] = '.'
            else: arr[ym + i][x1 + 4] = '.'
            if s4: arr[ym - i][x1 + 4] = '.'
            else: arr[y1 + 4][xm - i] = '.'

        if h == 16: return
        f(x1, y1, xm, ym, h >> 1, patt)
        f(xm, y1, x2, ym, h >> 1, patt)
        f(x1, ym, xm, y2, h >> 1, patt)
        f(xm, ym, x2, y2, h >> 1, patt)

    txt = 'GHYR2pLDuVR>n&l"B]v-Tl^yFo2d(I4C0%]cVmnJY+ LebvBR0^(mk^C9]77V:ZKn|ogsTT22=*!neNMs"FydfZwg}LgcXkO[wRq?,_]a7ww3")`]$;9b/a_aF;awVKhuxaNO}PGl1!3O~k3!),#.MRH5DHpX@Sw)g*f:L!J#+"D.=S092.t>NFm}`"cnZ8wR xq!g?LDFjEg/h2qsQ1Y$t{R71-yFAKO_wOw*~cMUH))"MGG.9?`Y`tk{{f%{a[oUO#STcPtS8h(re{msMX_p$BSbnzU~!!swv[mN;drbr3i]euV "fhQB(D`15SE96%RSM/r&p~|Gf42R:vU,X)lI6jS/z0N5zBa^wN/_R2Gh^vA,7zTdfODnDY&n9Z+QqaTLc}HnH&j1<}z3|B`P8ws!^I)!Pntq>z+(_TQQ/1gWnB?Jn=2RBDEb.KWbDL9ctuC5%+_RvXnk/e7<MK+?K$?nKH<+x0@4HtNpYuta6<r{EB#H*=V"XMk:(Dhc4[H)FkAy uq|LO;+a:u9Mbq-7yW:iT*1WWR,51x`}P[l#nbh.yUChA&#Z$sT*=U,h%7"S+9;~^ZZXOWU8<r^e"{-yBg|zlbY|z/<8|SC!B>&HY/yq<14J@Qk|XkF"9d9"|Lh?4Qgy)pty!uxRp6:FiF&DkI.R#.6j/9Q/<E`P3wDXP"WB}}W_J2/9sP_9G6X$1jVEt,"Z:#G_(V`_9a?MDz:XiSj}O)HbWRT|_aEY|w@J/]m/>!R>J{X@5HD iwm?SAoKE2j6Ed,t<P#U^Zjlu9_}(7%Q0x[8C$p,)%E4xTXfGp~pgNYe[HW;/L1(I+Yy3|g!w"$(_p%]~KcIYm*k]8f5}{B`11j~MKz}1B;9xxUZx"3:IIkH6P/$BYp8,SF{.fltEF(z9a9dOUw,Qu6K0|CH27dr-p@M{p.XOm9EN==^G?6S23P2%_G"JVY}bJ}u"pT%{:a-s:,eSQdNiKDMYhzl``/sYM#@O|BZ]`V6xt>8q6$+Pg7/{QgYr8FuPJQeL>$bWy:yL/Qb7FRnXohahb,C0OZB=l4E/dyW?uizWHUD!|P^|X]CUus3B,.OwaDPwy#Y,cL5saG(nb,2#N4S:Ykf&S(AU-L&#^:$we (e? ~|K#7=S{delag($gQ6$6"S_vHT8MXae20(PZY= SCls&KnE.s,f}c2vn9Jla|b_?$MayhPe<9qbn4hgL+j""rO]"h__=jdj0X#uE^t6@$KA1);}MqyOSjY#B2Q)Xhq9WuRmOP2vX}w/E=CmkZ?]L1sal]k"qO2*kx#id)*|NIH(|Yk(8VQh{g!"XnXKM-/bz7}}u,oY"!dj?hy! A+B)*:w5fQ[q6@^R,om_C>W8?afhyc<D0@._93;FUkEO_CGgG^Dg^RT=tFh>L!*/}N^a!A;!70P/5b35/NB!eU:RM)7"j2J|W3tR6=(">ECHF_q:Yco$zW.*gwH]3f( wVpt9>*:f0Fc6^;*@?6m}.;a%HELP,kRDqHHb*No?T=cF(dy`u&LFIe0mO=5l*j$rU#*87ZJ_(WWnzRe1eP}/&}Yc7*U}hIz:B*3g<dqYB)G"U//Z}0Znlad#_h+z,G5SC^k^ E|%5~-=]xXoG0R/,1X.Rsp3e8}@y@/xtj-V}BDgphSkL0+edo"m-7;rzy?cH!p~xW{HH?U8(02V6rD[a/h.2c2E6yo4GF5kYgkAJjW_fc$?02h"c>~Yf50?hYBk/V*m1>H5dhxP2E:OSR59VCMn[h)KlwxUtS]4.bRC@U 1C"xHLQ.E`VKGF[?sS""T]^}0j^2q]7g#!K`/1y6ucIx{SvG~s4 WI`Y"SD7.H#h@|:Ye4rHj8Kk=)J$iF#(pX.0#YG.7e~67A0f2PZR`>w;JilUEs/Mi(^jYe::Yo0v5PwN;Q+,rxW_",8)gKql1!&,*%s]]&`[p8!^T(YV9z=e_%M84dXbBN}Zi/ZcW@S#znC&DXFH"t0Y4!nzKnkv Z]<k1;iP5D^. %X-X~xO};LV,NIM(E`/o}"6 >MopA<3We4{x=|8IyUVMs+">FE._Klh.xm#-_8:z|oyKJn?GgWyw[t5~wi*0(k"5_95f6/=4HDVIv=!<HE^@Mzhg8N;?,.T2`@[ U=vA>I ydaz)baO"f)(.(M`r,$f1DLY8POV[&z^}+CqL.{n7X6_I}00PL}Xd +@RfN/ZKUqrkLvLYIW`8sO -YH+MotP{TR_m>5n]j.?ilzI7(@Yq082MIa-HCr^gkFORZLo>%!;ZoD]%jC&C8Xx[#f9`q:n@jk$u8NkU>5<LpN:mYGmv|y.B]olv=;tsCf?6XeB$xyR_Yd}FvW@(BWS 5*]d75]"9o{!$$skek(66Dt}?6;@oe2EPbpKCe7}Gb9pqw,Xf~:[{6IBW8?n*K@8Zn?Syaz;G|RCY?wr D2ruj1kS!lD[~h)8S, .@nyTzp%N[`k`NdlBm@&z#)z264]9+W}vi|b-0 K6<Kk goI!N|fFwQU("'
    txt = '0' + bin(atoi(txt))[2:]
    patt = iter(txt)

    arr = [['#'] * 1024 for _ in range(1024)]
    f(0, 0, 1024, 1024, 1024, patt)

    brr = [l[:] for l in arr]
    d = [[0, 0], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    for i in range(3, 1022):
        for j in range(3, 1022):
            if all(brr[i + y][j + x] == '#' for y, x in d):
                arr[i][j] = '.'

    return '\n'.join(''.join(x[3: -2]) for x in arr[3: -2])


def f8():
    n = 3 ** 7
    s = '1'

    while n > 1:
        t = [x * 3 for x in s]
        s = t + [x + '0' * len(x) + x for x in s] + t
        n //= 3

    s = ''.join(s)
    b = bytes(int(s[i: i + 8], 2) for i in range(0, len(s), 8))
    txt = base64.b64encode(b).decode()
    return txt[:-3]


def f9():
    return ','.join(map(str, [(376739550 * x ** 4 + 28540875 * x ** 3 + 565524465 * x ** 2 + 855292706 * x + 20000) % 1695327975 for x in range(100000)]))


if __name__ == '__main__':
    print([f0, f1, f2, f3, f4, f5, f6, f7, f8, f9][int(input())]())
    print('\n')
