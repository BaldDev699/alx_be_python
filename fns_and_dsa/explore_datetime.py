# Script to explore datetime functionalities in Python

from datetime import datetime, date, timedelta # importing necessary modules

# Function to display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S")) # displaying current date and time in a formatted way
display_current_datetime()

# Function to display the current time
def calculate_future_date(days):
    today = date.today()
    future_date = today + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d")) # displaying future date based on user input
try:
    user_input = int(input("Enter the number of days to add to the current date: ")) # taking user input
    calculate_future_date(user_input) # calculating future date based on user input
except ValueError:
    print("Invalid input. Please enter a valid number.") # handling invalid input