# Phase 1: The zip() and for Loop Refactor
# In your original code, you used a while loop and an index to pull data out of your zipped list
# While that works, it's like using a manual screwdriver when you have a power drill available
# The Goal: Unpack the trip and the date directly in the loop header
trips = ["Reunion Cruise", "Jamaica", "North Carolina Move"]
dates = ["February 2027", "December 2027", "2029-2031"]

# The "Pro" way: No index, no len(), just direct access.
for trip, date in zip(trips, dates):
    match trip:
        case "Japan":
            print("Error: Japan trip has been canceled.")
        case _:
            print(f"Destination: {trip} | Target: {date}")


# Why this is better:
#   Readability: Anyone can see exactly what trip and date represent immediately
#   Safety: You can't accidentally create an "infinite loop" because you forgot to add index += 1


# answer this question:
account_nam = ["Sail Checking", "Shore Savings", "Dog Grooming Fund"]
current_bal = [1200, 3500, 80]
monthly_tar = [1000, 5000, 100]

# Use a for loop and zip() to combine all three lists at once.
# Goal: Print a report for each account.
# Format: "Account: [Name] | Balance: $[Current] | Goal: $[Target]".
# Pro Tip: zip() can take as many lists as you want! Just comma-separate them: zip(list1, list2, list3).


for name, bal, goal in zip(account_nam, current_bal, monthly_tar):
    print(f"Account: {name} | Balance: ${bal} | Goal: ${goal}")

# Task 2: The "Savings Gap" Comprehension
# Now, use a List Comprehension to find out which accounts are below their monthly target.
# The Logic: Create a new list called underfunded_accounts.
# The Filter: Only include the account name if the current_balance is less than the monthly_target.
# The Result: Print the list of accounts that need more savings this month.
# We name the three pieces of the tuple: name, bal, and goal
underfunded_accounts = [name for name, bal, goal in zip(account_nam, current_bal, monthly_tar) if bal < goal]

print(f"Accounts needing more savings: {underfunded_accounts}")
print(underfunded_accounts)
