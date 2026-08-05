#keyword arguments = an argument preceded by an identifier
# helps with readability
# order of arguments doesn't matter 
# 1. positional 2. default 3. keyword 4. arbitrary

# def hello(greetings, title, first, last):
#     print(f"{greetings} {title} {first} {last}")

# hello(greetings="Hello", first="Nat", last="Amartey",title="Mr",)

# print("1", "2", "3", "4", "5", sep="-")

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=1, area=123, first=456, last=7890)

# print(phone_num)

#ARBITRARY

#*args = allows you to pass multiple non-key arguments
#**kwargs = allows you to pass multiple keyword-arguments
# * unpacking operator

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.","Spongebob","Harold","Squarepants","III")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")

# print_address(street="123 Fake St.",
#               apt = "100",
#               city = "Detroit",
#               state = "MI",
#               zip = "54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")


shipping_label("Dr.", "Spongebob","Squarepants",
              street ="123 Fake St.",
              apt = "100",
              city = "Detroit",
              state = "MI",
              zip = "54321")


