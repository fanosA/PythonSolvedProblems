r"""
Problem 1: Paying the Minimum
10.0/10.0 points (graded)
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal
"""

paid=0
for i in range(1,13):
    print('Month: ' + str(i))
    minimumPayment = balance*monthlyPaymentRate
    print('Minimum monthly payment: ' ),
    print("%1.2f" % minimumPayment)
    paid += balance*monthlyPaymentRate
    balance -= balance*monthlyPaymentRate
    balance += balance*(annualInterestRate/12)
    print("Remaining balance: " ),
    print("%1.2f" % balance)
print("Total paid: "),
print("%1.2f" % paid)
print("Remaining balance: " ),
print("%1.2f" % balance)
