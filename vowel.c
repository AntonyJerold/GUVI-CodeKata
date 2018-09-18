cha= input("enter alphabet: ")
if(cha.isalpha()==1):
    if cha in ('a', 'e', 'i', 'o', 'u'):
        print("%s is a vowel." % cha)
    else:
        print("%s is a consonant." % cha)
else:
    print("Ivalid")
