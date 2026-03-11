# Project 2: The Maintenance Threshold (Chevrolet Suburban)
# Goal: Use a default parameter to optimize how you check your vehicle's status
# Task: Refactor your check_fuel_range function to take two parameters:
# miles_left
# threshold (set the default threshold to 50)
# The Logic: If miles_left is less than threshold, print "Alert: Low Fuel!". Otherwise, print "Range is acceptable."
# The Call: Call the function with miles_left=60 and use a keyword argument to set a stricter threshold=75 for a long trip

def check_fuel_range(miles_left, threshold=50):
    if miles_left < threshold:
        print("Alert: Low Fuel!")
    else:
        print("Range is acceptable")


check_fuel_range(60, threshold=75)
