price = float(input("Input the original price: "))
discount_percent = float(input("Input the discount percentage: "))

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (discount_percent / 100 * price)
        print(f"The final price is {final_price}")
        return final_price
    else:
        print(f"{price}")

calculate_discount(price, discount_percent)
