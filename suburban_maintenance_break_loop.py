# Project 2: The Suburban Maintenance "Break" Loop
# Simulate a diagnostic check on your Chevrolet Suburban
# Task:
# Create a list engine_codes = ["P0101", "P0300", "SERVICE", "P0420"]
# Write a for loop to iterate through the codes
# If the code is "SERVICE", print "Critical error found. Stopping scan." and use break to exit the loop
# Otherwise, print "Checking code: [code]... OK"

engine_codes = ["P0101", "P0300", "SERVICE", "P0420"]
for codes in engine_codes:
    if codes == "SERVICE":
        print("Critical error found. Stopping scan")
        break
    print(f"Checking code: {codes}... OK")
