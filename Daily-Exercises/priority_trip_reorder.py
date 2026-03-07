# Project 1: The Priority Trip Reorder
# Use your planned_trips list from yesterday [cite: 2026-03-01].

# Task: Use .insert() to put "Passport Renewal" at the very beginning of the list [cite: 2026-03-02].
# Task: Use .pop() to remove the last item you added (the NC move) and save it into a variable called long_term_goal [cite: 2026-02-04, 2026-03-02].

planned_trips = ["Reunion Cruise", "Japan", "Jamaica", "NC Move"]
planned_trips.insert(0, "Passport Renewal")
print(planned_trips)

long_term_goal = planned_trips.pop(-1)
print(long_term_goal)
