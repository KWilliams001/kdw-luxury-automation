# Project 3: The Medical Bill "Tax" Comprehension
# Automate the math for your late March ER bill audit
# Task:
# Create a list raw_prices = [500, 1200, 75, 250]
# Use a List Comprehension to create a new list prices_with_tax that multiplies each price by 1.07
# Bonus Conditional: Only include items in the new list if the price is greater than $100

raw_prices = [500, 1200, 75, 250]
prices_with_tax = [price * 1.07 for price in raw_prices]
print(prices_with_tax)

prices_with_tax_conditional = [price for price in prices_with_tax if price > 100]
print(prices_with_tax_conditional)
