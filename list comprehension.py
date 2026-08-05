#list comprehension = A concise way to create lists in python
# compact and easier to read than traditional loops
# [expression for value in iterable if condition]

#double number 1-10

# doubles = []
# for x in range(1,11):
#     doubles.append(x * 2)

# print(doubles)

#simplified

# doubles = [x * 2 for x in range(1, 11)]

# triples = [y * 3 for y in range(1, 11)]

# squares = [z * z for z in range (1, 11)]

# print(triples)

# fruits = ["apple","orange","banana","coconut"]

# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6]

# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]

# print(even_nums)

# grades = [85, 42, 79, 90, 56, 30]
# passing_grades = [grade for grade in grades if grade >=60]

# print(passing_grades)

users = ['Nat','John','Sara']

data = ['Nat', 29, True]

empty_list = []

print("Nat" in empty_list)

print(users[0])
print(users[-2])

print(users.index('Nat'))
users.append('Hannah')
users.extend(['rashid','Yayha'])
print(users)

users.remove('Nat')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
# data.clear()

users.sort()
print(users)

users.sort(key=str.lower)
print(users)


nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

nums.sort(reverse = True)
print(nums)

print(sorted(nums, reverse = True))
print(nums)

nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]

print(type(nums))

my_list = list([1,"Gabby", True])
print(my_list)

# Tuples

my_tuples = tuple(('Jill', 30, False))
another_tuple = (1,4,5,6)

print(my_tuples)
print(type(my_tuples))
print(type(another_tuple))

new_list = list(my_tuples)
new_list.append('Dajif')
new_tuple = tuple(new_list)
print(new_tuple)



