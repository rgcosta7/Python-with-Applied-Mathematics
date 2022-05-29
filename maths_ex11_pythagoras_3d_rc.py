'''
Name: Raul Costa
Date: 22/01/2022
EC148003 Software Development with Applied Mathematics with Python
Moodle Version

Problem:
Finding the distance between two opposite corners, the longest diagonal, of a rectangular cuboid.

Functional requirement(s):
    you must use a function to calculate the longest diagonal
    accuracy to 1 decimal place

Constraints:
    width > 0
    length > 0
    height > 0


Important: your code must comply with this units coding style.


An example of the EXACT output this program should produce:

Finding the longest diagonal of a rectangular cuboid
Please enter the width: 5.5
Please enter the length: 6.5
Please enter the height: 7.5
The length of the longest diagonal is 11.3


'''

from math import sqrt

def diagonal(w,l,h):
    d1 = (w * w) + (l * l)
    d1 = sqrt(d1)
    d2 = (d1 * d1 ) + (h * h)
    d2 = sqrt(d2)
    return d2

def main():
    print('Finding the longest diagonal of a rectangular cuboid')
    w = float(input('Please enter the width? '))
    l = float(input('Please enter the length? '))
    h = float(input('Please enter the height? '))

    d = diagonal(w,l,h)

    print(f'The length of the longest diagonal is {d:.1f}')
if __name__ == "__main__":
    main()
