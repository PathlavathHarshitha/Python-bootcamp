# write a code on inheritance on single,multi and multilevel:
class Animal:
    def speak():
        return " Animal is speaking "
#single inh:
class Dog(Animal):
    def Bark():
        return " Bow... "
#multiple inh:     
class Puppy(Dog):
    def Puppy_speak():
        return " im puppy "
obj1=Animal
obj2=Dog 
obj3=Puppy       
print(obj1.speak()) 
print(obj2.Bark())
print(obj3.Puppy_speak())
# multilevel inh:
class Father:
    def father_speak():
        return "Father class"
class Mother:
    def mother_speak():
        return "Mother class"
class Kid(Father,Mother):
    def kid_speak():
        return "Im kid. Im having properties of father"
obj1=Kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())




    

