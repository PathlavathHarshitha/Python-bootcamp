#find the maximum element in the given list
#test case:0
#12 23 36 44 45 57
#57
#test case=1
#56 78 -8 12 34 -99
#78
my_list=list(map(int,input().split(" "))) 
print(max(my_list))

#method two
my_list=list(map(int,input().split(" ")))
maxi=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
        print(maxi)
    