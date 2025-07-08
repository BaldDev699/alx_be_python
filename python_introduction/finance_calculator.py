# This script gets the user's monthly income and monthly expenses, and calculates projects savings for the year.

monthly_income = float(input("Enter your monthly income: ")) # Get the user's monthly income
monthly_expenses = float(input("Enter your monthly expenses: ")) # Get the user's monthly expenses
monthly_savings = monthly_income - monthly_expenses # Calculate monthly savings
interest_rate = 0.05 # Interest rate of 5%
projected_savings = monthly_savings * 12 + (monthly_savings * interest_rate) # Calculate projected savings for the year
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}") # Print the projected savings