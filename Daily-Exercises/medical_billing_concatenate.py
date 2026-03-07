# Project 3: The Medical Billing Concatenation
# Prepare for your late March ER bill audit. [cite: 2026-02-05]
#
# Task:
# Create a list hospital_charges = ["IV Drip", "Medication"].
# Create a second list admin_fees = ["Room Fee", "Lab Work"].
# Concatenate (combine) them into a single list named total_bill_items.
# Use len() to print how many total items you need to review.

hospital_charges = ["IV Drip", "Medication"]
admin_fees = ["Room Fee", "Lab Work"]

total_bill_items = hospital_charges + admin_fees
print(total_bill_items)

print(len(total_bill_items))
