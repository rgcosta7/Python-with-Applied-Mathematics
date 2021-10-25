'''
Name: Raul Costa
Date: 25/10/2021
EC148003 Software Development with Applied Mathematics with Python
Moodle Version
Concrete Quote Calculator.


alt+0179 = ³

Constraint:
    quote  >= minimum order price


Examples of the exact output this program should produce:

Concrete Quote Calculator:
 Please enter the width (m): 5
 Please enter the length (m): 6
 Please enter the depth (m): .25
 Please enter the cost (m³): 90

Concrete Quote:
 Width: 5.0 m
 Length: 6.0 m
 Depth: 0.25 m
 Volume: 7.50 m³
 Cost : £90.00 per m³
 Quote: £675.00


Concrete Quote Calculator:
 Please enter the width (m): 4.2
 Please enter the length (m): 4.4
 Please enter the depth (m): .15
 Please enter the cost (m³): 90

Concrete Quote:
 Width: 4.2 m
 Length: 4.4 m
 Depth: 0.15 m
 Volume: 2.77 m³
 Cost : £90.00 per m³
 Quote: £250.00

'''


print('Concrete Quote Calculator:')

MIN_ORDER = 250  # the minimum order - price in pounds

width = float(input("Please enter the width (m): "))
length = float(input("Please enter the lenght (m): "))
depth = float(input("Please enter the depth (m): "))
cost = float(input("Please enter the cost (m³): "))

volume = length * width * depth
quote = cost * volume

if quote >= MIN_ORDER:
    print()
    print(f'Concrete Quote\n Width: {width} m\n Length: {length} m\n Depth: {depth} m\n ', end='')
    print(f'Volume: {volume:.2f} m³\n Cost: {cost:.2f} per m³\n Quote: £{quote:.2f}')
else:
    print()
    print('Minimum order value not reached!')
