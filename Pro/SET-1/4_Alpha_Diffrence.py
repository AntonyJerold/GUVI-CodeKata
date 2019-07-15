d,a=map(str,input().split());
f=0;
if len(d)>len(a):
   d,a=a,d;
r=0
while r<len(d):
   f+=(ord(a[r])-ord(d[r]));
   r+=1;
for r in range(r,len(a)):
   f+=ord(a[r])-ord('a')+1;
print(f);
