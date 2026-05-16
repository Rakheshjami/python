'''
concatination
------------------------
'''
a=9
b=8
print(a+b)
str1="hello"
str2="world"
print(str1+str2)
list1=[1,2]
list2=[3,4]
print(list1+list2)

'''
Tuple
------------------
'''
tup=(1,"python",[1,2],(3,4))
print(tup)
print(tup[1])
print(tup.count(1))
print(tup.index([1,2]))
tup1=(1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4])
print(tup1[2][2][1])
'''
dictionary
-------------
'''
dict1={"name":"Python",1:2,(1,2):[3,4]}
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get("name"))
print(dict1["name"])
dict1.update({"age":25}) #can add new items
print(dict1)
dict1["name"]="Rakesh"
print(dict1["name"])
dict1["branch"]="cse" #can add new item
print(dict1)
dict1.clear()
print(dict1)


