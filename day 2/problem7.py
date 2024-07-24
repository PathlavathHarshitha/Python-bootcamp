    #u r given with a comma seperated with a natural numberb 1 to 10 print only the even numbers
my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
        count+=1
        print(count)