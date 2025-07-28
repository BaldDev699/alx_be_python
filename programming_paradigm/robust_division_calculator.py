# This script defines a function that performs division with error handling for zero division and non-numeric inputs.

# Function to safely divide two numbers with error handling
def safe_divide(numerator, denominator):
    try:
        num = float(numerator) # Convert numerator to float
        denom = float(denominator) # Convert denominator to float
        result = num / denom # Perform division
        return f"Result: {result}" # Return the result as a formatted string
    # Handle division by zero
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    # Handle non-numeric inputs
    except ValueError:
        return "Error: Both inputs must be numeric."