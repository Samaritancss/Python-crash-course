# dictionary = {'name':'nat', 'age':12, 'size':'small'}
# dictionary['hair'] = 'brown'
# print(dictionary)

# new_message = '''
#              this is 
#              a comment
#              on multiple line
#              '''
# print(new_message)
# attendance = 'bob,sue,tin,pan,tin'
# attendance = attendance.split('.')
# print(attendance)

# student = ['bob','tin','phil','nat']
# for name in student:
#     print(f"hello {name}")

# teen = 11
# adult = 18
# retired = 65

# while True:
#     age = input("Enter your age:")
#     age = int(age)

#     if age < teen:
#         print("You are a kid")
#     elif age >= 11 and age < 18:
#         print("You're an teenager")
#     elif age >= 18 and age < retired:
#         print("You're an adult")
#     else:
#         print("You're old and retired")

    
# password = "open potato"

# while True:
#     phrase = input("Enter your password:")

#     if password in phrase.lower():
#         print("You are right!!!")
#         break
#     else:
#         print("You are wrong. Try again")


# from random import randint

# number = randint(1,10)

# while True:
#     guess = input("Enter your guess:")
#     guess = int(guess)

#     if guess > number:
#         print(f"The {guess} is too high")
#     elif guess < number:
#         print(f"{guess} is too low")
#     else:
#         print(f"{guess} is right")
#         break

# owed = float(input("Enter the staring loan:"))
# payment = float(input("Enter monthly payment: "))
# interest = float(input("Enter yearly interest: "))

# interest_monthly = (interest / 12 ) / 100
# month = 0

# while owed >= 0:
#     print(owed)
#     owed = owed - payment
#     owed = owed + (owed + interest_monthly)
#     month += 1

# print(f"Months to pay off = {month}")

import requests

url = 'http://ip-api.com/json/'

response = requests.get(url).json()

# print(response)
print(f"You are in this city: {response['city']}")

for key, value in response.items():
    print(f"{key} --{value}")





 