# Project 3: The Savings Goal Calculator (SunCu Banking)
# Goal: Create a function that calculates how much more you need to save for a trip
# Task: Define a function calc_savings_gap with two parameters: target and current.
# Logic: Subtract current from target and return the difference
# The Call: Call the function using your Shore Savings target (5000) and current balance (3500) from your review earlier
target = 5000
current = 3500
def calc_savings_gap(target, current):
    target_minus_current = target - current
    print(f"You are ${target_minus_current} from reaching your goal")


calc_savings_gap(target, current)
