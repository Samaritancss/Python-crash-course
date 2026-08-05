# #string functions

# #name = input("Enter your full name: ")

# phone_number = input("Enter your phone number: ")

# #result = len(name)
# #result = name.find("o")
# #result = name.rfind("q")
# #name = name.capitalize()
# #name = name.upper()
# #name = name.lower()
# #result = name.isdigit()
# #result = name.isalpha()
# #result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")

# print(phone_number)


user_name = input("Enter your user_name: ")

if len(user_name) > 12:
    print("Your username cannot be more than 12 characters ")
elif not user_name.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not user_name.isalpha():
    print("Your username cannot contain numbers")
else:
    print(f"Welcome {user_name}!")
    


