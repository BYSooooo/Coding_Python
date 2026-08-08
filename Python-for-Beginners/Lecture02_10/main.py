## Return Values

# Calculate Tax
def tax_calc(money):
    print(money * 0.35)

# Showing the tax wichi is calculated.
def pay_tax(tax):
    print("thank you for paying", tax)

tax_calc(1500000)
# pay_tax(?????)


# Retun of calculated tax
def tax_calc01(money):
    return money * 0.35

def pay_tax01(tax):
    print("thank you for paying", tax)

# get a return value to Variable
to_pay = tax_calc01(1500000)
# set a Argument to pay_tax01
pay_tax01(to_pay)
# more shot
pay_tax01(tax_calc01(1500000))
