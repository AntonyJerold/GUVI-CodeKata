a=[]
n=int(input("Enter No.Of Elements:"))
for i in range(n):    
    v=int(input("Enter The Array Value :"))
    a.append(v)
k=int(input("Enter The Value For less than N:"))
sum=0
for i in range(k):    
    sum=a[i]+sum
print("Sum of",k ,"Elements in Array=",sum)
