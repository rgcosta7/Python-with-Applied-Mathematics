'''
Name: Raul Costa
Date: 29/11/2021
EC148003 Software Development with Applied Mathematics with Python
Moodle Version
Problem:
Drop Time Calculator.
If you were to drop a small iron ball from a height - say the Leaning Tower of Pisa
for example, how long would it take before it hit the ground?


Examples of the exact output this program should produce:

Drop Time Calculator
Please enter the height in metres: 55.86
It would take 3.4 seconds for the ball to drop 55.86 m.


Constraints:
    height > 0

'''
from math import sqrt

def calc_drop_time(height):
    if height > 0:
        drop_time = sqrt(2 * height / 9.8)
        return drop_time
    else:
        return 0

# Do not modify the code below this line.
def main():
    print('Drop Time Calculator')

    height = float(input('Please enter the height in metres: '))

    drop_time = calc_drop_time(height)

    print(
        f'It would take{drop_time: 0.1f} seconds for the ball to drop {height} m.')


if __name__ == "__main__":
    main()


'''
The time t (s) for free fall from height x (m) is:
t (s) = SQR[2 • x (m) / g (m/s^2)]
'''
