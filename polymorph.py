'''
polymorphism:
It means 'many forms'..it allows the same function,method,or operator to behave differently depending on the object.


1.method overloading:

class calc:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
obj=calc()
print(obj.add(5,5))
print(obj.add(5,5,5))
---------------------------------

2.method overriding:
This occurs when a child class provides its own implementation of a method already defined in the parent class

class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
obj=animal()
obj.sound()
---------------------------------
operator overloading:
This allows operators such as +,-,* etc,,to perform different actions for user defined objects
note:The operator inside the method will overload a special method or operator given in the call
'''
class stu:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
ob1=stu(4)
ob2=stu(5)
print(ob1+ob2)













