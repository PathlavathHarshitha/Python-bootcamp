# prime number using square
#my_list=list(map(int,input().split()))
#a=int(input("enter a number:"))
#r=a**0.5
#count=0
#if count==0:
 #   print("not a prime")
#else:
 #   print("prime")
#for i in range(2,int(r+1)):
 #   if a%i==0:
  #      count=1
   #     break

#write a program to print all the prime numbers in a given range:
a=int(input("enter a value of a:"))
b=int(input("enter a value of b:"))
for i in range(a,b+1):
    for j in range(2,i):
     if i%j==0:
      break
else:
     print(i)



