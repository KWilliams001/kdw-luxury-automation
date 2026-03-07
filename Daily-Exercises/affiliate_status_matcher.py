# Project 1: The Affiliate Status Matcher
# Instead of just numbers, let’s categorize affiliates by their "Tier."
# Task: Create a variable affiliate_tier. Use a match statement to check its value.

# Logic:
# case "Gold": Print "High-priority partner; 15% commission."
# case "Silver": Print "Standard partner; 10% commission."
# case "Bronze": Print "Trial partner; 5% commission."
# case _: (The "wildcard"): Print "Tier not recognized; contact support."
# Goal: Master the syntax of match and case.

affiliate_tier = ""

match affiliate_tier:
    case "Gold":
        print("High-priority partner; 15% commission.")
    case "Silver":
        print("Standard partner; 10% commission.")
    case "Bronze":
        print("Trial partner; 5% commission.")
    case _:
        print("Tier not recognized; contact support.")
