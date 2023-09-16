# order.py
from kiteconnect import KiteConnect
import json
import logging

logging.basicConfig(level=logging.DEBUG)

with open('config.json', 'r') as file:
    config = json.load(file)

api_key = config['KITE_API_KEY']
access_token = config['KITE_ACCESS_TOKEN']

kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

# Place an order
try:
    order_id = kite.place_order(
        variety=kite.VARIETY_REGULAR,
        exchange=kite.EXCHANGE_NSE,
        tradingsymbol="VIKASLIFE",
        transaction_type=kite.TRANSACTION_TYPE_BUY,
        quantity=1,
        product=kite.PRODUCT_CNC,
        order_type=kite.ORDER_TYPE_MARKET
    )

    logging.info("Order placed. ID is: {}".format(order_id))
except Exception as e:
    logging.info("Order placement failed: {}".format(e))

# Fetch all orders
kite.orders()
