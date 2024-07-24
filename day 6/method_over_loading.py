class cal:
    #def add(a,b,c):
     #   return a+b+c
    #def add(a,b,c,d):
     #   return a+b+c+d
    #def add(a,b,c,d,e):
     #   return a+b+c+d+e 
    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        return(sum) 
#take inputs:
obj1=cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
