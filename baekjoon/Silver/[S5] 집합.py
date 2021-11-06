import sys
input = sys.stdin.readline

S = 0
for i in range(int(input())):
	cmd = input().split()
	if cmd[0][1] == 'd': S |= 1 << int(cmd[1])
	elif cmd[0][1] == 'h': print(1 if S & (1 << int(cmd[1])) else 0)
	elif cmd[0][1] == 'e': S &= ~(1 << int(cmd[1]))
	elif cmd[0][1] == 'o': S ^= 1 << int(cmd[1])
	elif cmd[0][1] == 'l': S = 2097150
	elif cmd[0][1] == 'm': S = 0
