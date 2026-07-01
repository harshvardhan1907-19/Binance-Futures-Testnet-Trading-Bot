from bot.orders import place_market_order

try:

    response = place_market_order(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.001
    )

    print("\n========== ORDER REQUEST ==========")
    print("Symbol   :", "BTCUSDT")
    print("Side     :", "BUY")
    print("Type     :", "MARKET")
    print("Quantity :", 0.001)

    print("\n========== ORDER RESPONSE ==========")
    print("Order ID      :", response["orderId"])
    print("Status        :", response["status"])
    print("Executed Qty  :", response["executedQty"])
    print("Price         :", response["price"])

    print("\n✅ Order Submitted Successfully")

except Exception as e:
    print("\n❌ Order Failed")
    print(e)