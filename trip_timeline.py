# Project 1: The 2027-2028 Trip Timeline
# Create a list named planned_trips. [cite: 2026-02-04]
#
# Task:
# Initialize the list with: "Reunion Cruise", "Japan", and "Jamaica".
# Since the Japan trip was canceled, use .remove() to take it off the list.#
# Use .append() to add "North Carolina Move" to the end.#
# Print the final list and use a negative index to print only the most recent addition.

planned_trips = ["Reunion Cruise", "Japan", "Jamaica"]
planned_trips.remove("Japan")
planned_trips.append("North Carolina Move")
print(planned_trips)
print(planned_trips[-1])
