a=[];
i=1
n=int(input("Enter the Size N:"));
if( n <= 1):
    print("INVALID SIZE");
else:
    while(i<=n):
        st=str(input("Enter the String:"));
        if(len(st)>=100000):
            print("String is Too large RE-ENTER\n");
        else:
            a.append(st);
            i=i+1;             
    if (len(a) == 0): 
        print("The longest Common Prefix is : NULL"); 
    if (len(a) == 1): 
        print("The longest Common Prefix is :",a[0]); 
    else:
        a.sort() 
        stop = min(len(a[0]), len(a[len(a) - 1]))
        i = 0
        while (i < stop and a[0][i] == a[len(a) - 1][i]): 
            i += 1
  
        pre = a[0][0: i]
        print("The longest Common Prefix is :" ,pre);
