# The Goal: Build a script that manages your 2027-2028 travel schedule, audits your medical expenses, and checks your vehicle status—all in one file using everything from zip() to list comprehensions.

# Part 1: The Business Schedule (Zip & Match)
# Data: Create a list of three trips: "Reunion Cruise", "Jamaica", and "North Carolina Move"
# Data: Create a list of three dates: "February 2027", "December 2027", and "2029-2031"
# Action: Use zip() to pair them
# Action: Loop through the zipped list. Inside the loop, use a match statement
# If the trip is "Japan", print "Error: Japan trip was canceled."
# Otherwise, print "Destination: [Trip] | Target: [Date]"


# Part 2: The Medical Audit (2D Lists & Comprehensions)
# Data: Create a 2D list called er_bill_data where each sub-list is ["Service Name", Cost]
# Include at least 4 items (e.g., ["IV", 500], ["Consultation", 1200], ["Lab", 80], ["Bandage", 20]).
# Action: Use a List Comprehension to create a new list high_cost_audit
# Only include the names of the services that cost more than $100.
# Action: Print: "High priority items to review in late March: [list]"


# Part 3: The Suburban Health Scan (While Loops & Breaks)
# Data: Set a variable fuel_level = 100
# Action: Write a while loop that runs as long as fuel_level > 0
# In each "cycle" of the loop, subtract 20 from the fuel level
# Print "Current Fuel: [level]%"
# Logic: If the level hits 20%, print "Low Fuel Warning! Stopping scan." and break the loop
