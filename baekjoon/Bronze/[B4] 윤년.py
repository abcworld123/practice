y=int(input())
print(1 if y%400==0 else 0 if y%100==0 else 1 if y%4==0 else 0)
