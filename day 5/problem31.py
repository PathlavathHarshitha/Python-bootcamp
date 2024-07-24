#print sum of the digits from hello123world:
vowel="aeiou"
consonant="bcdfghjklmnpqrstvwxyz"
check="0123456789" 
ans=0
i="hello123world"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
        print(ans)
