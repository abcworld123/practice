for _ in range(int(input())):
    x = int(input())
    print(['NIE', 'TAK'][x % 9 == 0 or x % 3 == 2])
