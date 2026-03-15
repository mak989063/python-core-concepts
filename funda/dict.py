d = {'a':1,'b':2,'c':3}

print(d.get('a'))

#if key is not present in the dict
print(d.get('d','xyz'))


a = {True:1,False:2,"Keerthi":"Instr", "Mani":"Stud",100:"Hundred","pi":3.14, "names":['name1', 'name2', 'name3']}
print(a)

#A dict element can be another dict.
#insert

a['Iyshu'] = "super cool"
a['names'] = ['name1', 'name2']
print(a)
#how many keys in the dict
print(len(a))

#how to delete
a.pop("names") #removes key 'names'
a.pop("Sachine","hello")
del a['Iyshu']
print(a)

#Iterate over a dictionary
scores = {"J":50, "K":60, "L":70, "M":80, "N":90}
print(scores.keys()) # returns list contains all the keys
print(scores.values()) ## returns list contains all the values

#1st way
for key in scores:
    print(key,scores[key])

#2nd way
for key,value in scores.items():
    print(key,value)

#How to check an element in present or not

print("Z" in scores) #False
print("K" in scores) #True

a = {'a': 'A'}
print(type(a))
a = {'Scaler': 1}
a.pop('Scaler')
print(len(a))

