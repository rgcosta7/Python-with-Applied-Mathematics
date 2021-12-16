'''
Name: Raul Costa
Date: 15/11/2021
EC148003 Software Development with Applied Mathematics with Python
Moodle Version

Iron Ball Weight Calculator.
Problem:
Given the diameter of a solid iron ball, in centimetres, determine its weight.
To solve this tasks you may have to carry out some additional research.


Constraints:
    diameter >= 1.0

Requirements:
    If the weight is less than 1 kg then display the result in grams to zero decimal places.
    If weight is greater than or equal to 100 kg then display the result in kilograms to zero decimal places.
    Otherwise display the weight in kilograms to 1 decimal place.


Examples of the exact output this program should produce:



Iron Ball Weight Calculator:
Please enter the diameter in centimetres: 6.2
Weight: 983 g


Iron Ball Weight Calculator:
Please enter the diameter in centimetres: 6.4
Weight: 1.1 kg


Iron Ball Weight Calculator:
Please enter the diameter in centimetres: 29
Weight: 101 kg


Important: please thoroughly test your code before uploading.
And do not forget to remove any TODO tags.
'''
import math

DENSITY_IRON = 7.874  # g/cm3.


def calc_weight(diameter):
    ''' Calculate the weight of a solid iron ball.
    Parameters:  diameter in centimetres
    Returns:  weight in grams
    '''
    volume = (4 * math.pi / 3) * (diameter / 2) ** 3
    weight = volume * DENSITY_IRON
    return weight



def main():
    print('Iron Ball Weight Calculator:')

    diameter = float(input('Please enter the diameter in centimetres: '))
    wight = calc_weight(diameter)
    if int(wight) in range (0,1000):
        print(f'Weight: {wight:.0f} g')
    elif int(wight) in range(1001,100000):
        print(f'Weight: {wight /1000:.1f} kg')
    else:
        print(f'Weight: {wight /1000:.0f} kg')



if __name__ == "__main__":
    main()
