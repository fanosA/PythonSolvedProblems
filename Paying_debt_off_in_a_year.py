r"""
Problem 2: Paying Debt Off in a Year
15.0/15.0 points (graded)
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal
"""

lowestPayment = balance/12
lowestPayment = int(round(lowestPayment,-1))
temp = balance
while True:
    balance = temp
    for i in range(12):
        balance -= lowestPayment
        balance += balance*(annualInterestRate/12)
    if balance > 0:
        lowestPayment += 10
    else:
        break
print("Lowest Payment: " + str(lowestPayment))
