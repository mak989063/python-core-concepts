text = "ScalerAcademy"

print(text[::2])

print(text[::-1])

#Functions in string


s = 'john doe'
print(s.capitalize()) #capital

print(s.title()) #title

print(s.count('h')) # count frequency of substring

print(s.replace('h', 'mo'))  #replace substring in all the occurence

print(s.replace('o', 'xx', 1)) #replace only first occurence

names = "Mani,Iyshu,Mivaan"
print(names.split(','))     #output - ['Mani', 'Iyshu', 'Mivaan']

#convert an iterable to string
li = ["hi", "hello", "how"]
separator = "."
print(separator.join(li))   #hi.hello.how
print('.'.join(['2','3','4']))

print('hello world'.upper()) #upper
print('Hello World'.lower())  #lower

#formatted string
name = "Mani"
gender = "Male"
age = 30
print("name = ", name, "gender = ", gender, "age = ", age)

#create template - log files usage
template = "name={}, gender={}, age={}"
print(template.format(name, gender, age))

#method
print(f"name={name}, gender={gender}, age={age}")

template = "name={0}, gender={1}, age={2}"
print(template.format(name, gender, age))

#comparing strings & lists

print("Anj" > "Anil") # True j > i 3rd character


#List comparison

print([1,2,3,4] < [2,3])
