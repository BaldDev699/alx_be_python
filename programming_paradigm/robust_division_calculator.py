# This script defines a function that performs division with error handling for zero division and non-numeric inputs.

# Function to safely divide two numbers with error handling
def safe_divide(numerator, denominator):
    try:
        num = float(numerator) # Convert numerator to float
        denom = float(denominator) # Convert denominator to float
        result = num / denom # Perform division
        print(f"The result of the division is: {result}") # Return the result
    # Handle division by zero
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    # Handle non-numeric inputs
    except ValueError:
        return "Error: Please enter numeric values only."