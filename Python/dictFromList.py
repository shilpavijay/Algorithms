l = [1,2,3,3,5,1,2,3,4]

d = {}
for each in set(l):
    d.update({each:l.count(each)})
# OR

# {d.update({each:l.count(each)}) for each in set(l)}

print(d)

OR 
from collections import Counter
c=Counter(l)
print(c)


#DICT FROM TWO LISTS
a=['a','b','c']
b=[1,2,3]

lstDict = dict(zip(a,b))
print(lstDict)