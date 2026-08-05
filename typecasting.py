#Typecasting a process of converting a variable from one data type to another i.e str(),int(),float(),bool().
#useful in handling user input


name = "Nathaniel"
age = 29
gpa = 3.72
is_student = False

#from float to integer
# gpa = int(gpa)
# print(gpa)

#from integer to float
# age = float(age)
# print(age)

#integer to float
# age = str(age)
# print(age)

#from string to bool. Remember if nothing is entered in the quotations assigned to the name variable then it becomes false. This can be used to check if someone entered their name or not.

name = bool(name)
print(name)

#casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#error if you attempt to cast incorrect data(you can try this code
zip_value = int("New York")

