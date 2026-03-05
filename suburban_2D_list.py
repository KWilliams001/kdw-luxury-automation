# Project 2: The Suburban Trim & Package 2D List
# Organize your Chevrolet Suburban data into a 2D list (a list of lists). [cite: 2026-02-06]
#
# Task:
# Create a list where each sub-list is ["Trim Name", "Engine", "Has Luxury Package"].
# Include your specific setup: ["LT", "3.0L Duramax", True].
# Add a second sub-list for a base model: ["LS", "5.3L V8", False].
# Modify the 2D list: change the "LT" engine to "3.0L Duramax Diesel" to be more specific.

suburban_data = [["Trim Name", "Engine", "Has Luxury Package"], ["LT", "3.0L Duramax", True], ["LS", "5.3L V8", False]]

suburban_data[1][1] = "3.0L Duramax Diesel"
print(suburban_data)
