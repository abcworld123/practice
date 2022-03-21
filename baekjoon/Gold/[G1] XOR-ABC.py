K=int(input())
m=3000009
print(~-pow(2,K,m)*~-pow(2,K-1,m)%m//3)