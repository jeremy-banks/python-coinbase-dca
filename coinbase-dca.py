#!/usr/bin/env python3

import sys
import time
import uuid
import argparse
from coinbase.rest import RESTClient

API_KEY = ""
API_SECRET = """"""

def handle_fail(error_message):
    print(error_message)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("underlying", nargs="?", default="")
    parser.add_argument("side", nargs="?", default="")
    parser.add_argument("mode", nargs="?", default="")
    parser.add_argument("price_start", nargs="?", type=float, default=0)
    parser.add_argument("price_end", nargs="?", type=float, default=0)
    parser.add_argument("price_step", nargs="?", type=float, default=0)
    parser.add_argument("total_amount", nargs="?", type=float, default=0)
    parser.add_argument("weighted_mod", nargs="?", type=float, default=0.95)

    args = parser.parse_args()

    underlying = args.underlying
    side = args.side
    mode = args.mode
    price_start = args.price_start
    price_end = args.price_end
    price_step = args.price_step
    total_amount = args.total_amount
    weighted_mod = args.weighted_mod

    match underlying:
        case "test":
            print(client.get_accounts())
            sys.exit(1)

        case ( "BTC-USD" | "LTC-USD" ):
            base_size_round_to = 8
            base_size_min = 0.00000001
            price_round_to = 2.0

        case ( "DOGE-USD" ):
            base_size_round_to = 1
            base_size_min = 0.1
            price_round_to = 5.0

        case "PUMP-USD":
            base_size_round_to = 0
            base_size_min = 1.0
            price_round_to = 6.0

        case _: handle_fail(f"Unsupported underlying: {underlying}")

    client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)

    order_delay = 0.34 # rate limiter

    price = price_start
    # print(price_start)

    price_range = 0
    match side:
        case "buy": price_range = price_start - price_end
        case "sell": price_range = price_end - price_start
        case _: handle_fail(f"Unsupported side: {side}")

    number_of_orders = int(price_range / price_step) + 1
    amount_per_order = total_amount / number_of_orders

    weighted_start_multiplier = 1 - weighted_mod
    weighted_end_multiplier = 1 + weighted_mod

    match side:
        case "buy":
            while price >= price_end:

                match mode:
                    case "flat":
                        base_size = round(amount_per_order / price, base_size_round_to)
                        order_amount = amount_per_order

                    case "weighted":
                        order_index = int((price_start - price) / price_step)

                        progress = order_index / (number_of_orders - 1)

                        multiplier = (
                            weighted_start_multiplier +
                            (weighted_end_multiplier - weighted_start_multiplier) * progress
                        )

                        order_amount = amount_per_order * multiplier

                        base_size = round(order_amount / price, base_size_round_to)

                    case _: handle_fail(f"Unsupported mode: {mode}")

                if base_size < base_size_min: handle_fail(f"base_size: {base_size} is smaller than base_size_min: {base_size_min}")

                print(f"{underlying} {side} {mode} {base_size:.{base_size_round_to}f} @ ${price} = ${base_size * price:.2f}")

                client.create_order(
                    client_order_id=str(uuid.uuid4()),
                    underlying=underlying,
                    side="BUY",
                    order_configuration={
                        "limit_limit_gtc": {
                            "base_size": str(base_size),
                            "limit_price": str(price)
                        }
                    }
                )

                price -= price_step
                price = round(price, int(price_round_to))
                time.sleep(order_delay)

        case "sell":
            while price <= price_end:

                match mode:
                    case "flat":
                        base_size = round(amount_per_order, base_size_round_to)
                        order_amount = amount_per_order

                    case "weighted":
                        order_index = int((price - price_start) / price_step)

                        progress = order_index / (number_of_orders - 1)

                        multiplier = (
                            weighted_start_multiplier +
                            (weighted_end_multiplier - weighted_start_multiplier) * progress
                        )

                        order_amount = amount_per_order * multiplier

                        base_size = round(order_amount, base_size_round_to)
                        
                    case _: handle_fail(f"Unsupported mode: {mode}")

                if base_size < base_size_min: handle_fail(f"base_size: {base_size} is smaller than base_size_min: {base_size_min}")

                print(f"{underlying} {side} {mode} {base_size:.{base_size_round_to}f} @ ${price} = ${base_size * price:.2f}")

                client.create_order(
                    client_order_id=str(uuid.uuid4()),
                    underlying=underlying,
                    side="SELL",
                    order_configuration={
                        "limit_limit_gtc": {
                            "base_size": str(base_size),
                            "limit_price": str(price)
                        }
                    }
                )

                price += price_step
                price = round(price, int(price_round_to))
                time.sleep(order_delay)

if __name__ == "__main__":
    main()