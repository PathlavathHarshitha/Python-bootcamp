#person x goes to market to by 10 apples 2dz bananas 3 oranges cost of 
# 1 apple=15, 1 banana=4, 1 0range=5
cost_apple=15
cost_banana=4
cost_orange=5
#no.of fruits
print("enter no.of apples")
no_apples=int(input())
print("enter no.of bananas")
no_bananas=int(input())
print("enter no.of oranges")
no_oranges=int(input())
print("enter the amount given by mother")
amount_given=int(input())
sum=(no_apples*cost_apple)+(no_bananas*cost_banana*12*4)+(no_oranges*cost_orange)
if(sum<=amount_given):
    print("not cheated")
else:
    print("cheated")
