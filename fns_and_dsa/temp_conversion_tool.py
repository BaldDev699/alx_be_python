# Script to convert temperatures between Celsius and Fahrenheit

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 # Conversion factor from Celsius to Fahrenheit

def convert_to_celcius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temperature = input("Enter the temperature to convert: ")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F) ").strip().upper()

    try:
        temperature = float(temperature)
    except ValueError:
        print("Invalid temperature input. Please enter a numeric value.")

    if unit == "C":
        converted = convert_to_fahrenheit(float(temperature))
        print(f"{temperature}°C is {converted:.2f}°F")
    elif unit == "F":
        converted = convert_to_celcius(float(temperature))
        print(f"{temperature}°F is {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

if __name__ == "__main__":
    main()
