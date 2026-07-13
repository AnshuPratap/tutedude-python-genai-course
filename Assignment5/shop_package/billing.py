def calculate_total(prices):
    Total_bill = sum(prices)
    return Total_bill

def apply_tax(amount):
    tax_amount = amount*0.05
    Total_amount = tax_amount + amount
    return Total_amount