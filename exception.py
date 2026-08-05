# exception = An event that interrupts the flow of a program
# (zerodivisionError, TypeError, ValueError)
# 1. try, 2. except 3. finally

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero ")
except ValueError:
    print("Enter only number please!")


# try:
#     number = int(input("Enter a number: "))
#     print(1 / number)
# except Exception:
#     print("Something went wrong!")

try:
    raise Exception("I'm a custom exception")
