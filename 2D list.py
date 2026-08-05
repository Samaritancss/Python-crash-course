groceries = [("apple","orange","banana","coconut"),
             ("celery","carrots", "potatoes"),
             ("chicken", "fish","turkey")]


#print(groceries[0][1])
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

#2D keypad
num_pad = [(1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#")]

for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()
