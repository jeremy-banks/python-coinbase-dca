#!/usr/bin/env python3

import sys
import time
import uuid
import argparse
from coinbase.rest import RESTClient

API_KEY = ""
API_SECRET = """"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("side", nargs="?", default="")
    parser.add_argument("product_id", nargs="?", default="")
    parser.add_argument("mode", nargs="?", default="")
    parser.add_argument("price_start", nargs="?", type=float, default=0)
    parser.add_argument("price_end", nargs="?", type=float, default=0)
    parser.add_argument("price_step", nargs="?", type=float, default=0)
    parser.add_argument("total_amount", nargs="?", type=float, default=0)
    parser.add_argument("aggr_mod", nargs="?", type=float, default=0)

    args = parser.parse_args()

    side = args.side
    product_id = args.product_id
    mode = args.mode
    price_start = args.price_start
    price_end = args.price_end
    price_step = args.price_step
    total_amount = args.total_amount
    aggr_mod = args.aggr_mod

    round_to_base_size = 8
    round_to_price = 2

    if product_id == "DOGE-USD":
        round_to_base_size = 1
        round_to_price = 5

    client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)

    if side == "test":
        print(client.get_accounts())
        sys.exit(1)

    price = price_start
    aggr_price_threshold_med = round(price_start + (price_end - price_start) * 0.33, round_to_price)
    aggr_price_threshold_low = round(price_start + (price_end - price_start) * 0.66, round_to_price)
    # print(price_start)
    # print(aggr_price_threshold_med)
    # print(aggr_price_threshold_low)

    if side == "buy":
        price_range = price_start - price_end
    elif side == "sell":
        price_range = price_end - price_start
    else:
        price_range = 0

    number_of_orders = int(price_range / price_step) + 1

    amount_per_order = total_amount / number_of_orders
    aggr_amount_per_order_high = amount_per_order * 1.34
    aggr_amount_per_order_med = amount_per_order
    aggr_amount_per_order_low = amount_per_order * 0.66
    # print(aggr_amount_per_order_high)
    # print(aggr_amount_per_order_med)
    # print(aggr_amount_per_order_low)

    if side == "buy":

        while price >= price_end:

            if mode == "flat":
                base_size = round(amount_per_order / price, round_to_base_size)

            elif mode == "aggr":
                if price >= aggr_price_threshold_med:
                    amount_per_order = round(aggr_amount_per_order_low, round_to_price)
                elif price <= aggr_price_threshold_low:
                    amount_per_order = round(aggr_amount_per_order_high, round_to_price)
                else:
                    amount_per_order = round(aggr_amount_per_order_med, round_to_price)

                base_size = round(amount_per_order / price, round_to_base_size)

            base_size = f"{base_size:.{round_to_base_size}f}"

            print(f"placing limit buy: ${round(amount_per_order, 2)} (~{base_size} ${product_id}) @ ${price}")

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
            price = round(price, round_to_price)
            time.sleep(0.2) # rate limit

    elif side == "sell":

        while price <= price_end:

            if mode == "flat":
                base_size = round(amount_per_order, round_to_base_size)

            elif mode == "aggr":
                if price <= aggr_price_threshold_med:
                    amount_per_order = round(aggr_amount_per_order_low, round_to_base_size)
                elif price >= aggr_price_threshold_low:
                    amount_per_order = round(aggr_amount_per_order_high, round_to_base_size)
                else:
                    amount_per_order = round(aggr_amount_per_order_med, round_to_base_size)

                base_size = round(amount_per_order, round_to_base_size)

            base_size = f"{base_size:.{round_to_base_size}f}"

            print(f"placing limit sell: ${round(amount_per_order * price, 2)} (~{base_size} ${product_id}) @ ${price}")

            # client.create_order(
            #     client_order_id=str(uuid.uuid4()),
            #     product_id=product_id,
            #     side="SELL",
            #     order_configuration={
            #         "limit_limit_gtc": {
            #             "base_size": str(base_size),
            #             "limit_price": str(price)
            #         }
            #     }
            # )

            price += price_step
            price = round(price, round_to_price)
            time.sleep(0.2) # rate limit

if __name__ == "__main__":
    main()