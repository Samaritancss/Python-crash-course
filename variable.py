#variable = A container for a value i.e (string, integer, float, boolean)
# A variable behaves as if it was the value it contains

#1 STRINGS

#literal assignment
#first = "Nat"
#last = "Abeka"
#print(type(first))

# first_name = "Nathaniel"
# print(first_name)

#with the f-string (f means format). It aids you form a sentence with your assigned variable.

# first_name = "Nathaniel"
# print(f"Hello {first_name}!")

#STRINGS
# first_name = "Nathaniel"
# food = "waakye"
# email = "nathanielabeka03@gmail.com"
# print(f"Good morning {first_name}")
# print(f"You like {food}")
# print(f"Your email is : {email}")

#concatenation
#first = "Nat"
#last = "Abeka"
#fullname = first + " " + last
#print(fullname)
#fullname += "!"
#print(fullname)

#Casting a number to a string
# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = "I like rock music from the " + decade + "s."
# print(statement)

#multiple lines
# multiline = '''
# Hey, how are you?

# I was just checking in.
#                                  All good?

# '''
# print(multiline)

# Escaping special characters
# sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at \\located?'
# print(sentence)

# BUILD A MENU
# print("")

# title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee" .ljust(16, ".") + "$1" .rjust(4))
# print("Muffin" .ljust(16, ".") + "$2" .rjust(4))
# print("Cheesecake" .ljust(16, ".") + "$3" .rjust(4))

#checking for boolean data
# first = "Nat"
# print(first.startswith("N"))
# print(first.endswith("a"))

#2 INTEGERS (A whole number. Remember integer should always not be in quotes that means it a string)


# age = 25
# courses = 6
# num_of_students = 26

# print(f"You are {age} years old. You offer {courses} courses and you are {num_of_students} students  in class")

#3 FLOAT (A number but contain decimals)
# price = 8.99

# print(f"The price is {price}")

# price = 10.99
# gpa = 3.72
# hours = 3.42

# print(f"Because you had a gpa of {gpa} you will earn ${price} for studying {hours} hours.")

#4 BOOLEAN(Is either true or false)
#You can set it to true or false

# is_millionaire = True

# if is_millionaire:
#     print("You are a millionaire")
# else:
#     print("You are not a millionaire")

# for_sale = False

# if for_sale:
#     print("The item is forsale")
# else:
#     print("The item is Not forsale")

# is_online = True

# if is_online:
#     print("You are online")
# else:
#     print("You are offline")


#meaning
# meaning = 42
# print('')

# if meaning > 10:
#     print('Right on!')
# else:
#     print('Not today')

# #Ternary operator
# print('Right on!') if meaning  > 10 else print('Not today')

#complex type (use in electrical engineering)
# comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)
