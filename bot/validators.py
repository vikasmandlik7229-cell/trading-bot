def validate_input(symbol, side, order_type, quantity, price):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    try:
        quantity = float(quantity)
    except:
        raise ValueError("Quantity must be a number")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")
        try:
            price = float(price)
        except:
            raise ValueError("Price must be a number")

        if price <= 0:
            raise ValueError("Price must be positive")