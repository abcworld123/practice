a,b=map(int,(input().split(' ')))
c=1395+a*60+b
print(c%1440//60,c%60)
