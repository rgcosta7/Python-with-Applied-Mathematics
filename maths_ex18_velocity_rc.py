'''
Name: Raul Costa
Date:01/04/2022
EC148003 Software Development with Applied Mathematics with Python
Problem:
Simple transpose formulae:
    Velocity Calculator:
        v = u + at ( final velocity = initial velocity + (acceleration * time) )
        u = v - at ( initial velocity = final velocity - (acceleration * time) )
        a = (v - u) / t ( acceleration = (final velocity - initial velocity ) / time )
        t = (v - u) / a ( time = (final velocity - initial velocity ) / acceleration )


Functional requirement:
    accuracy to 1 decimal place

Important: your code for this task must comply with this units coding style.

https://peps.python.org/pep-0257/ # info docstring


Your program should output the following (your time might be different):

Testing Acceleration
.Testing Acceleration
.Testing Time
.Testing Time
.Testing Final Velocity
.Testing Final Velocity
.Testing Initial Velocity
.Testing Initial Velocity
.
----------------------------------------------------------------------
Ran 8 tests in 0.001s
'''

import unittest


def calculate_final_velocity(initial_velocity, acceleration, time):
    ''' Calculate and return the final velocity
    given the initial velocity, acceleration and time.
    '''
    final_velocity = initial_velocity + (acceleration * time)

    return final_velocity

def calculate_initial_velocity(final_velocity, acceleration, time):
    ''' Calculate and return the initial velocity
    given the final velocity, acceleration and time.
    '''
    initial_velocity = final_velocity - (acceleration * time)
    return initial_velocity


def calculate_acceleration(final_velocity, initial_velocity, time):
    ''' Calculate and return the acceleration
    given the final velocity, initial velocity and time.
    '''
    acceleration = (final_velocity - initial_velocity) /  time
    return acceleration

def calculate_time(final_velocity, initial_velocity, acceleration):
    ''' Calculate and return the time
    given the final velocity, initial velocity and acceleration.
    '''
    acceleration = (final_velocity - initial_velocity) /  acceleration
    return acceleration



# ---------------------- Do not modify code below this line ----------------------

class VelocityTestCases(unittest.TestCase):

    def test_final_velocity_01(self):
        print('Testing Final Velocity')
        self.assertAlmostEqual(calculate_final_velocity(0, 4.2, 10), 42.0, 1)

    def test_final_velocity_02(self):
        print('Testing Final Velocity')
        self.assertAlmostEqual(
            calculate_final_velocity(0, -9.8, 5.5), -53.9, 1)

    def test_initial_velocity_01(self):
        print('Testing Initial Velocity')
        self.assertAlmostEqual(
            calculate_initial_velocity(42, 4.2, 4), 25.2, 1)

    def test_initial_velocity_02(self):
        print('Testing Initial Velocity')
        self.assertAlmostEqual(
            calculate_initial_velocity(-53.9, -9.8, 6), 4.9, 1)

    def test_calculate_acceleration_01(self):
        print('Testing Acceleration')
        self.assertAlmostEqual(calculate_acceleration(24, 12, 4), 3.0, 1)

    def test_calculate_acceleration_02(self):
        print('Testing Acceleration')
        self.assertAlmostEqual(calculate_acceleration(50, 100, 4), -12.5, 1)

    def test_calculate_time_01(self):
        print('Testing Time')
        self.assertAlmostEqual(calculate_time(33, 3, 2.4), 12.5, 1)

    def test_calculate_time_02(self):
        print('Testing Time')
        self.assertAlmostEqual(calculate_time(150, 0, 6.5), 23.1, 1)


if __name__ == '__main__':
    unittest.main()
