#!/usr/bin/env python3
# coinbase-dca.py
# pip install coinbase-advanced-py
# python3 -m pip install coinbase-advanced-py --break-system-packages

# python3 coinbase-dca.py BTC-USD 80000 1000 250 80

import sys
import time
import uuid
from coinbase.rest import RESTClient

API_KEY = ""
API_SECRET = """"""

def main():

    # for testing
    # client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)
    # print(client.get_accounts())

    if len(sys.argv) != 6:
        print("usage: python coinbase-dca.py <product_id> <price_high> <price_low> <price_step> <usd_per_order>")
        sys.exit(1)

    product_id = sys.argv[1]
    price_high = float(sys.argv[2])
    price_low = float(sys.argv[3])
    price_step = float(sys.argv[4])
    usd_per_order = float(sys.argv[5])

    client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)

    price = price_high
    while price >= price_low:
        base_size = round(usd_per_order / price, 8)
        print(f"placing limit buy: ${usd_per_order} (~{base_size} ${product_id}) @ ${price}")

        client.create_order(
            client_order_id=str(uuid.uuid4()),
            product_id=product_id,
            side="BUY",
            order_configuration={
                "limit_limit_gtc": {
                    "base_size": str(base_size),
                    "limit_price": str(price)
                }
            }
        )

        price -= price_step
        time.sleep(0.2) # rate limit

if __name__ == "__main__":
    main()