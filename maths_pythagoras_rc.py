'''
Pythagoras Calculator
Name: Raul Costa
Date: 15/12/2021
Version: 1.1
***************************
1.1 - add loop to the function
1.0 - initial program
'''

import math

def pythagoras(a,b,f,u):
    print(f'x² = {a}² + {b}²')
    y = a * a
    z = b * b
    print(f'x² = {y:.{f}f} + {z:.{f}f}')
    t = y + z
    print(f'x² = {t:.{f}f}')
    q = math.sqrt(t)
    print(f'x = {q:.{f}f}{u}')
    print(f'______________________________________________________________')

def sides(b,x,f,u):
    print(f'a² = {b}² - {x}²')
    y = b * b
    z = x * x
    print(f'a² = {y:.{f}f} - {z:.{f}f}')
    t = y - z
    print(f'a² = {t:.{f}f}')
    q = math.sqrt(t)
    print(f'a = {q:.{f}f}{u}')
    print(f'______________________________________________________________')

def main():

    func = ''
    while func != 'q':
        func = input('\nLooking to find the Pythagoras Hypotenuse (p)\nLooking to find one of the sides (s)\nQuit (q)? :  ')
        if func == 'p':
            a = float(input('\nPlease enter side a: '))
            b = float(input('Please enter side b: '))
            f = int(input('Please enter result decimal points: '))
            u = input('Please enter the unit to be calculated Ex. mm, cm, m: ')
            pythagoras(a,b,f,u)
        elif func == 's':
            b = float(input('\nPlease enter side b: '))
            x = float(input('Please enter side x: '))
            f = int(input('Please enter result decimal points: '))
            u = input('Please enter the unit to be calculated Ex. mm, cm, m: ')
            if b > x:
                sides(b,x,f,u)
            else:
                sides(x,b,f,u)
        else:
            break


if __name__ == "__main__":
    main()
