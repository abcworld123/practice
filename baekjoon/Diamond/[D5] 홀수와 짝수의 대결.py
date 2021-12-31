t = "99_!osӅԥOᄟᄵᄹ©ᇓᇙᇭᇯᇱሑሕምሱሹ%ቍ቏ቑቓቕ቗!ብቫ!ኋ痏痓痕痗痛痟痯癯癵皁%皓⾃ꚗ'ꚫ9ꛑꛓO꜓ꜛ꜡ćꠕꠥꠧꡟ꣓꤁ꤋꤍ꺻꺽!껍껏%껫꽣꽭=꾗뀩뀫˃닝닱닳닷댕댝댡#댵댹댻덋ㅙ+­1񁢕񏽯a񏿳񏿵񏿷1񐀕񐀗񐀱񐀵񐀷񐀹∓񒋝񒋟񒋩񒋫񒋭񒌃񒌏񒍅񒍍M񒎇/񒎥O񒏡񒏥񒏧񒏩񒏵񒏷#񒑙񒑛񒑟񒑡񒑣񒑭񒒣񒒥񒒧񒒯%񒝅񒝉񒝕-񒝯'񒞃񒞋񒞏񒞑񒞟񒞣;񒟋񒟕"
arr = [[1, 1]] + [[ord(t[i]) + 906150200, ord(t[i + 1]) - 20] for i in range(0, len(t), 2)]

for n in map(int, [*open(0)][1:]):
    print('OE'[any([0 <= n - x[0] < x[1] for x in arr])])



# 계산 과정
# from tqdm import tqdm
#
# def prime(n):
#     if n < 2: return []
#     n += 1
#     save = [1] * (n // 2)
#     for i in tqdm(range(3, int(n ** 0.5) + 1, 2)):
#         if save[i // 2]: k = i * i; save[k // 2::i] = [0] * ((n - k - 1) // (2 * i) + 1)
#     return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]
#
# n = 1000000000
# primes = prime(n)
# print('primes ok')
# arr = [0] * (n + 1)
# here_is_O = []
#
# for p in tqdm(primes):
#     pw = p
#     while pw <= n:
#         # print('-' * 10, pw)
#         # if pw % 1000000 == 0: print(pw)
#         x = pw
#         while x <= n:
#             arr[x] += 1
#             x += pw
#         pw *= p
# print('calc ok')
# del primes
# hol = 0
# jjak = 0
#
# for i in tqdm(range(2, 900000001)):
#     # if arr[i] <= 0: here_is_O.append(i); print(i)
#     if arr[i] & 1: hol += 1
#     else: jjak += 1
#     # arr[i] = 0 if jjak > hol else 1
#     if jjak >= hol: print(i, end=' ', flush=True); here_is_O.append(i)
#
# hol9djr, jjak9djr = hol, jjak
#
# # 906,316,571
# for i in tqdm(range(900000001, n + 1)):
#     # if arr[i] <= 0: here_is_O.append(i); print(i)
#     if arr[i] & 1: hol += 1
#     else: jjak += 1
#     # arr[i] = 0 if jjak > hol else 1
#     if jjak >= hol: print(i, end=' ', flush=True); here_is_O.append(i)
#
# print('str ok')
# print('hol, jjak:', hol9djr, jjak9djr)
#
# # 여기
# print(len(here_is_O))
# # exit()
#
# with open('here.txt', 'w') as f:
#     f.write(' '.join(map(str, here_is_O)))
#
# print('write ok')
