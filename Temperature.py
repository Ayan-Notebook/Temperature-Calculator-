def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature(value, unit):
    if unit == 'C':
        celsius = value
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif unit == 'F':
        fahrenheit = value
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif unit == 'K':
        kelvin = value
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        raise ValueError("Invalid unit. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

    return celsius, fahrenheit, kelvin

def main():
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C/F/K): ").strip().upper()

    try:
        celsius, fahrenheit, kelvin = convert_temperature(value, unit)
        print(f"\nTemperature conversions for {value} {unit}:")
        print(f"Celsius: {celsius:.2f} C")
        print(f"Fahrenheit: {fahrenheit:.2f} F")
        print(f"Kelvin: {kelvin:.2f} K")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
