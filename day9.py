'''
table
---------------
num=int(input())
for i in range(1,11):
    print(num,"*",i,"=",num*i)'''
'''
string rev
----------------
s=input()
empt=""
for j in s:
    empt=j+empt
print(empt)
'''
'''
armstrong
---------------
num=int(input())
n=num
som=0
pow=len(str(num))
while n>0:
    mod=n%10
    som+=mod**pow
    n//=10
if num==som:
    print("armstrong")
else:
    print("not armstrong")'''

'''
perfect
--------------
num=int(input())
tot=0
for i in range(1,num):
    if num%i==0:
        tot+=i
if tot==num:
    print("perfect")
else:
    print("not a perfect")'''
'''
prime
--------------'''
'''num=int(input())
c=0
for i in range(1,num+1):
    if num%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not a prime")'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()'''
        
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()'''

'''num=int(input())
c=0
for i in range(1,num+1):
    for j in range(1,i+1):
        c+=1
        print(c,end=" ")
    print()'''

'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''



























