#!/usr/bin/env python3

# import sys module
import sys

print(len(sys.argv))

# check if system argument was provided
if len(sys.argv) == 1:
    my_name = "Guest" # if no argument was provided use "guest"
else:
    my_name = sys.argv[1] #"Josiah"


# asign variable values
my_color = "Green"
my_activity = "Night Disc"
my_animal = "Octopus"
my_number = 5

# print output
print(
f"""My name: {my_name}
My favorite color: {my_color}
My favorite activity: {my_activity}
My favorite animal: {my_animal}
My Favorite number: {my_number}"""
)

# print('"my_name"')
# print('my_name')
# print(my_name + " " + my_color)

