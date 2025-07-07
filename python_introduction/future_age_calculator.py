# This script calculates the user's age in a future year.

current_age = int(input("How old are you? ")) # Get the user's age
current_year = 2023 # Current year
future_year = 2050 # Year to calculate future age
# Calculate future age
age = current_age + (future_year - current_year)
# Print the result
print(f"In {future_year}, you will be {age} years old.")