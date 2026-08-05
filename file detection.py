# python file detection

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
        
else:
    print("That location doesn't exist")

