'''
Name: Raul Costa
Date: 07/03/2022
EC148003 Software Development with Applied Mathematics with Python

Problem: create a function for this Circle class that will determine if two circles overlap.

Note that you have already done all the maths in previous exercises.

Your program should output the following:

.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s


OK
'''


import unittest
import math

class Circle(object):
    '''
        Represents a circle.
    '''

    def __init__(self, x, y,  radius):
        '''
        The x-coordinate position of the centre of the circle.
        The y-coordinate position of the centre of the circle.
        The radius - the length of the radius of the circle.
        '''
        self.x = x
        self.y = y
        self.radius = radius

    def overlap(self, other) -> bool:
        # returns true if two circles overlap
        overlap = math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
        if overlap == self.radius + other.radius:
            return False
        elif overlap == self.radius - other.radius:
            return False
        else:
            return True

class CircleTestCases(unittest.TestCase):
    # Do not edit the following code.

    def setUp(self):
        self.circle = Circle(10, 10, 5)

    def test_overlap_01(self):
        other_circle = Circle(20, 10, 5)
        self.assertFalse(self.circle.overlap(other_circle))

    def test_overlap_02(self):
        other_circle = Circle(10, 20, 5)
        self.assertFalse(self.circle.overlap(other_circle))

    def test_overlap_03(self):
        other_circle = Circle(0, 10, 5)
        self.assertFalse(self.circle.overlap(other_circle))

    def test_overlap_04(self):
        other_circle = Circle(10, 0, 5)
        self.assertFalse(self.circle.overlap(other_circle))

    def test_overlap_05(self):
        other_circle = Circle(18, 10, 5)
        self.assertTrue(self.circle.overlap(other_circle))

    def test_overlap_06(self):
        other_circle = Circle(-10, 10, 20)
        self.assertTrue(self.circle.overlap(other_circle))

    def test_overlap_07(self):
        other_circle = Circle(-10, -10, 24)
        self.assertTrue(self.circle.overlap(other_circle))


if __name__ == '__main__':
    unittest.main()
