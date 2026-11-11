def process_order(item, quantity):
    if not isinstance(item, str) or not item.strip():
        return "Error: Invalid item name."
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        return "Error: Invalid quantity."
    return f"Successfully ordered {quantity} {item}(s)."

def calculate_total(prices):
    if not isinstance(prices, list):
        return 0.0
    total = 0.0
    for price in prices:
        if isinstance(price, (int, float)) and not isinstance(price, bool) and price >= 0:
            total += float(price)
    return round(total, 2)

def validate_coupon(coupon):
    if not isinstance(coupon, str):
        return False
    valid_coupons = {"COFFEE10", "FREESHOT", "DISCOUNT20"}
    return coupon.strip() in valid_coupons

if __name__ == "__main__":
    print(process_order("Latte", 2))
    print(calculate_total([3.5, 4.0, 2.75]))
    print(validate_coupon("COFFEE10"))