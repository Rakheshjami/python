'''
Data Abstraction:
This is the process of hiding internal implementaton details and showing only essential features to the user
-> It focuses on what an object does rather than how it does it.


'''
from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def parameters(self):
        pass
class Rec(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def perimeter(self):
        return 2*(self.a+self.b)
an=Rec(10,5)
print(an.area())
    
