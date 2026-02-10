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
    parser.add_argument("total_usd", nargs="?", type=float, default=0)
    parser.add_argument("aggr_mod", nargs="?", type=float, default=0)

    args = parser.parse_args()

    side = args.side
    product_id = args.product_id
    mode = args.mode
    price_start = args.price_start
    price_end = args.price_end
    price_step = args.price_step
    total_usd = args.total_usd
    aggr_mod = args.aggr_mod

    round_to = 8

    client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)

    if side == "test":
        print(client.get_accounts())
        sys.exit(1)

    price = price_start
    aggr_price_threshold_med = round(price_start + (price_end - price_start) * 0.66, 2)
    aggr_price_threshold_low = round(price_start + (price_end - price_start) * 0.33, 2)

    print(price_start)
    print(aggr_price_threshold_med)
    print(aggr_price_threshold_low)

    if side == "buy":
        price_range = price_start - price_end
        number_of_orders = round(price_range / price_step)

        # print(price_range)

        usd_per_order = round(total_usd / number_of_orders, 2)
        aggr_usd_per_order_high = round(usd_per_order * 1.34, 2)
        aggr_usd_per_order_med = usd_per_order
        aggr_usd_per_order_low = round(usd_per_order * 0.66, 2)

        print(aggr_usd_per_order_high)
        print(aggr_usd_per_order_med)
        print(aggr_usd_per_order_low)

        while price >= price_end:

            if mode == "flat":
                base_size = round(usd_per_order / price, round_to)
                base_size = f"{base_size:.{round_to}f}"
                
                print(f"placing limit buy: ${usd_per_order} (~{base_size} ${product_id}) @ ${price}")

            elif mode == "aggr":
                if price > aggr_price_threshold_med:
                    usd_per_order = aggr_usd_per_order_low
                elif price <= aggr_price_threshold_low:
                    usd_per_order = aggr_usd_per_order_high
                else:
                    usd_per_order = aggr_usd_per_order_med

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

    elif side == "sell":
        price_range = price_end - price_start
        number_of_orders = round(price_range / price_step)

        # print(price_range)

        # price = price_start
        # aggr_price_threshold_med = round(price_start + (price_end - price_start) * 0.66, 2)
        # aggr_price_threshold_low = round(price_start + (price_end - price_start) * 0.33, 2)

        # print(price)
        # print(aggr_price_threshold_med)
        # print(aggr_price_threshold_low)

        usd_per_order = round(total_usd / number_of_orders, 2)
        aggr_usd_per_order_high = round(usd_per_order * 1.34, 2)
        aggr_usd_per_order_med = usd_per_order
        aggr_usd_per_order_low = round(usd_per_order * 0.66, 2)

        print(aggr_usd_per_order_high)
        print(aggr_usd_per_order_med)
        print(aggr_usd_per_order_low)

        # print(aggr_usd_per_order_med)

        while price <= price_end:

            if mode == "flat":
                base_size = round(usd_per_order / price, round_to)
                base_size = f"{base_size:.{round_to}f}"
                
                print(f"placing limit sell: ${usd_per_order} (~{base_size} ${product_id}) @ ${price}")

            elif mode == "aggr":
                if price < aggr_price_threshold_low:
                    usd_per_order = aggr_usd_per_order_low
                elif price >= aggr_price_threshold_med:
                    usd_per_order = aggr_usd_per_order_high
                else:
                    usd_per_order = aggr_usd_per_order_med

                base_size = round(usd_per_order / price, round_to)
                base_size = f"{base_size:.{round_to}f}"

                print(f"placing limit sell: ${usd_per_order} (~{base_size} ${product_id}) @ ${price}")

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

            price += price_step
            price = round(price, 2)
            time.sleep(0.2) # rate limit

if __name__ == "__main__":
    main()