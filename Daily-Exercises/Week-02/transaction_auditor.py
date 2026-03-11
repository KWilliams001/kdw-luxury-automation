# Project 3: The Transaction Auditor (SunCu Banking)
# Goal: Use positional and keyword arguments to audit specific transactions
# Task: Define a function audit_transaction that takes account_type, amount, and category
# The Logic: Print: "Auditing {account_type} account: ${amount} spent on {category}."
# The Call: Call this using positional arguments for your Shore Savings account
# Then, call it again for your dog grooming payment of $80 using keyword arguments in a different order than you defined them

def audit_transaction(account_type, amount, category):
    print(f"Auditing {account_type} account: ${amount} spent on {category}.")


audit_transaction("Shore Savings Account", 80, "Dog Grooming")
audit_transaction(amount=80, category="Dog Grooming", account_type="Shore Savings Account")
