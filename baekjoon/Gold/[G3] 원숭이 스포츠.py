n = int(input())
arr = [
	'AB' * 64,
	'AABB' * 32,
	'AAAABBBB' * 16,
	('A' * 8 + 'B' * 8) * 8,
	('A' * 16 + 'B' * 16) * 4,
	('A' * 32 + 'B' * 32) * 2,
	'A' * 64 + 'B' * 64
	][:(n - 1).bit_length()]

while len(arr) < 7: arr.append(arr[-1])
for x in arr: print(x[:n])
