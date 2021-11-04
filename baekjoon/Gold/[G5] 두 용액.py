input()
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = len(arr) - 1
ans = 999999999999
ans_left, ans_right = left, right

while 1:
	mix = abs(arr[left] + arr[right])
	if ans > mix:
		ans = mix
		ans_left = left
		ans_right = right
	if right - left == 1: break
	move_left = abs(arr[left + 1] + arr[right])
	move_right = abs(arr[left] + arr[right - 1])
	if move_left < move_right: left += 1
	else: right -= 1


print(arr[ans_left], arr[ans_right])
