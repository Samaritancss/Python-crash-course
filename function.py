#function = A block of reusable code
#place () after the function name to invoke it

# def happy_birthday():
#     print("happy birthday to you!")
#     print("How old are you now?")
#     print("Happy birthday to you!")
#     print()

# happy_birthday()
# happy_birthday()
# happy_birthday()

# def happy_birthday(name,age):
#     print(f"happy birthday to {name}!")
#     print(f"You are {age} years old")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("nat", 29)

#function to display an invoice

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Nat", 33.50, "01/02/2026")
    

#return = statement used to end a function 
# and send a result back to the caller

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("nathaniel", "amartey")

print(full_name)

#new function

def hello():
    print("Hello world!")

hello()

def sum(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum("h",5)
print(total)

#working with args mostly works like a tuple
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Nat","John","Pat")

#working with keyword arguments mostly works like a dictionary
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first= "Nat", last= "Kill")

#while loops
#zero is considered to be false

value = "y"
count = 0

while value:
    count += 1
    if (count == 5):
        break
    else:
        value = 0
        continue


