from bot.client import get_client

client = get_client()

try:
    balances = client.futures_account_balance()

    for balance in balances:
        if balance["asset"] == "USDT":
            print(balance)

except Exception as e:
    print(e)