# Project 1: The SunCu Savings "Shore" Forecast
# Use input() to ask for your current balance in your SunCu Shore Savings account and your monthly contribution. Use math operators to calculate how much you will have by the February 2027 Reunion Cruise (roughly 11 months from now) [cite: 2026-01-22, 2026-03-01].
#
# Goal: Practice int() or float() conversion with user input and basic multiplication.

current_balance = input(" What is your current balance in your Shore Savings Account? ")
print(f"${current_balance}")
monthly_contribution = input("How much are you putting into it each month? ")
print(f"${monthly_contribution}")

reunion_cruise = float(current_balance) + (float(monthly_contribution) * 11)
print(f"After 11mo, you will have ${round(reunion_cruise, 2)}")
