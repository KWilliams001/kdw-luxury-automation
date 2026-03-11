# Project 4: The Strategic Saver (SunCu & Grooming)
# Goal: Use a function to calculate a value and then return it so you can use that result in a second calculation
# The Task: 1. Define a function get_savings_gap(target, current).
# 2. Inside the function, return the difference (target - current).
# 3. Outside the function, call it with your Shore Savings target ($5,000) and current balance ($3,500)
# 4. Save that returned value into a variable called remaining.
# 5. Finally, calculate how many dog grooming payments ($80) it would take to cover that gap and print the result

def get_savings_gap(target, current):
    return target - current


remaining = get_savings_gap(5000, 3500)
dog_groom_payments = remaining / 80
print(dog_groom_payments)
