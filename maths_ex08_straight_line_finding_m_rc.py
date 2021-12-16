'''
Name: Raul Costa
Date: 25/11/2021
EC148003 Software Development with Applied Mathematics with Python
Moodle Version

Problem:
Finding m, slope/gradient, of a straight line giving the
cordinates for any two points along its length.

Examples of the exact output this program should produce:

Finding (m) the slope/gradient of a straight line:
Please enter the x value for point 1: -3
Please enter the y value for point 1: -1
Please enter the x value for point 2: 6
Please enter the y value for point 2: 3
The slope (m) for that straight line is 0.44

Finding (m) the slope/gradient of a straight line:
Please enter the x value for point 1: -1
Please enter the y value for point 1: 5
Please enter the x value for point 2: 3
Please enter the y value for point 2: -3
The slope (m) for that straight line is -2.00


Important: Please thoroughly test your code before uploading.
And do not forget to remove the TODO tags.
'''


def find_m(x1, y1, x2, y2):
    '''
    calculate the slope/gradient of a straight line
    Parameters:
        x1, the x value of the first point
        y1, the y value of the first point
        x2, the x value of the second point
        y2, the y value of the second point
    Returns:
        m the slope/gradient

    '''

    m = (y2 - y1) / (x2 - x1)

    return m


def main():
    print('Finding (m) the slope/gradient of a straight line:')

    x1 = float(input('Please enter the x value for point 1: '))
    y1 = float(input('Please enter the y value for point 1: '))

    x2 = float(input('Please enter the x value for point 2: '))
    y2 = float(input('Please enter the y value for point 2: '))

    result = find_m(x1, y1, x2, y2)

    print(f'The slope (m) for that straight line is {result:,.2f}')


if __name__ == "__main__":
    main()
