def easy(n):
	# n = n
	n |= n << 1
	n |= n << 2
	n |= n << 4
	n |= n << 8
	n |= n << 16
	n |= n << 32
	n &= 18446744073709551615  # only python
	return n


def push(n):
	for i in range(62):
		x = n
		x &= 1
		n >>= x
	return n


def bitcount(n):
	n = (n >> 1 & 0x5555555555555555) + (n & 0x5555555555555555)
	n = (n >> 2 & 0x3333333333333333) + (n & 0x3333333333333333)
	n = (n >> 4 & 0x0f0f0f0f0f0f0f0f) + (n & 0x0f0f0f0f0f0f0f0f)
	n = (n >> 8 & 0x00ff00ff00ff00ff) + (n & 0x00ff00ff00ff00ff)
	n = (n >> 16 & 0x0000ffff0000ffff) + (n & 0x0000ffff0000ffff)
	n = (n >> 32 & 0x00000000ffffffff) + (n & 0x00000000ffffffff)
	return n


def check(i, n):
	ans = bitcount(i)
	i += 1
	while i < n:
		if bitcount(i) == ans: print('!!!!!!!!')
		i += 1

for i in range(1, 1000000):
	a = i

	b = a
	b |= b << 1
	b |= b << 2
	b |= b << 4
	b |= b << 8
	b |= b << 16
	b |= b << 32
	b &= 18446744073709551615  # only python

	c = a
	c ^= b
	c |= c << 1
	c |= c << 2
	c |= c << 4
	c |= c << 8
	c |= c << 16
	c |= c << 32
	c &= 18446744073709551615  # only python

	b = c
	b <<= 1
	b &= 18446744073709551615  # python
	b ^= c

	d = c
	# d = ~d  # dma
	d ^= 18446744073709551615
	d &= a

	a &= c
	a |= b

	b = d
	d >>= 1
	d &= b
	# b = ~b
	d ^= 18446744073709551615

	# d = b

	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e
	e = d
	e &= 1
	d >>= e


	d |= d << 1
	d |= d << 2
	d |= d << 4
	d |= d << 8
	d |= d << 16
	d |= d << 32
	d &= 18446744073709551615  # only python
	# d = ~d
	d ^= 18446744073709551615

	a |= d

	# print(a)
	check(i, a)
	# print(bin(i))
	# print(bin(a))


# 제출 코드
# mov B A
# mov F B
# shl F 1
# or B F
# mov F B
# shl F 2
# or B F
# mov F B
# shl F 4
# or B F
# mov F B
# shl F 8
# or B F
# mov F B
# shl F 16
# or B F
# mov F B
# shl F 32
# or B F
# mov C A
# xor C B
# mov F C
# shl F 1
# or C F
# mov F C
# shl F 2
# or C F
# mov F C
# shl F 4
# or C F
# mov F C
# shl F 8
# or C F
# mov F C
# shl F 16
# or C F
# mov F C
# shl F 32
# or C F
# mov B C
# shl B 1
# xor B C
# mov D C
# not D
# and D A
# and A C
# or A B
# mov B D
# shr D 1
# and D B
# not D
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# and E 1
# shr D E
# mov E D
# shl E 1
# or D E
# mov E D
# shl E 2
# or D E
# mov E D
# shl E 4
# or D E
# mov E D
# shl E 8
# or D E
# mov E D
# shl E 16
# or D E
# mov E D
# shl E 32
# or D E
# not D
# or A D



# 테스트용 코드

def bitcount(n):
	n = (n >> 1 & 0x5555555555555555) + (n & 0x5555555555555555)
	n = (n >> 2 & 0x3333333333333333) + (n & 0x3333333333333333)
	n = (n >> 4 & 0x0f0f0f0f0f0f0f0f) + (n & 0x0f0f0f0f0f0f0f0f)
	n = (n >> 8 & 0x00ff00ff00ff00ff) + (n & 0x00ff00ff00ff00ff)
	n = (n >> 16 & 0x0000ffff0000ffff) + (n & 0x0000ffff0000ffff)
	n = (n >> 32 & 0x00000000ffffffff) + (n & 0x00000000ffffffff)
	return n


def check(i, n):
	ans = bitcount(i)
	i += 1
	while i < n:
		if bitcount(i) == ans: print('!!!!!!!!')
		i += 1





reg = {x: 0 for x in [chr(c) for c in range(65, 91)]}

# i = 0x7fffffffffffffff
while 1:
	i = int(input(), 2)

	# if i % 1000 == 0: print(f'i: {i}')
	reg['A'] = i

	for l in cmds:
		if not l: continue
		l = l.split()
		cmd, R = l[0], l[1]

		if cmd == 'not':
			reg[R] = reg[R] ^ ((1 << 64) - 1)
			continue

		X = l[2]

		if cmd == 'mov':
			reg[R] = int(X) if X.isdigit() else reg[X]

		elif cmd == 'and':
			reg[R] &= int(X) if X.isdigit() else reg[X]

		elif cmd == 'or':
			reg[R] |= int(X) if X.isdigit() else reg[X]

		elif cmd == 'xor':
			reg[R] ^= int(X) if X.isdigit() else reg[X]

		elif cmd == 'shl':
			reg[R] <<= int(X) if X.isdigit() else reg[X]
			reg[R] &= ((1 << 64) - 1)

		elif cmd == 'shr':
			reg[R] >>= int(X) if X.isdigit() else reg[X]
			reg[R] &= ((1 << 64) - 1)

	print(reg['A'])
	print(bin(i)[2:].zfill(64))
	print(bin(reg['A'])[2:].zfill(64))
	# check(i, reg['A'])
	# print(reg['A'])
