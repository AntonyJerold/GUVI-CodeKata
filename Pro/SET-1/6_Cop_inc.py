n=int(input());
a=list(map(int,input().split()));
b=0;
for i in range(n):
  for j in range(i,n-1):
    for k in range(j,n-1):
      if(a[i]<a[j]<a[k]):
        b=b+1;

print(b);

