'''
Name: Raul Costa
Date: 21/03/2022
EC148003 Software Development with Applied Mathematics with Python
Problem:
    Simple transpose formulae:
        Ohm's law:
            V = IR ( voltage = current * resistance )
            I = VR ( current = voltage / resistence )
            R = VC ( resistence = voltage / current )

Constraints:
    voltage >0
    current >0
    resistance >0

Functional requirement:
    accuracy to 1 decimal place.

Important: your code for this task must comply with this units coding style.


Your program should output the following (your time might be different):

Testing Current
.Testing Voltage
.Testing Resistance
.Testing Resistance
.Testing Voltage
.Testing Voltage
.
----------------------------------------------------------------------
Ran 6 tests in 0.001s

'''

import unittest


def calculate_voltage(current, resistance):
    '''
    Calculate and return the voltage by appling Ohm's Law to the giving parameters.
    '''
    voltage = current * resistance
    return voltage

def calculate_current(voltage, resistance):
    '''
    Calculate and return the current by appling Ohm's Law to the giving parameters.
    '''
    current = voltage / resistance
    return current


def calculate_resistance(voltage, current):
    '''
    Calculate and return the resistance by appling Ohm's Law to the giving parameters.
    '''
    resistance = voltage / current
    return resistance



class OhmsLawTestCases(unittest.TestCase):

    def test_voltage_01(self):
        print('Testing Voltage')
        self.assertEqual(calculate_voltage(21, 2), 42)

    def test_voltage_02(self):
        print('Testing Voltage')
        self.assertAlmostEqual(calculate_voltage(1.2, 3.4), 4.1, 1)

    def test_current_03(self):
        print('Testing Current')
        self.assertEqual(calculate_current(210, 12), 17.5)

    def test_current_04(self):
        print('Testing Current')
        self.assertAlmostEqual(calculate_current(112.5, 17.3), 6.5, 1)

    def test_current_05(self):
        print('Testing Resistance')
        self.assertEqual(calculate_resistance(84, 10), 8.4)

    def test_current_06(self):
        print('Testing Resistance')
        self.assertAlmostEqual(calculate_resistance(31.25, 12.5), 2.5, 1)

if __name__ == '__main__':
    unittest.main()
