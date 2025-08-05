# Script to demonstrate class static methods and class methods in Python

# Calculator class with static and class methods
class Calculator:
    calculation_type = "Arithmetic Operations" # Class variable to indicate the type of calculations

    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b
    
    # Class method to multiply two numbers
    @classmethod
    def multiply(cls, a, b): 
        print(f"Calculation type: {cls.calculation_type}")
        return a * b