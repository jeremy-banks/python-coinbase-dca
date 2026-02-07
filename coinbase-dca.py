#!/usr/bin/env python3
# coinbase-dca.py
# pip install coinbase-advanced-py
# python3 -m pip install coinbase-advanced-py --break-system-packages

# python3 coinbase-dca.py BTC-USD 80000 1000 250 80

import sys
import time
import uuid
import argparse
from coinbase.rest import RESTClient

API_KEY = ""
API_SECRET = """"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("product_id", nargs="?", default="")
    parser.add_argument("mode", nargs="?", default="")
    parser.add_argument("price_high", nargs="?", type=float, default=0)
    parser.add_argument("price_low", nargs="?", type=float, default=0)
    parser.add_argument("price_step", nargs="?", type=float, default=0)
    parser.add_argument("total_usd", nargs="?", type=float, default=0)

    args = parser.parse_args()

    product_id = args.product_id
    mode = args.mode
    price_high = args.price_high
    price_low = args.price_low
    price_step = args.price_step
    total_usd = args.total_usd

    # old code
    # product_id = sys.argv[1]
    # mode = sys.argv[2]
    # price_high = float(sys.argv[3])
    # price_low = float(sys.argv[4])
    # price_step = float(sys.argv[5])
    # total_usd = float(sys.argv[6])

    client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)

    if product_id == "test":
        print(client.get_accounts())
        # print("test passed")
        sys.exit(1)

    price_range = price_high - price_low
    number_of_orders = round(price_range / price_step)

    price = price_high
    usd_per_order = 0

    round_to = 8

    # old code
    # if len(sys.argv) != 7:
    #     print("usage: python coinbase-dca.py <product_id> <mode> <price_high> <price_low> <price_step> <total_usd>")
    #     sys.exit(1)

    while price >= price_low:
        if mode == "flat":
            # print("flat")
            usd_per_order = round(total_usd / number_of_orders, 2)

            base_size = round(usd_per_order / price, round_to)
            base_size = f"{base_size:.{round_to}f}"
            
            print(f"placing limit buy: ${usd_per_order} (~{base_size} ${product_id}) @ ${price}")
        elif mode == "aggr":
            # print("aggr")
            # print(price)

            price_1x = price_high
            price_2x = price_high - price_range * 0.125   # 12.5% drop from high
            price_4x = price_high - price_range * 0.25    # 25% drop from high
            price_8x = price_high - price_range * 0.5     # 50% drop from high

            # print(price_1x)
            # print(price_2x)
            # print(price_4x)
            # print(price_8x)

            if price <= price_8x:
                # print("8x")
                # print(round((total_usd * 0.50) / number_of_orders, 2))
                usd_per_order = round((total_usd * 0.50) / number_of_orders, 2)
            elif price <= price_4x:
                # print("4x")
                # print(round((total_usd * 0.50 * 0.50) / number_of_orders, 2))
                usd_per_order = round((total_usd * 0.50 * 0.50) / number_of_orders, 2)
            elif price <= price_2x:
                # print("2x")
                # print(round((total_usd * 0.50 * 0.50 * 0.50) / number_of_orders, 2))
                usd_per_order = round((total_usd * 0.50 * 0.50 * 0.50) / number_of_orders, 2)
            elif price > price_2x:
                # print("1x")
                # print(round((total_usd * 0.50 * 0.50 * 0.50 * 0.50) / number_of_orders, 2))
                usd_per_order = round((total_usd * 0.50 * 0.50 * 0.50 * 0.50) / number_of_orders, 2)
            else:
                print("ERROR")
                sys.exit(1)

            base_size = round(usd_per_order / price, round_to)
            base_size = f"{base_size:.{round_to}f}"

            print(f"placing limit buy: ${usd_per_order} (~{base_size} ${product_id}) @ ${price}")

        # client.create_order(
        #     client_order_id=str(uuid.uuid4()),
        #     product_id=product_id,
        #     side="BUY",
        #     order_configuration={
        #         "limit_limit_gtc": {
        #             "base_size": str(base_size),
        #             "limit_price": str(price)
        #         }
        #     }
        # )

        price -= price_step
        price = round(price, 2)
        time.sleep(0.2) # rate limit

if __name__ == "__main__":
    main()