import math, zlib, base64, sys
from bisect import *
print = sys.stdout.write

fibo, lg = [0, 1], [-1]
for i in range(91): fibo.append(fibo[-2] + fibo[-1])
for i in range(1, len(fibo)): lg.append(math.log2(fibo[i]))
pf = eval(zlib.decompress(base64.a85decode('Gar>E8[@/+#eUMVCpFU]&naetrms[c,X;<qEd<gZBY#/^r;-)USo`IOl=0XUE7>!Y25056hKL4,]!$MTiXjgjVb$hYo6`H:5#Fjp!4Ij4Y8kK-X5Mq`X;n$`dL,5$.C$AB0"6)gh[#<QFr?)YA+5%;2K,Z>{B7CWC#c#"p/bapo2X9E+aidK+h0E6>mnn;%YbF/FhT>d`.AM&aJ,3M?Yn]RV$"pO{"&6PAj^Dn-q,d5.C^/V1XJRS7$CF9!";Nj<t2(Cg=SWi+JPm+3`I#EK!)V8!LIkiUb)U?P%*N?H3R0R&b8kPNsJ/bo=/DRMWcRZGACr=i&(E=7@Q?)n8YKki_^2&OV75QV-<)@d:T}L-&X`s:mqKqL71:QN0!73gr?>P&0=)E]%Y/)e7c,`=@80}#*8#d1VP`[QI0^^c!rgm0$lK}}<"+e:cj_.@c!E$:pA91o^ur=<4:M#Uk]:m:M>R1iV[lOd580X^;c}{<N#naTq{?]C``4n(@8pY(J`<Y;7oB:8,UqU;i(BT09<m(@:NEY9u,/c4lk7jeXE=8eKq-?Pd&<>+TD`HmL%#jGWhU6Ha7JZ+OkAG)i(Uumf4YlqWZ4@p07t3#o_,;=<3NbgK"X}oGU)uS7"Vb=>]@^;RZa$*Zs3p5c!;T#5H"tRSM"$qUM^`4/OX?A@%A/3Km=.9`Oih;nljeFd]`J"$s+M-"U*lU3L95E#d,XD.Odb0a%i]*/B`ZajVQt1Zt>9Jb>HEZk+Co8,4Q/3N-;X{,97}I8/{hHd>PkWFYoe>BW:T*Y#4dc-f*mb+6mBHSdn?K4mJJ[*7EWj4H5h'.replace('{',"'").replace('}','\\'))))

for s in [*open(0)]:
    lo, hi = map(eval, s.split())
    if lo >= hi: break
    l, r = bisect_left(fibo, lo), bisect(fibo, hi)
    print(f'Range {lo} to {hi}:\n')
    if l < r:
        for i in range(l, r):
            print(f'Fib({i}) = {fibo[i]}, {fibo[i] and f"lg is {lg[i]:.6f}" or "lg does not exist"}\n')
            print(f'{pf[i] and f"Prime factors: {pf[i]}" or "No prime factors"}\n')
    else: print('No Fibonacci numbers in the range\n')
    print('\n')
