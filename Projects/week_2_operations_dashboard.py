# The Week 2 Milestone: "The KDW Operations Dashboard"
# The Scenario: You need a single script that can process a batch of data for your business, your vehicle, and your savings all at once.

# Phase 1: The Global Registry
# At the top of your script, define three Global Variables:
# BUSINESS_NAME = "KDW Luxury Travels"
# CURRENT_SAVINGS = 3500
# VEHICLE_STATUS = "Ready"
BUSINESS_NAME = "KDW Luxury Travels"
CURRENT_SAVINGS = 3500
VEHICLE_STATUS = "Ready"


# Phase 2: The Logic Engines (Functions)
# Create three distinct functions that use your new skills:

# The Trip Processor (Multiple Returns):
# Create a function process_trip(base_price) that returns:
# The total price (base + $50 fee)
# The commission (15% of total)
# A formatted string: "KDW-BOOKING: {base_price}"
def process_trip(base_price):
    total_price = base_price + 50
    commission = total_price * .15
    booking = f"KDW-BOOKING: ${base_price}"
    return total_price, commission, booking


# The Savings Updater (Global Scope):
# Create a function add_income(amount).
# Use the global keyword to update CURRENT_SAVINGS.
# Return the new total balance.
def add_income(amount):
    global CURRENT_SAVINGS
    CURRENT_SAVINGS += amount
    return CURRENT_SAVINGS


# The Alert System (Mapping):
# Create a function format_alert(message).
# It should return the message in all caps with a prefix: "[SYSTEM ALERT]: {MESSAGE}".
def format_alert(message):
    return f"[SYSTEM ALERT]: {message.upper()}"


# Phase 3: The Execution (The "Master Run")
# Write the code that actually runs the dashboard:
# Create a list of 3 trip prices: [1200, 4500, 900].
# Use map() with your process_trip function to create a new list of "Trip Summaries."
# Update your savings by adding a $500 commission using your add_income function.
# Print a final report that shows your BUSINESS_NAME, your new CURRENT_SAVINGS, and the list of processed trips.
trip_prices = [1200, 4500, 900]
trip_summaries = list(map(process_trip, trip_prices))
add_income(500)
print(f"--- {BUSINESS_NAME} DASHBOARD ---")
print(f"Current Balance: ${CURRENT_SAVINGS}")
print(f"Processed Trips: {trip_summaries}")
