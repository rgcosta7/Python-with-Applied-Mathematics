'''
Name: Raul Costa
Date: 30/01/2022
EC148003 Software Development with Applied Mathematics with Python
Moodle Version
Problem:
    Finding the properties of a regular square-based pyramid.

To solve this task you may have to carry out some additional research.

Functional requirements:
    you must use functions to calculate the various properties
    accuracy to 1 decimal place

Constraints:
    base > 0
    slant height > 0


Important: your code for this task must comply with this units coding style.


An example of the EXACT output this program should produce:

The properties a regular square-based pyramid.
Please enter the length of the base: 12.4
Please enter the length of the slant height: 10.6
Properties
        Vertical Height: 8.6 units
        Slant Height: 10.6 units
        Base Length: 12.4 units
        Base Perimeter: 49.6 units
        Lateral Edge Length : 12.3 units
        Volume: 440.7 units³
        Base Surface Area: 153.8 units²
        Lateral Surface Area: 65.7 units²
        Total Lateral Surface Area: 262.9 units²
        Total Surface Area: 416.6 units²


'''
from math import sqrt
def calculate_height(base,slant):
    return sqrt(slant*slant-(base/2)*(base/2))

def calculate_perimeter(base):
    return (4*base)

def calculate_length(base,height):
    return sqrt(height*height + (base*base/2))

def calculate_volume(base,height):
    return 1/3 * base * base * height

def calculate_surface(base):
    return base*base

def calculate_lateral(base,height):
    return base/2 * sqrt(base*base/4+height*height)

def calculate_total(base,slant):
    return 4*(1/2*base*slant)

def calculate_tsurface(base,height):
    return base * sqrt(base*base+4*(height*height))+base*base

def main():

    print('The properties a regular square-based pyramid.')
    base=float(input('Please enter the length of the base: '))
    slant=float(input('Please enter the length of the slant height: '))
    print('Properties')

    height = calculate_height(base,slant)
    print(f'\tVertical Height: {height:.1f} units')
    print(f'\tSlant Height: {slant:.1f} units')
    print(f'\tBase Length: {base:.1f} units')

    perimeter = calculate_perimeter(base)
    print(f'\tBase Perimeter: {perimeter:.1f} units')

    length = calculate_length(base,height)
    print(f'\tLateral Edge Length : {length:.1f} units')

    volume = calculate_volume(base,height)
    print(f'\tVolume: {volume:.1f} units³')

    surface = calculate_surface(base)
    print(f'\tBase Surface Area: {surface:.1f} units²')

    lateral = calculate_lateral(base,height)
    print(f'\tLateral Surface Area: {lateral:.1f} units²')

    total = calculate_total(base,slant)
    print(f'\tTotal Lateral Surface Area: {total:.1f} units²')

    tsurface = calculate_tsurface(base,height)
    print(f'\tTotal Surface Area: {tsurface:.1f} units²')

if __name__ == "__main__":
    main()
