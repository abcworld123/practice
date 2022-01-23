N,M=map(int,input().split())
print([[ord(c)-14for c in l]for l in'   2 m 7ħҭᩖ #̛ܰ 0§࣓ፉ⇯ᗍ↫ Eᣎ៫⚴ gɉ΅ḥᑦ᯹ڭऩᗴ ڲ܀᾽῭ ÷ࡡ᭙ᔀܑᘍआ⃪ᗐႼ΃ ƇᴀᯃẘἼۜ ɰ἟ᠴᗴᢟ὘ᰝբᠥຝ຿ྑϬ'.split()][max(N,M)-1][min(N,M)-1])



# O(1)로 풀어버림..;
# 배열 생성 코드는 아래 (성능은 그닥)
ans = [[0] * 14 for _ in range(14)]

def dfs(i, j, n):
	# for x in arr: print(*x)
	# print('-' * 50)
	if n == full: return 1
	sarr = str(arr)
	if sarr in dic: return dic[sarr]
	ret = 0
	while 1:
		if arr[i][j] == 0:
			if arr[i][j + 1] == 1 and arr[i + 1][j] == 1: return 0
			arr[i][j] = 1
			if arr[i][j + 1] == 0:
				arr[i][j + 1] = 1
				ret += (dfs(i, j + 2, n + 1) if j + 2 < M else dfs(i + 1, 0, n + 1))
				arr[i][j + 1] = 0
			if arr[i + 1][j] == 0:
				arr[i + 1][j] = 1
				ret += (dfs(i, j + 1, n + 1) if j + 1 < M else dfs(i + 1, 0, n + 1))
				arr[i + 1][j] = 0
			arr[i][j] = 0
			dic[sarr] = ret
			break
		else:
			j += 1
			if j == M:
				j = 0
				i += 1

	return ret

for N in range(1, 15):
	for M in range(1, N + 1):
		# print(N, M)
		if (N * M) & 1:
			print(0)
			continue
		full = N * M // 2
		arr = [[0] * M + [1] for _ in range(N)] + [[1] * (M + 1)]
		dic = {}
		# 14, 14: 112202208776036178000000

		print(dfs(0, 0, 0) % 9901)

# for a in ans: print(a)
