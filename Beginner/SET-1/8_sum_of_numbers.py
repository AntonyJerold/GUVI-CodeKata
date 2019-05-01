n=int(input("Enter The Number:"))
sum=0
if(n>0):
  for i in range (1,n+1):
    sum=sum+i
  print("Sum=",sum)

else:
  print("Invalid Input")
