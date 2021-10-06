'''
Name: Raul Costa
Date: 20/09/2021
EC148003 Software Development with Applied Mathematics with Python
Moodle Version
Percentages
Problem:
Finding a % increase as a value

Examples of the output this program should produce:

Finding a % increase as a value
Please enter the current price: 100
Please enter the percentage increase: 10
Current Price: £100.00 - Percentage Increase: 10.00% - New Price: £110.00

Finding an increase in a value as a %
Please enter the new price: 50.25
Please enter the old price: 5.75 <-----
Current Price: £50.25 - Percentage Increase: 5.75% - New Price: £53.14

'''


print("Finding a % increase as a value")
current_price = float(input("Please enter the current price: "))
percentage_increase = float(input("Please enter the percentage increase: "))
new_price = (current_price * percentage_increase) / 100 + current_price
print(f'Current Price: £{current_price:,.2f} - Percentage Increase: {percentage_increase:,.2f}% - New Price: £{new_price:,.2f}')
