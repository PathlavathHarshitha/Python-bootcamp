#find the minimum element in a gioven list
#test case=0
#12 23 36 44 45 57
#op:57
#test case=1
#
my_list=list(map(int,input().split(" ")))
mini=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<mini):
        mini=my_list[i]
        print(mini)