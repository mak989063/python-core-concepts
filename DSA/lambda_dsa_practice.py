# Write Lambda functions Tutorial -  23 March 2026

#1. Add 2 numbers
add = lambda x,y:x+y
print(add(10,20))

#2. get first char of a string
first_char = lambda word:word[0]
print(first_char("Hello"))

#3. check if a number is even or not
is_even = lambda x:x%2==0
print(is_even(5)) #False

#4. conver string to a upper case
convert_upper = lambda word:word.upper()
print(convert_upper("Hello"))

#5. Quiz - 1
get_last = lambda s: s[-1]
print(get_last("Scaler"))

# sorted + lambda
words = ["apple", "kiwi", "banana"]
words_sort_based_on_num_chars = sorted(words, key = lambda x: len(x))
print(words_sort_based_on_num_chars)

# sort numbers by absolute value
numbers  = []
sort_by_abs_value = sorted(numbers, key = lambda x: abs(x))

#sort tuples
tup = ((1,5),(4,2),(7,3))

sort_tuple = sorted(tup, key = lambda x: x[0])
print(sort_tuple)

#sort dict based on scores
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 70}
]
students_sorted = sorted(students, key=lambda x: x["score"])
print(students_sorted)

#Quiz - 2
names = ["Scaler", "AI", "Learning"]
print(sorted(names, key=lambda x: len(x)))

#Time Stamp on servers - UTC time

