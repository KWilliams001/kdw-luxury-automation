# Project 2: The Suburban Maintenance Alert
# Task: Use your if/else logic with the or operator.
# Logic: If mileage > 7500 or months_since_service > 6, alert the user for a 3.0L Duramax service check

mileage = 90000
months_since_service = 3

if mileage > 7500 or months_since_service > 6:
    print("You need to do a service check on that diesel engine!")
else:
    print("That engine might be good to use")
