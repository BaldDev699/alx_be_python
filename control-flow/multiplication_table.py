# This script generates a multiplication table for a given number

number = int(input("Enter a number to see its multiplication table: ")) # Input from the user

for i in range(1, 11):  # Loop from 1 to 10
    number * i  # Calculate the product
    print(f"{number} x {i} = {number * i}")  # Print the multiplication result