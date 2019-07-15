from itertools import combinations
n=int(input("Enter a Number:"));
m=int(input("Enter a number to delete digits:"));
le=len(str(n))
a=list(combinations(str(n),le-m))
a=(sorted(a))
b="".join(a[0])
print("After Deleting the given number:",b);
