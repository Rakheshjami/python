'''
Inheritance:
This allows one class to acquire the properties and menthods of another class
Types:
-------------------------------
1.single inheritance:
A class inherts from a single parent class

class father:
    def land(self):
        print("I am father have 5A")
class child(father):
    def my_own(self):
        print("I have 2A")
obj=child()
obj.land()
------------------------------
2.multiple inheritance:
    
class father:
    def land(self):
        print("I am father have 5A")
class mother:
    def gold(self):
        print("mother have 5kg gold")
class child(father,mother):
    def my_own(self):
        print("I have nothing")
obj=child()
obj.land()
obj.gold()
-------------------------------------
3.multilevel inheritance:
A class inherits from a parent class and another class inherits from that child class
class grandfather:
    def land(self):
        print("I am father have 5A")
class father(grandfather):
    def flat(self):
        print("Have flat at BNG")
class child(father):
    def my_own(self):
        print("I have nothing")
obj=child()
obj.land()
obj.flat()
----------------------------------------
4.hierarchial inheritance
multiple child classes onherits from a single parent.
class father:
    def land(self):
        print("I am father have 10A")
class child_1(father):
    def job(self):
        print("Job")
class child_2(father):
    def study(self):
        print("Study")
obj1=child_1()
obj2=child_2()
obj1.land()
obj2.land()
-------------------------------------
5.Hybrid inheritance
This is combination of two more types of inheritance
class A:
    def m1(self):
        print("class A")
class B(A):
    def m2(self):
        print("class B")
class C(A):
    def m3(self):
        print("class C")
class D(B,C):
    def m4(self):
        print("class D")

obj=D()
obj.m1()
obj.m2()
obj.m3()
obj.m4()
----------------------------------------------
super():
It is used to access methods and constructor of the parent class from the child class from the child class

class parent:
    def disp(self):
        print("class parent")
class child(parent):
    def display(self):
        super().disp()
        print("class child")
obj=child()
obj.display()


constructor:
'''
class parent:
    def __init__(self,name):
        self.name=name
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
obj=child("rakesh",21)
obj.display()


















