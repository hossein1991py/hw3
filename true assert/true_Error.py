def apply_discount(price: int, discount:float = 0.0) -> int:
    
    """Apply Discount Percent and Calculate Final Price"""
    
    final_price = int(price * (1 - discount))
    if not (0 < final_price <= price):
        raise ValueError(" Unacceptable price expected ")
    return final_price

# Take input from user
price_user = float(input("Enter the price: "))
discount_user = float(input("Enter the discount percent (decimal): "))

# Calculate the final price
finalprice = apply_discount(price_user, discount_user)

# Display the final price to the user
print("price is:", finalprice)