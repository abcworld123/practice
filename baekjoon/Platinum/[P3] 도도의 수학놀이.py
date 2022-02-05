import sys
input = sys.stdin.readline

rotate = lambda s: s.replace('9', '_').replace('6', '9').replace('_', '6')[::-1]

input()
arr = sorted(rotate(input()).split(), key=lambda x: x * 6, reverse=True)
twice = max(arr, key=lambda x: len(x))
arr.insert(arr.index(twice), twice)

sys.stdout.write(rotate(''.join(arr)))
