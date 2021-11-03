'''
Name: Raul Costa
Date: 01/11/2021
EC148003 Software Development with Applied Mathematics with Python
Moodle Version
Simple net income calculator.

Problem:
Calculate the amount of income tax payable and the net income for a given gross income.

Constraints:
    gross income >=0
    Tax rules:
    Gross Income	            Rate (in %)
    First £10,000  	            0
    Next £40,000	            20
    Remaining	                50


Examples of the exact output this program should produce:

Net Income Calculator:
Please enter the gross income: 10000
Gross Income: £10,000.00
Income Tax: £0.00
Net Income: £10,000.00

Net Income Calculator:
Please enter the gross income: 11000
Gross Income: £11,000.00
Income Tax: £200.00
Net Income: £10,800.00

Net Income Calculator:
Please enter the gross income: 50000
Gross Income: £50,000.00
Income Tax: £8,000.00
Net Income: £42,000.00


Net Income Calculator:
Please enter the gross income: 100000
Gross Income: £100,000.00
Income Tax: £33,000.00
Net Income: £67,000.00

Net Income Calculator:
Please enter the gross income: 123456.75
Gross Income: £123,456.75
Income Tax: £44,728.38
Net Income: £78,728.38

Important: Please thoroughly test your code before uploading.
And not forget to remove the TODO tags.

'''


def calc_tax_payable(gross_income):
    ''' A function that calculates the total tax payable for a given gross income.
        Returns:
        The total tax payable.
    '''
    tax_payable = 0.0

    if gross_income > 50000:
        tax_payable = (gross_income-10000) * 0.2
        tax_payable = (gross_income-50000) * 0.3 + tax_payable

    elif gross_income >= 10000:
        tax_payable = (gross_income-10000) * 0.2

    return tax_payable


def main():
    print('Net Income Calculator:')

    gross_income = float(input('Please enter the gross income: '))

    # function call to get the total tax payable on the given gross income
    tax_payable = calc_tax_payable(gross_income)

    net_income = gross_income - tax_payable

    print(f'Gross Income: £{gross_income:,.2f}')
    print(f'Income Tax: £{tax_payable:,.2f}')
    print(f'Net Income: £{net_income:,.2f}')

if __name__ == "__main__":
    main()
