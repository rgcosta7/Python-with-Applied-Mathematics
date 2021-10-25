'''
Name: Raul Gomes da Costa
Date: 04/10/2021
EC148003 Software Development with Applied Mathematics with Python
Moodle Version
Percentages
Problem:
Finding a decrease in a value as a %
Important, remember to remove the TODO tag when you complete a task.

Constraints:
    old price > new price



Examples of the output this program should produce:

Finding a decrease in a value as a %
Please enter the old price: 125
Please enter the new price: 100
Old Price: £125.00 - New Price: £100.00 - Decrease: 20.00%


Finding a decrease in a value as a %
Please enter the old price: 45.50
Please enter the new price: 40.00
Old Price: £45.50 - New Price: £40.00 - Decrease: 12.09%
'''


oldprice = float(input("Plesae enter the old price: "))
newprice = float(input("Please enter the new price: "))

percentage = (oldprice - newprice) / oldprice * 100
print(f'Old Price: £{oldprice:.2f} - New Price: £{newprice:.2f} - Decrease: {percentage:.2f}% ')
