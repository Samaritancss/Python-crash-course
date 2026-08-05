#logical operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be true
#                    and = both conditions must be true
#                    not = inverts the conditions (not false, not true)

#using the "or" operator both conditions should not be  necessary true

#setting up conditions for an event

# temp = 25
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")


#"and" with this operator both conditions must be true

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <= 0  and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is warm outside ")
    print("It is sunny")  
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is cloudy")
elif temp <= 0  and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It is warm outside ")
    print("It is cloudy")



