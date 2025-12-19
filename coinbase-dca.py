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

# def create_order(z, y):

    # print(f"placing limit buy: ${usd_per_order} (~{base_size} ${product_id}) @ ${price}")

    # client.create_order(
    #     client_order_id=str(uuid.uuid4()),
    #     product_id=product_id,
    #     side="BUY",
    #     order_configuration={
    #         "limit_limit_gtc": {
    #             "base_size": str(z),
    #             "limit_price": str(y)
    #         }
    #     }
    # ) 

def main():
    product_id = sys.argv[1]
    mode = sys.argv[2]
    price_high = float(sys.argv[3])
    price_low = float(sys.argv[4])
    price_step = float(sys.argv[5])
    total_usd = float(sys.argv[6])

    number_of_orders = round((price_high - price_low) / price_step)

    price = price_high

    round_to = 8
    if product_id == "DOGE-USD":
        round_to = 2

    # # for testing
    # client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)
    # print(client.get_accounts())

    if len(sys.argv) != 7:
        print("usage: python coinbase-dca.py <product_id> <mode> <price_high> <price_low> <price_step> <total_usd>")
        sys.exit(1)

    if mode != "flat" and mode != "aggr":
        print("mode must be 'flat' or 'aggr'")
        sys.exit(1)

    # client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)

    while price >= price_low:
        if mode == "flat":
            # print("flat")
            usd_per_order = round(total_usd / number_of_orders, 2)

            base_size = round(usd_per_order / price, round_to)
            base_size = f"{base_size:.{round_to}f}"
            
            print(f"placing limit buy: ${usd_per_order} (~{base_size} ${product_id}) @ ${price}")
            # create_order(base_size, price)
        elif mode == "aggr":
            print("aggr")

        price -= price_step
        time.sleep(0.2) # rate limit


    # price = price_high
    # while price >= price_low:
    #     base_size = round(usd_per_order / price, 8)
    #     print(f"placing limit buy: ${usd_per_order} (~{base_size} ${product_id}) @ ${price}")

    #     client.create_order(
    #         client_order_id=str(uuid.uuid4()),
    #         product_id=product_id,
    #         side="BUY",
    #         order_configuration={
    #             "limit_limit_gtc": {
    #                 "base_size": str(base_size),
    #                 "limit_price": str(price)
    #             }
    #         }
    #     )

    #     price -= price_step
    #     time.sleep(0.2) # rate limit

if __name__ == "__main__":
    main()