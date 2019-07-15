m=input();
n=input();
l=0;    
if len(m)<len(n):
    l=len(m);
else:
    len(n);
u=abs(len(m)-len(n));
count=u;
for i in range(l):
  if(len(n)==1 and n[i] in m):
    break;
  if(m[i]!=n[i]):
    count+=1;
print(count);
