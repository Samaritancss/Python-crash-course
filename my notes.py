#DISTANCE BETWEEN TWO POINTS
# import math
# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))
# distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print("The distance is", round(distance,2))

# print("grand" "mother")

#A PROGRAM FORA TIP
# tip = float(11/100)
# total = float(input("Enter your total bill:"))
# if total > tip:
#     print(f"Your tip is {tip * total}")
# else:
#     print("You didn't enter your total bill")

#say hello to user remove white spaces and capitalize 
# name = input("Enter your name: ").strip().title()

# print(f"Your name is {name}")

# using some function sep and end
# name = input("Enter your name: ")
# print(f"Your name is {name}", sep="???") 

#USING THE DEF FUNCTION
# def hello(to):
#     print("hello", to)

# name = input("What's your name?: ")
# hello(name)

# def main():
#     x = int(input("Enter a number for x?:"))
#     print(f"x squared is ", square(x))

# def square(n):
#     return n * n /pow(n,2)

# main()


#CONDITIONS
# score = int(input("Enter a score: "))

# if score >= 90 and score <= 100:
#     print("Your  Grade is A")
# elif score >= 80 and score < 90:
#     print("you  Grade  is B")
# elif score >= 70 and score < 80:
#     print("Your  Grade is C")
# elif score >= 60 and score < 70:
#     print("Your  Grade is  D")
# else:
#     print("You Grade is F")

#FUNCTIONS

# def main():
#     x = int(input("Enter a number for x: "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# main()

# list = [2,23,39,6,-5]
# list[2]=int(35)
# print(list)

# reducing lines of code
# name = input("Enter your name: ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

#USING MATCH CASE
# name = input("Enter your name: ")

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermoine":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

#a shorter form
# name = input("Enter your name: ")

# match name:
#     case "Harry" | "Hermoine" | "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

#LOOPS (WHILE LOOPS)
# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1

#OR (WHILE LOOPS)
# i = 0
# while i < 3:
#     print("meow")
#     i += 1

#FOR LOOPS
# for i in range(3):
#     print("meow")

# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("What's n?: "))
#         if n > 0:
#             return n

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

#LIST
# students = ["Hermoine","Harry","Ron"]

# for student in students:
#     print(student)

# students = ["Hermoine", "Harry", "Ron"]

# for student in range(len(students)):
#     print(student + 1, students[student])

#DICTIONARY
# students = {
#     "Hermoine":"Gryffindor",
#     "Harry":"Gryffindor",
#     "Ron":"Gryffindor",
#     "Draco":"Slytherin",
# }
#will print only the keys
# for student in students:
#     print(student)

#will print both key and value
# for student in students:
#     print(student, students[student], sep=", ")

# students = [
#     {"name": "Hermoine", "house": "Gryffindor", "patronus":"otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus":"Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus":"Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus":"None"},
# ]

# for  student in students:
#     print(student["name"], student["house"],student["patronus"], sep=", ")

# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()

#shorter form
# def main():
#     print_column(3)

# def print_column(height):
#     print("#\n" * height, end="")

# main()

# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()

# def main():
#     print_square(3)

# def print_square(size):

#     #for each row in square
#     for i in range(size):

#         #for each column in square
#         for j in range(size):

#             #print brick
#             print("#", end="")
        
#         print()

# main()

#TRY STATEMENT
# while True:

#     try:
#         x = int(input("Enter a number for x?: "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")


# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("Enter a number for x?: "))
#         except ValueError:
#             print("X is not an integer")
#         else:
#             break
#     return x

# main()

#IMPORTING THE RANDOM MODULE
#tossing a coin
# import random

# coin = random.choice(["heads","tails"])
# print(coin)

#choosing random numbers between 1 and 9
# import random

# number = random.randint(1, 10)
# print(number)

#to shuffle cards... NB:This works best with for loops
# import random

# cards = ["jack","queen","king"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

numbers = list(range(1, 10))  # Create list [1, 2, 3, ..., 9]

# For each pass, print the current list and then remove the last element
for i in range(len(numbers)):
    # Print current list
    for num in numbers:
        print(num, end=' ')
    print()
    
    # Remove last element for next iteration
    numbers.pop()  # Remove the last element




