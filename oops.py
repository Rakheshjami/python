'''
oops
----------------------
1.class:
A class is a blueprint or template used to create an object
eg:
class student:
  name="rakesh"
-----------------------
2.object:
object is an instance of a class.
class stud:   #class
    def educ(self):
        print("hi how are you")
s1=stud()    #object
s1.educ()
----------------------------
Attributes:
Attributes are the variiables that belongs to a class or an object

class stu:
  name='rakesh'
  age=21
s1=stu()
prinnt(s1.name)
print(s1.age)
------------------------------
Methods:
methods are functions defined in the class
class pfs_da:
    def python(self):
        pfs_da='Batch3'
        print('This is pfs and ds batch3')
    def flask(self):
        print('This is pfs')
obj=pfs_da()
obj.python()
obj.flask()
-----------------------------
constructor: __init__
A constructor is a special method that is automatically called when object is created

class Atm:
    def __init__(self,Balance,name):
        self.Balance=Balance
        self.name=name
        print(f"{self.name} your total balace is {self.Balance+7000}")
        print(self.name)

card=Atm(Balance=5000,name='rakesh')
---------------------------------------
Access specifiers:
public->This can be accessed from any where in the program 
protected->This is represented using underscore(_)
private->This is represented using double underscore(__)


class stu:
    name='rakesh'
    _age=21
    __branch='cse'
s=stu()
print(s.name)
print(s._age)
print(s._stu__branch)

-----------------------------------------------
Encapsulation:
It is the process of binding data and methods together
'''
class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def depo_(self,amount):
        self.__balance+=amount
    def get_bal(self):
        return self.__balance
acc=Bank(1000)
acc.depo_(1000)
acc.get_bal()



















        
 
