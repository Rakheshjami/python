'''
sets
-------------------
'''
set1={1,2,2,3,4,5,7,65,987,23}
print(set1)
set2={7,4,8,6,4,9,2,65,2,87}
print(set1.union(set2))
print(set1 | set2)
print(set1 & set2)
print(set1.intersection(set2))
print(set1 - set2)
print(set1.difference(set2))
print(set1 ^ set2)
set1.add(32)
print(set1)
set1.update({33,34,35})
print(set1)
set1.remove(65)
print(set1)
set1.pop()
print(set1)


