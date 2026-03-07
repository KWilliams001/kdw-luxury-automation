# Project 1: The KDW Destination Zipper
# Use zip() to pair your trips with their specific years
# Task:
# Create trips = ["Reunion Cruise", "Jamaica", "NC Move"]
# Create years = [2027, 2027, 2029]
# Use zip() to combine them and convert it to a list
# Print: "KDW 2027-2029 Schedule: [your zipped list]"

trips = ["Reunion Cruise", "Jamaica", "NC Move"]
years = [2027, 2027, 2029]

trips_and_years = zip(trips, years)
print(f"KDW 2027-2029 Schedule: {list(trips_and_years)}")
