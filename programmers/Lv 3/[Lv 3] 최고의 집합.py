solution=lambda n,s:[[s//n]*(n-s%n)+[s//n+1]*(s%n),[-1]][n>s]
