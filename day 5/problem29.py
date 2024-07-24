 # print all the vowels which are followed by consonants:
str=input()
vowel="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
count=0
for i in(str):
    if(i in consonants):
        print(i,end=" ")
        for i in(str):
            if(i in vowel):
              print(i,end=" ")
