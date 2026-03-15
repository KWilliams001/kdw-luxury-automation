# Bucket 2: The SunCu Financial Suite (Days 8-10)
# Focus: Data Transformation and Calculations

# Project 4 (Multiple Returns):
# Create audit_savings(target, current).
# Return the amount_saved and the percentage_complete (e.g., (current/target) * 100).
def audit_savings(target, current):
    amount_saved = current
    percentage_complete = (amount_saved / target) * 100
    return amount_saved, percentage_complete


# Project 5 (Scope/Variable Access):
# Create a function that tries to update a global TOTAL_ASSETS variable.
# Use the global keyword to make sure the change sticks.
TOTAL_ASSETS = "variable"


def change_global(asset):
    global TOTAL_ASSETS  # This tells Python: "Reach outside the function"
    TOTAL_ASSETS = asset
    return TOTAL_ASSETS


print(change_global("not a variable"))

# Project 6 (Map):
# You have a list of monthly expenses: [80, 120, 45, 200].
# Use map() with a function that rounds each expense to the nearest $10.
monthly_expenses = [80, 120, 45, 200]


def round_up(expense):
    return expense + 10 if expense > 70 else expense + 5


rounded_expense = list(map(round_up, monthly_expenses))
