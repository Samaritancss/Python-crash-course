# Python reading files(.txt, .json, .csv)

#FOR TEXT

# file_path = "C:/Users/hp/OneDrive/Desktop/output.txt"

# try:

#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read this file")

#FOR JSON

# import json

# file_path = "C:/Users/hp/OneDrive/Desktop/output.json"

# try:

#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read this file")

#FOR CSV

# import csv

# file_path = "C:/Users/hp/OneDrive/Desktop/output.csv"

# try:

#     with open(file_path, "r") as file:
#         content = csv.reader(file)
#         for line in content:
#             print(line)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read this file")

###############another method##########
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line)

######to sort it out
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
#to resverse
for name in sorted(names):
#for name in sorted(names, reverse= True):
    print(f"hello, {name}")


