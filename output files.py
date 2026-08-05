# Python writing files (.txt, .json, .csv)

#FOR TXT
#txt_data ="I like jollof"

#relative method
#file_path = "output.txt"

#absolute method
# file_path = "C:/Users/hp/OneDrive/Desktop/output.txt"

# to write
# try:
#     with open(file_path, "w") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


#TO APPEND
# try:
#     with open(file_path, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

# for loops
#employees = ["Hassan","Fathi","Gamel","Nuredeen"]
# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

# import json
#FOR JSON
# employee = {
#     "name": "Nathaniel"
#     "age": 29,
#     "job": "engineer"
# }

# for json
# file_path = "C:/Users/hp/OneDrive/Desktop/output.json"

#json

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=3)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

#FOR .CSV

# import csv

# employees = [["Name","Age","Job"],
#             ["Nathaniel", 29, "Engineer"],
#             ["Lois", 26, "Unemployed"],
#             ["Cindy", 28, "Dentist"]]

# file_path = "C:/Users/hp/OneDrive/Desktop/output.csv"

# try:
#     with open(file_path, "w", newline = "") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


######### ANOTHER METHOD ############
#to write in text for output
# name = input("What's your name? ")

# file = open("names.txt", "w")
# file.write(name)
# file.close()

#to append in text for output 
# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

#read files
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")




