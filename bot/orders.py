from bot.client import get_client
from bot.logging_config import logger

def place_order(symbol, side, order_type, quantity, price=None):
    """
    Places a MARKET or LIMIT order on Binance Futures Testnet.

    Args:
        symbol (str): Trading symbol (e.g. BTCUSDT)
        side (str): BUY or SELL
        order_type (str): MARKET or LIMIT
        quantity (float): Order quantity
        price (float, optional): Required for LIMIT orders

    Returns:
        dict: Binance API response
    """

    logger.info(
        f"Order Request -> Symbol={symbol}, Side={side}, Type={order_type}, Quantity={quantity}, Price={price}"
    )

    try:
        client = get_client()

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(
            f"Order Response -> "
            f"OrderId={response['orderId']}, "
            f"Status={response['status']}, "
            f"ExecutedQty={response['executedQty']}"
        )

        return response

    except Exception as e:
        logger.error(f"Order Failed -> {e}")
        raise