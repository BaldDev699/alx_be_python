# This script draws a square pattern of asterisks based on user input for the size.

size_pattern = int(input("Enter the size of the pattern: ")) # Input for the size of the pattern
row = 0 # Initialize row counter

while row < size_pattern: # Loop until the number of rows equals the size
    for col in range(size_pattern):
        print("*", end="") # Print asterisks in the same row
    print() # Move to the next line after printing a row
    row += 1 # Increment the row counter after completing a row