# print the non repeating or unique characters in a given string:
vowel="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
ans=" "
i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
       ans+=i
print(ans)