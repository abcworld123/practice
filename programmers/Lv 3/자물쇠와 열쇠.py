def rotate(key):
    length = len(key)
    newkey = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            newkey[j][length - i - 1] = key[i][j]
    return newkey

def check(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    for i in range(1 - len_key, len_lock):
        for j in range(1 - len_key, len_lock):
            success = True
            for x in range(len_lock):
                for y in range(len_lock):
                    key_can = key[x - i][y - j] if 0 <= x - i < len_key and 0 <= y - j < len_key else 0
                    lock_can = lock[x][y]
                    if key_can + lock_can != 1: success = False
            if success: return True
    return False

def solution(key, lock):
    for i in range(4):
        if check(key, lock): return True
        if i < 3: key = rotate(key)
    return False
