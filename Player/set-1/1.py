r = ""
s = str(input("Enter the String:"));  
print ("The given string  is : ",s)
if(len(s) > 100000):
    print("size INVALID");
else:
    for i in s: 
        r = i + r
    print ("The reversed string:",r) 
