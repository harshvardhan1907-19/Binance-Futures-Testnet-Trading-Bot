import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

parser = argparse.ArgumentParser(
    description="Binance Futures Trading Bot"
)

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    symbol = args.symbol.upper()
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)
    price = validate_price(args.price, order_type)

    response = place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol   : {symbol}")
    print(f"Side     : {side}")
    print(f"Type     : {order_type}")
    print(f"Quantity : {quantity}")

    if price is not None:
        print(f"Price    : {price}")

    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID      : {response['orderId']}")
    print(f"Status        : {response['status']}")
    print(f"Executed Qty  : {response['executedQty']}")
    print(f"Price         : {response['price']}")

    print("\n✅ Order Submitted Successfully")

except ValueError as e:
    print(f"\n❌ Validation Error: {e}")

except Exception as e:
    print(f"\n❌ API Error: {e}")