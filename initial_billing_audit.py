# Project 3: The "Duplicate Service" Flag (Mental Challenge Solution)
# Since you'll be auditing that ER bill in late March, let’s build a basic version of the morning challenge using Concatenation and Strings [cite: 2026-02-05].
#
# Create two variables representing two different charges (e.g., charge_1 = "IV Drip" and charge_2 = "IV Drip").
#
# Create a third variable that combines them into a "Audit Report" string.
#
# Goal: Use a multi-line string to print a "Professional Audit Summary" for KDW Luxury Travels [cite: 2026-03-01].


charge1 = "IV Drip"
charge2 = "Medication"
charges = charge1 + ", " + charge2
total_cost = 0
print(f"""Professional Audit Summary:
{charges}
{total_cost}
""")
