# Project 2: The Suburban "Fuel & Range" Calculator
# Your Chevrolet Suburban has a 3.0L Duramax Diesel engine [cite: 2026-02-06]. Create a script that asks for the current price of diesel and the size of the tank (approx. 24 gallons). Calculate:
#
# The total cost to fill the tank.
#
# How many full tanks you can afford with a set "Monthly Maintenance" budget of $500.
#
# Goal: Practice plus equals logic and modulo (to see if there is a "remainder" of cash left over).

current_diesel_price = float(input("How much does diesel cost at Wawa today: $"))
tank_size = int(input("How many gallons can the tank hold? "))

total_cost = 0
total_cost += current_diesel_price * tank_size
print(total_cost)

monthly_budget = 500
full_tank = monthly_budget / total_cost
print(int(full_tank))
leftover_funds = monthly_budget % total_cost
print(leftover_funds)

print(f"With a monthly budget of ${monthly_budget}, you will be able to fill up your tank {int(full_tank)} times each month and have ${round(leftover_funds, 2)} funds")
