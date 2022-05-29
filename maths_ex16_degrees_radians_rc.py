'''
Name: Raul Costa
Date: 14/03/2022
EC148003 Software Development with Applied Mathematics
Moodle Version

Automated Testing via unit testing.
In computer programming, unit testing is a software testing method by which functions
are tested to determine whether they are fit for purpose.

https://realpython.com/python-testing/


Important: your code for this task must comply with this units coding style.
And for this task you are not allowed to use the math.radians(var) or math.degrees(var) functions.


Your program should output the following (your time might be different):

Testing Radians To Degrees
.Testing Radians To Degrees
.Testing Radians To Degrees
.Testing Degrees To Radians
.Testing Degrees To Radians
.Testing Degrees To Radians
.
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK

'''

from math import pi
import unittest


def to_radians(degrees):
    '''Converts an angle in degrees to an angle in radians.
    '''
    radians = degrees * pi/180
    return radians


def to_degrees(radians):
    '''Converts an angle in radians to an angle in degrees.
    '''
    degrees = radians * 180/pi
    return degrees


class TestAssignment1(unittest.TestCase):
    def test_to_radians_01(self):
        print('Testing Degrees To Radians')
        # 90.0 is the value/parameter passed into the function to_radians(degrees)
        # 1.571 is the expected value rounded to 3 decimal places
        self.assertAlmostEqual(to_radians(90.0), 1.571, 3)

    def test_to_radians2(self):
        print('Testing Degrees To Radians')
        self.assertAlmostEqual(to_radians(-180), -3.142, 3)

    def test_to_radians3(self):
        print('Testing Degrees To Radians')
        self.assertAlmostEqual(to_radians(84.5), 1.5, 1)

    def test_to_degrees_01(self):
        print('Testing Radians To Degrees')
        # 3 is the value/parameter passed into the function to_degrees(radians)
        # 171.89 is the expected value rounded to 2 decimal places
        self.assertAlmostEqual(to_degrees(3), 171.89, 2)

    def test_to_degrees2(self):
        print('Testing Radians To Degrees')
        self.assertAlmostEqual(to_degrees(25), 1432.39, 2)

    def test_to_degrees3(self):
        print('Testing Radians To Degrees')
        self.assertAlmostEqual(to_degrees(-12), -687.55, 2)


if __name__ == '__main__':
    unittest.main()
