num = int(input("Enter the Number (NUMBER <= 20):"));
fact=1;
if( num > 20):
    print("size INVALID");
else:
    if num < 0:
       print("Negative numbers cannot be factorized");
    elif num == 0:
       print("The Factorial of",num,"is : 1")
    else:
       for i in range(1,num + 1):
           fact = fact*i
    print("The Factorial of",num,"is:",fact);
