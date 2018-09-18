cha= input("Enter Alphabet: ")
if(cha.isalpha()==1):
    if cha in ('a', 'e', 'i', 'o', 'u'):
        print("Vowel")
    else:
        print("Consonant" )
else:
    print("Ivalid")
