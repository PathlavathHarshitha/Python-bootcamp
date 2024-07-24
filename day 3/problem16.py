#sum of digits: while
# 123 1+2+3=6
my_list=list(map(int,input().split(" ")))
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)
