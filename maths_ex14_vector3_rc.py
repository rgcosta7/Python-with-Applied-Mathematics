'''
Name: Raul Costa
Date: 28/02/2022
EC148003 Software Development with Applied Mathematics
Moodle Version

Important: your code for this task must comply with this units coding style.

An example of the EXACT output this program should produce:

--------------- 3D Vectors -------------
Please enter the x value for point 1: -3
Please enter the y value for point 1: 4
Please enter the z value for point 1: 5
Please enter the x value for point 2: 6
Please enter the y value for point 2: 7
Please enter the z value for point 2: 8

Addition
[-3.0, 4.0, 5.0] + [6.0, 7.0, 8.0] = [3.0, 11.0, 13.0]

Subtraction
[-3.0, 4.0, 5.0] - [6.0, 7.0, 8.0] = [-9.0, -3.0, -3.0]

Multiplication
[-3.0, 4.0, 5.0] x [6.0, 7.0, 8.0] = [-18.0, 28.0, 40.0]

Multiple by Scalar
[-3.0, 4.0, 5.0] x 5.0 = [-15.0, 20.0, 25.0]

Magnitude
[-3.0, 4.0, 5.0] has magnitude of 7.07


Don't forget to remove the TODOs
'''

from math import sqrt


class Vector3(object):
    '''
        Represents a 3D vector.
    '''
    # Class initializer/constructor.
    # Whenever an instance of a class is created its __init__ method is called.

    def __init__(self, x, y, z):
        '''
        x : The x coordinate in 3d-space.
        y : The y coordinate in 3d-space.
        z : The z coordinate in 3d-space.
        '''
        self.x = x
        self.y = y
        self.z = z

    # This method is called when the print() function is invoked on the given object.
    # This method returns a string, which should be a nicely printable
    # representation of the given object.
    def __str__(self):
        return f'[{self.x}, {self.y}, {self.z}]'

    # Addition
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    # Subtraction
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    # Multiplication
    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    # Multiplying scalar
    def multiple_by_scalar(self, scalar):
        return Vector3(self.x * scalar , self.y * scalar, self.z * scalar )

    # Magnitude/length
    @property
    def magnitude(self):
        mag = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return mag


# Do not edit the following code.
def main():
    print('--------------- 3D Vectors -------------')
    x1 = float(input('Please enter the x value for point 1: '))
    y1 = float(input('Please enter the y value for point 1: '))
    z1 = float(input('Please enter the z value for point 1: '))

    x2 = float(input('Please enter the x value for point 2: '))
    y2 = float(input('Please enter the y value for point 2: '))
    z2 = float(input('Please enter the z value for point 2: '))

    v1 = Vector3(x1, y1, z1)
    v2 = Vector3(x2, y2, z2)

    print()

    # Addition
    print('Addition')
    print(f'{v1} + {v2} = {v1 + v2}')
    print()

    # Subtraction
    print('Subtraction')
    print(f'{v1} - {v2} = {v1 - v2}')
    print()

    # Multiplication
    print('Multiplication')
    print(f'{v1} x {v2} = {v1 * v2}')
    print()

    # Multiple by scalar
    print('Multiple by Scalar')
    SCALAR = 5.0  # I have hardcoded this for convenience
    print(f'{v1} x {SCALAR} = {v1.multiple_by_scalar(SCALAR)}')
    print()

    # Magnitude
    print('Magnitude')

    print(f'{v1} has magnitude of {v1.magnitude:,.2f}')
    print()


if __name__ == "__main__":
    main()
