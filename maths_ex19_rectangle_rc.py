'''
Name: Raul Costa
Date: 28/04/2022
EC148003 Software Development with Applied Mathematics with Python
Problem: complete the rectangle class - this task is more python than mathematics.

Four of the functions have been completed for you as examples.

You might find it useful to draw the unit test rectangle on graph paper first - remembering
that (0, 0) is the top left.

Important: your code for this task must comply with this units coding style.
Also, remember to remove the TODO when you complete a task.

Your program should output the following (your time might be different):

Testing Area 1
.Testing Area 2
.Testing Bottom 1
.Testing Bottom 2
.Testing Bottom-Left
.Testing Bottom-Left 2
.Testing Bottom-Right 1
.Testing Bottom-Right 2
.Testing Centre 1
.Testing Centre 2
.Testing Centre-X 1
.Testing Centre-X 2
.Testing Centre-Y
.Testing Centre-Y 2
.Testing Diagonal 1
.Testing Diagonal 2
.Testing Left 1
.Testing Left 2
.Testing Middle-Bottom 1
.Testing Middle-Bottom 2
.Testing Middle-Left 1
.Testing Middle-Left 2
.Testing Middle-Right 1
.Testing Middle-Right 2
.Testing Middle-Top 1
.Testing Middle-Top 2
.Testing Perimeter 1
.Testing Perimeter 2
.Testing Right 1
.Testing Right 2
.Testing Top 1
.Testing Top 2
.Testing Top-Left 1
.Testing Top-Left 2
.Testing Top-Right 1
.Testing Top-Right 2
.
----------------------------------------------------------------------
Ran 36 tests in 0.012s

OK

'''
from curses.textpad import rectangle
from math import sqrt
import unittest


class Rectangle():
    '''
        Represents a rectangle.
    '''

    def __init__(self, x, y, width, height):
        self.x = x  # distance from the left of the screen
        self.y = y  # distance from the top of the screen
        self.width = width
        self.height = height

    @property
    def area(self):
        return (self.width * self.height) # returns the rectangle area

    @property
    def bottom(self):
        return (self.x + self.height) # returns distance from top of the screen to bottom

    @property
    def bottom_left(self):
        return (self.x, self.y + self.height) # returns two values (x,y) bottom left

    @property
    def bottom_right(self):
        return (self.x + self.width, self.y + self.height) # returns two values (x,y) bottom right

    @property
    def centre(self):
        return ((self.width / 2) + self.x, (self.height / 2) + self.y) # returns two values (x,y) from the centre

    @property
    def centre_x(self):
        return self.x + (self.width / 2) # returns value of the centre for x

    @property
    def centre_y(self):
        return self.y + (self.height / 2) # returns value of the centre for y

    @property
    def diagonal(self):
        return sqrt((self.height * self.height) + (self.width * self.width)) # calculate and return diagonal

    @property
    def left(self):
        return self.x  # returns a single value

    @property
    def middle_bottom(self):
        return (self.x + (self.width / 2), self.y + self.height)  # return two values (x,y) from middle bottom

    @property
    def middle_left(self):
        return (self.x, self.y + (self.height / 2 ))  # return two values (x,y) from middle left

    @property
    def middle_right(self):
        return (self.x + self.width, self.y + (self.height/2))  # return two values (x,y) from middle right

    @property
    def middle_top(self):
        return (self.y + (self.width / 2),self.x)  # return two values (x,y) from middle top

    @property
    def right(self):
        return self.x + self.width  # return height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)  # calculate and return perimeter

    @property
    def top(self):
        return self.y  # returns a single value

    @property
    def top_left(self):
        return (self.x, self.y)  # returns two values as a tuple

    @property
    def top_right(self):
        return (self.x + self.width, self.y)  # return two values (x,y) from top right


# ---------------------- Do not modify code below this line ----------------------

class RectangleTestCases(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(x=0, y=0, width=100, height=50)
        self.rect2 = Rectangle(x=10, y=10, width=200, height=50)

    # testing rectangle 1
    def test_area_1(self):
        print('Testing Area 1')
        self.assertEqual(self.rect1.area,  5000)

    def test_bottom_1(self):
        print('Testing Bottom 1')
        self.assertEqual(self.rect1.bottom, 50)

    def test_bottom_left_1(self):
        print('Testing Bottom-Left')
        self.assertEqual(self.rect1.bottom_left, (0, 50))

    def test_bottom_right_1(self):
        print('Testing Bottom-Right 1')
        self.assertEqual(self.rect1.bottom_right, (100, 50))

    def test_centre_1(self):
        print('Testing Centre 1')
        self.assertEqual(self.rect1.centre, (50, 25))

    def test_centre_x_1(self):
        print('Testing Centre-X 1')
        self.assertEqual(self.rect1.centre_x, 50)

    def test_centre_y_1(self):
        print('Testing Centre-Y')
        self.assertEqual(self.rect1.centre_y,  25)

    def test_diagonal_1(self):
        print('Testing Diagonal 1')
        self.assertAlmostEqual(self.rect1.diagonal,  111.803, 3)

    def test_top_1(self):
        print('Testing Top 1')
        self.assertEqual(self.rect1.top, 0)

    def test_right_1(self):
        print('Testing Right 1')
        self.assertEqual(self.rect1.right, 100)

    def test_left_1(self):
        print('Testing Left 1')
        self.assertEqual(self.rect1.left, 0)

    def test_top_left_1(self):
        print('Testing Top-Left 1')
        self.assertEqual(self.rect1.top_left, (0, 0))

    def test_top_right_1(self):
        print('Testing Top-Right 1')
        self.assertEqual(self.rect1.top_right, (100, 0))

    def test_middle_left_1(self):
        print('Testing Middle-Left 1')
        self.assertEqual(self.rect1.middle_left, (0, 25))

    def test_middle_right_1(self):
        print('Testing Middle-Right 1')
        self.assertEqual(self.rect1.middle_right, (100, 25))

    def test_middle_top_1(self):
        print('Testing Middle-Top 1')
        self.assertEqual(self.rect1.middle_top, (50, 00))

    def test_middle_bottom_1(self):
        print('Testing Middle-Bottom 1')
        self.assertEqual(self.rect1.middle_bottom, (50, 50))

    def test_perimeter_1(self):
        print('Testing Perimeter 1')
        self.assertEqual(self.rect1.perimeter,  300)

     # testing rectangle 2
    def test_area_2(self):
        print('Testing Area 2')
        self.assertEqual(self.rect2.area,  10000)

    def test_bottom_2(self):
        print('Testing Bottom 2')
        self.assertEqual(self.rect2.bottom, 60)

    def test_bottom_left_2(self):
        print('Testing Bottom-Left 2')
        self.assertEqual(self.rect2.bottom_left, (10, 60))

    def test_bottom_right_2(self):
        print('Testing Bottom-Right 2')
        self.assertEqual(self.rect2.bottom_right, (210, 60))

    def test_centre_2(self):
        print('Testing Centre 2')
        self.assertEqual(self.rect2.centre, (110, 35))

    def test_centre_x_2(self):
        print('Testing Centre-X 2')
        self.assertEqual(self.rect2.centre_x, 110)

    def test_centre_y_2(self):
        print('Testing Centre-Y 2')
        self.assertEqual(self.rect2.centre_y,  35)

    def test_diagonal_2(self):
        print('Testing Diagonal 2')
        self.assertAlmostEqual(self.rect2.diagonal,  206.155, 3)

    def test_top_2(self):
        print('Testing Top 2')
        self.assertEqual(self.rect2.top, 10)

    def test_right_2(self):
        print('Testing Right 2')
        self.assertEqual(self.rect2.right, 210)

    def test_left_2(self):
        print('Testing Left 2')
        self.assertEqual(self.rect2.left, 10)

    def test_top_left_2(self):
        print('Testing Top-Left 2')
        self.assertEqual(self.rect2.top_left, (10, 10))

    def test_top_right_2(self):
        print('Testing Top-Right 2')
        self.assertEqual(self.rect2.top_right, (210, 10))

    def test_middle_left_2(self):
        print('Testing Middle-Left 2')
        self.assertEqual(self.rect2.middle_left, (10, 35))

    def test_middle_right_2(self):
        print('Testing Middle-Right 2')
        self.assertEqual(self.rect2.middle_right, (210, 35))

    def test_middle_top_2(self):
        print('Testing Middle-Top 2')
        self.assertEqual(self.rect2.middle_top, (110, 10))

    def test_middle_bottom_2(self):
        print('Testing Middle-Bottom 2')
        self.assertEqual(self.rect2.middle_bottom, (110, 60))

    def test_perimeter_2(self):
        print('Testing Perimeter 2')
        self.assertEqual(self.rect2.perimeter,  500)


if __name__ == '__main__':
    unittest.main()
