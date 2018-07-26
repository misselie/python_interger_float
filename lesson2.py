letters=['a','d','f','w']
print(letters)
print(letters[0:2])
letters.append('q')
print(letters)

letters.insert(2,'o')
print(letters)

letters.remove('d')
print(letters)

last_letter=letters.pop()
print(last_letter)
print(letters)
print("o" in letters)
boxes=[1,3,4,6,4,2,6,9]
for i in boxes:
  print(i)
letters.reverse()
print(letters)
boxes.sort()
print(boxes)
print(sum(boxes))
names=['elie', 'ozan', 'leila', 'bobo']
name_str='-'.join(names)
print(len(name_str))
print(type(name_str))
print(name_str)
b=name_str.split('-')
print(b)
print(len(b))

list1=['a','d','f','w']
list2=list1
print(list1)
print(list2)
list1[0]='y'
list2[2]='a'
print(list1)
print(list2)

arr_tuple=('a','d','f','w')
print()
print(arr_tuple) #tuple cannot change since it is imutable unlike list is,it is static 

arr_set1={'a','d','f','w'}
print(arr_set1)
arr_set2={'h','o','k','a'}
print(arr_set1.intersection(arr_set2))
print(arr_set1.difference(arr_set2))
print(arr_set1.union(arr_set2))
