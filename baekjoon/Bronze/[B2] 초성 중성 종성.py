x=ord(input())-44032
y=12496
print(chr(ord('abdghiqrsuvwxyz{|}~'[x//588])+y),chr(x%588//28+y+127),chr([32,ord(' abcdefgijklmnopqrtuvwxz{|}~'[x%28])+y][x%28>0]),sep='\n')