#global scope causes an error and a local scope is accepted
name = "Nat"
count = 1

def greeting(firstname):
    color = "blue"
    print(color)
    print(name)
    print(count)

greeting("Nat")

def another():
    color ="blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Nat")

another()
