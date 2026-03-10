# Project 2: The Fuel Range Finder (Suburban Maintenance)
# Goal: Create a function to help you decide if you need to stop for diesel
# Task: Define a function check_fuel_range that takes one parameter: miles_lef.
# Logic: If miles_left is less than 50, return "Time to find a station!". Otherwise, return "You're good to go!"
# The Call: Call the function with 35 and print the result
miles_left = 35
def check_fuel_range(miles_left):
    if miles_left < 50:
        print("Time to find a station!")
    else:
        print("You're good to go!")


check_fuel_range(miles_left)
