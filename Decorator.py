#  Decorator = A function that extends the behavior of another function
#  w/o modifying the base function
#  Pass the base function as an argument to the decorator

#    @add_sprinkles
#    get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles🎊*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge🍫*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream🍨")

get_ice_cream("strawberry")
