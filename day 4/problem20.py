#mr.x is trying to create a new password for his instagram account. This are the
#required conditions for creating a new password
# i) minimum length is 8 maximum length is 15
# ii) condition two only @,/ is allowed in a password
# iii) no spaces are allowed
# iv) only alpha numerics are allowed
# you are supposed to print weak if length exact 8 medium length is between 8 to 12
# strong if length is between 12 to 15
#password=input("enter password")
#n=len(password)
#if n<8:
 #   print("follow the cond:")
  #  str[0]='@'
   # str[1]='/'
    #for i in password:
     #   if(i in str[0] or str[1]): and i not=" "
      #  count+=1
       # break;

#peek values or elements:
# 5 12 8 17 18
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i-1]<my_list[i] and my_list[i]>my_list[i+1]:
       count=i
       break
print(my_list[count])
