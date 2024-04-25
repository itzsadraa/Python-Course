# Calculate income tax for the given income by adhering to the rules below
'''
Taxable Income            Rate (in %)
First $10,000                  0
Next $10,000                   10
The remaining                  20

For example, suppose the taxable income is 45000, and the income tax payable is
10000*0% + 10000*10%  + 25000*20% = 6000
'''

# define income and tax
income = 45000
tax = 0

# when income is under $10,000
if income <= 10000:
    tax = 0
# when income is under $20,000
elif income <= 20000:
    tax = (income - 10000) * 0.1
# when income is over $20,001
else:
    tax = 1000 + (income - 20000) * 0.2

print(tax)
