# Project 1: The Multi-Destination Specialist (KDW Luxury Travels)
# Goal: Use multiple parameters and default values to create a more powerful travel itinerary tool
# Task: Define a function create_itinerary that takes three parameters:
# client_name
# destination
# duration (give duration a default value of 7)
# The logic: Print a message like: "Booking a {duration} day trip to {destination} for {client_name}."
# The Call: Call it once using only positional arguments for Auntie and Jamaica, letting the duration stay at 7.
# Call it a second time for your Japan trip using a keyword argument to change the duration to 14

def create_itinerary(client_name, destination, duration = 7):
    print(f"Booking a {duration} day trip to {destination} for {client_name}.")


create_itinerary("Auntie", "Jamaica")
create_itinerary(duration=14, client_name="Auntie", destination="Jamaica")
