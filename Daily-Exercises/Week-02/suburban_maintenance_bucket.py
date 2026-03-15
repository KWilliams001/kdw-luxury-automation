# Bucket 3: The Suburban Maintenance Suite (Days 8-10)
# Focus: Advanced Logic and Quick Checks


# Project 7 (Multiple Returns):
# Create check_engine_status(fuel, oil_life).
# Return two strings: one for fuel status (using your threshold logic) and one for oil status.
def check_engine_status(fuel, oil_life):
    fuel_status = fuel
    oil_status = oil_life
    return fuel_status, oil_status


# Project 8 (Lambda):
# Even though you prefer regular functions, try this:
# Create a lambda called is_diesel that takes a string and returns True if it contains the word "Duramax"
is_diesel = lambda x: "Duramax" in x


# Project 9 (Culmination):
# Create a list of 3 "Alerts".
# Use map() and a function to wrap each alert in asterisks (e.g., *** OIL LOW ***) for a dashboard display.
alert_list = ["yellow", "red", "black"]


def wrap_alert(color):
    return f"*** {color.upper()} ALERT ***"


dashboard = list(map(wrap_alert, alert_list))
print(dashboard)
