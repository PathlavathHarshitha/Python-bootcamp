# remove all the brackets from the given algebric expression:
#inp=input()
#for i in inp:
 #   if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
  #    pass
   # else:
    #    print(i,end=" ")
#print()

#*****encoding and decoding (this have real time examples):-
#print abc=input string 4 is the skip value then output should be a EHG
#inp=input()
#for i in inp:
 #   print(chr(ord(i)+4),end=" ")
  #  print()

# input hello-----wor----ld
# output ---------helloworld 
inp=input()
count=0
ans=""
for i in inp: 
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)


