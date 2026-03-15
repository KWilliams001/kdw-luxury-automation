# Bucket 1: The KDW Luxury Travels Suite (Days 8-10)
# Focus: Multiple Returns and Professional Formatting

# Project 1 (Multiple Returns):
# Create get_commission_split(total_fare).
# Return three values: the agent's cut (15%), the house cut (5%), and the remaining balance.
def get_commission_split(total_fare):
    agent_cut = .15 * total_fare
    agent = f"The Agent will get {agent_cut}% of {total_fare}"
    before_house = total_fare - agent_cut
    house_cut = .05 * total_fare
    house = f"The House will get {house_cut}% of {total_fare}"
    remaining_balance = total_fare - house_cut - agent_cut
    balance = f"The remaining balance after those cuts are {remaining_balance}"
    return agent, house, balance


# Project 2 (Scope):
# Define a global variable AGENCY_ID = "KDW-777".
# Create a function that prints a "Ticket" using that global ID and a local passenger_name.
AGENCY_ID = "KDW-777"


def trip(local_name):
    return f"Ticket for {local_name}, Global ID: {AGENCY_ID} "


# Project 3 (Lambda/Map):
# You have a list of travel prices: [1200, 2500, 800].
# Use a lambda inside a map() to add a flat $50 "Booking Fee" to each price.
prices = [1200, 2500, 800]
final_prices = map(lambda x: x + 50, prices)
print(list(final_prices))
