count = 0
num=int(input("Enter The Number:"));
temp=num
while(temp != 0):
    temp=(int)(temp/10)
    count=count+1
print("Number of digits:" ,count,"in Given Number \"",num,"\"");
