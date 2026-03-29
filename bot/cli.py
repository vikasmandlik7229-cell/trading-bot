import argparse
from .orders import place_order
from .validators import validate_input
from .logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--order_type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:
        validate_input(
            args.symbol,
            args.side,
            args.order_type,
            args.quantity,
            args.price
        )

        print("\n========== ORDER SUMMARY ==========")
        print(f"Symbol     : {args.symbol}")
        print(f"Side       : {args.side}")
        print(f"Type       : {args.order_type}")
        print(f"Quantity   : {args.quantity}")
        if args.price:
            print(f"Price      : {args.price}")
        print("===================================\n")

        order = place_order(
            args.symbol,
            args.side,
            args.order_type,
            args.quantity,
            args.price
        )

        print(" SUCCESS\n")
        print("========== ORDER RESPONSE ==========")
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice')}")
        print("===================================")

    except Exception as e:
        print(f"\n ERROR: {e}")

if __name__ == "__main__":
    main()