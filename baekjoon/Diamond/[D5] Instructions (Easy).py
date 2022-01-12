
x = 130

y = x & 0b111
# print(bin(x)[2:].zfill(64))

x >>= 3
# a = ~x
a = x ^ ((1 << 61) - 1)  # not

a |= a << 1
a |= a << 2
a |= a << 4
a |= a << 8
a |= a << 16
a |= a << 32
a &= ((1 << 61) - 1)  # only python

# print(bin(a)[2:].zfill(64))

xl = x & a
xr = (a << 1) | x
xr &= ((1 << 61) - 1)  # only python

# print(bin(xl)[2:].zfill(64))
# print(bin(xr)[2:].zfill(64))

# print(bin(~xr)[2:].zfill(64))

ans = xl | (xr ^ ((1 << 61) - 1))  # xl | ~xr
ans <<= 3
ans |= y
print(ans)


# 제출 코드
# mov B A
# and B 7
# shr A 3
# mov C A
# not C
# mov D C
# shl D 1
# or C D
# mov D C
# shl D 2
# or C D
# mov D C
# shl D 4
# or C D
# mov D C
# shl D 8
# or C D
# mov D C
# shl D 16
# or C D
# mov D C
# shl D 32
# or C D
# mov F A
# and A C
# shl C 1
# or F C
# not F
# or A F
# shl A 3
# or A B
