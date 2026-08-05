#dictionary = a collection of {key: value} pairs
#ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            "India": "New Delhi",
            "China":"Beijing",
            "Russia": "Moscow"}
#another method
capitals = dict(USA = "Washington D.C", India ="New Delhi", China = "Beijing", Russia ="Moscow")
print(capitals)

# print(capitals.get("China"))

# if capitals.get("Ghana"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"Russia":"sochi"})
# capitals.pop("China")
#capitals.popitem()....removes latest key item
#capitals.clear()

#keys = capitals.keys()

# for key in capitals.keys():
#     print(keys)
   
# values = capitals.values()
# for value in capitals.values():
#      print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")

#nested dictionaries

member1 = {
    "name" : "Plant",
    "instrument" : "vocals"
}
member2 = {
    "name" : "Page",
    "instrument" : "guitar"
}
band = {
    "member1" : member1,
    "member2": member2
}
print(band)

#sets
nums = {1,2,3,4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))


#No duplicates allowed(notice sets dont allow duplicates)
nums = {1,2,2,3}
print(nums)

#true is a dupe of 1. False is a dupe of zero

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#check if a value is in a set
print(2 in nums)

#but you cannot refer to an element in the set with an index position or a key

#add a new element to a set
nums.add(8)
print(nums)

#add elements form one set to another

more_nums = {5,6,7}
nums.update(more_nums)
print(nums)

#you can use update with lists, tuples, and dictionaries, too.

#Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}

my_new_set = one.union(two)
print(my_new_set)

one.intersection_update(two)
print(one)

one.symmetric_difference_update(two)
print(one)




