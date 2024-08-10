class Animal:
    def __init__(self):
        pass

class Pets(Animal):
    def __init__(self):
        pass

class Dog(Pets):
    def bark(self,n):
        print("bhow "*n)

a = Dog()
a.bark(50)