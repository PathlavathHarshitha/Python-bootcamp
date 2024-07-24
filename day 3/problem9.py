# find the element present in k+N index
#k=3
#N=2
#3 6 8 4 61 2
#op:2
my_list=list(map(int,input().split(" ")))
k=int(input())
N=int(input())
for i in range (0,len(my_list)):
    print(my_list[k+N],end=" ")
    break

#find the element in a particular index but the codition is cyclic printing
#k=3
#3 6 8 4 61 2
#op:4
my_list=(list(int,input().split(" ")))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])

