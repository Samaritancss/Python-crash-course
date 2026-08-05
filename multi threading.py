# multithreading = Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like reading files or fetching data from APIs
# threading.Thread(target= my_function)

import threading
import time

def walk_cat(first):
    time.sleep(6)
    print(f"You Finish walking {first}")

def take_out_box():
    time.sleep(3)
    print("You take the box out")

def get_mail():
    time.sleep(2)
    print("You get the mail")

# walk_cat()
# take_out_box()
# get_mail()

#in accordance with time
chore1 = threading.Thread(target=walk_cat, args=("Chelsea",))
chore1.start()

chore2 = threading.Thread(target=take_out_box)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()


print("All chores are complete!")
