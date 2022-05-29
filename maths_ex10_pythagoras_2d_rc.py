'''
Name: Raul Costa
Date: 12/01/2022
EC148003 Software Development with Applied Mathematics with Python
Moodle Version
Pythagoras 2D - Right-Angled Triangle

Important: your code must comply with the current document coding style.

An example of the EXACT output this program must produce:

Find the length of an hypotenuse side in a right-angled triangle.
Please enter the length of side a: 5.5
Please enter the length of side b: 8.7
The length of the shortest hypotenuse is: 10.3

Find the length of an unknown side other than the hypotenuse in a right-angled triangle.
Please enter the length of the hypotenuse side: 15.1
Please enter the length of the other known side: 9.3
The length of the unknown side is 11.9
'''

from math import sqrt

# functions #TODO
def calc_hypotenuse(a,b):
    y = a * a + b * b
    c = sqrt(y)
    return c

def calc_unknows(a,b):
    y = a * a - b * b
    c = sqrt(y)
    return c

def main():
    print('Find the length of an hypotenuse side in a right-angled triangle.')
    a = float(input('Please enter the length of side a: '))
    b = float(input('Please enter the length of side b: '))

    c = calc_hypotenuse(a, b)
    print(f'The length of the hypotenuse is: {c:,.1f}')
    print()

    print('Find the length of an unknown side other than the hypotenuse in a right-angled triangle.')
    a = float(input('Please enter the length of the hypotenuse side: '))
    b = float(input('Please enter the length of the other known side: '))

    c = calc_unknows(a, b)
    print(f'The length of the unknown side is {c:,.1f}')

if __name__ == "__main__":
    main()
