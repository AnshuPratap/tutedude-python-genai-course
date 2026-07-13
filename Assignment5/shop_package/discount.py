def apply_discount(price,percent):
    if percent < 0 or percent > 100:
        print("Perecnt will be in between 0 and 100")
        return None
    else:
        discount = (price * percent)/100
        discounted_price = price - discount
        return discounted_price
    
def flat_discount(price):
    return price - 50
