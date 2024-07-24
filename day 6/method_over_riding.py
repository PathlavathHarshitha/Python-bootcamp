class Animal:
    def Speak():
        return "speaking...."
class Dog(Animal):
    def Speak():
        return "Dog is speaking"
class puppy(Dog):
    def Speak():
        return "puppy is speaking"      
obj3=puppy 
print(obj3.Speak())
         