'''
Type coversions
-----------------
'''
a=678
b=str(a)
print(type(b))
c=float(a)
print(type(c))
#-------------
s="789"
d=int(s)
print(type(d))
e=float(s)
print(type(e))
f=list(s)
print(f)
print(type(f))
g=tuple(s)
print(g)
print(type(g))
#----------------
fl=56.78
h=int(fl)
print(h)
print(type(h))
#-----------------------
listt=[1,2,3,4]
print(type(str(listt)))
print(type(tuple(listt)))
#----------------------
tup=(1,2,3,4)
print(type(list(tup)))
print(type(str(tup)))
#-------------------------------
'''num=int(input("Enter a number:"))
print(num)'''
#----------
'''string=input("Enter a text:")
print(string)'''
#------------
'''list1=list(map(int,input("Enter a list:").split()))
print(list1)'''
#------------
'''tup1=tuple(map(int,input("Enter a tuple:").split()))
print(tup1)'''
x=eval(input("enter :"))
print(x)

