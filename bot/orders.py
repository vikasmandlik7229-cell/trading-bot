import logging
from .client import get_client


client = get_client()


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()
        quantity = float(quantity)

        
        if quantity < 0.002:
            raise ValueError(
                "Quantity too small. Minimum for BTCUSDT should be around 0.002 (≈100 USDT)."
            )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "recvWindow": 60000  
        }

        
        if order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT order")

            params["price"] = float(price)
            params["timeInForce"] = "GTC"

        logging.info("Placing order with parameters:")
        logging.info(params)

     
        response = client.futures_create_order(**params)

        logging.info("Order placed successfully:")
        logging.info(response)

        return response

    except Exception as e:
        logging.error("Error while placing order:")
        logging.error(str(e))
        raise