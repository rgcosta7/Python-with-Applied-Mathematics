'''
Name: Raul Costa
Date: 11/10/2021
EC148003 Software Development with Applied Mathematics with Python
Moodle Version

Problem:
Classic conversion from Celsius to Fahrenheit and Kelvin.

Remember to remove the TODO tag when you complete a task.


Examples of the exact output this program should produce:

Convert from °Celsius to °Fahrenheit and Kelvin
Please enter the temperature in Celsius: 232.778
232.78 °C is equal to 451.00 °F or 505.93 K

Convert from °Celsius to °Fahrenheit and Kelvin
Please enter the temperature in Celsius: -273.15
-273.15 °C is equal to -459.67 °F or 0.00 K

'''

# alt+0176 (numpad) = °
print('Conversion from °Celsius to °Fahrenheit and Kelvin:')
temp = float(input("Please enter the temperature to convert in Celsius: "))

fahrenheit = (temp * 1.8) + 32
kelvin = temp + 273.15

print(f'{temp:.2f} °C is equal to {fahrenheit:.2f} °F or {kelvin:.2f} K')
