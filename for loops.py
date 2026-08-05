#for loops = execute a block of code a fixed of times.
#you can iterate over a range, string, sequence, etc.


# for x in reversed(range(1, 21)):
#     if x == 13:
#         continue
#     else:
#         print(x)

#countdown timer in for loops
# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in reversed(range(0, my_time)):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")

#     time.sleep(1)

# print("TIME'S UP!")


#loops
# value = 1
# while value < 10:
#     print(value)
#     value += 1

#to break at a point
# value = 1
# while value < 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

#to continue
# (remember the position of the print value determines the starting number and where it ends also take note of the operation used)

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# names = ["Nat", "Pat", "John"]
# for name in names:
#     print(name)

#because break will print all members of the list before the one assigned to 
# for name in names:
#     if name == "Pat":
#         break
#     print(name)
# #continue
# for name in names:
#     if name == "Pat":
#         continue
#     print(name)


#range
# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)

# for x in range(0, 100, 10):
#     print(x)
# else:
#     print("Glad that\'s over")

names = ["Nat", "Dad","Kelly"]
actions = ["play","eat","sleep"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")       


for action in actions:
    for name in names:
        print(name + " " + action + ".")

