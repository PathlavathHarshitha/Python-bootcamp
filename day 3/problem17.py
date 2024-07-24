#find the sum of squares of a digit in a given number
#n=123
#sum=0
#while n>0:
 #    r=n%10
  #   sum=sum+r**2
  #   n=n//10
#print(sum)

#sum of even digits in a given number
n=1234
sum=0
while n>0:
     r=n%10
     if(r%2==0):
        sum=sum+r
        n=n//10
print(sum)