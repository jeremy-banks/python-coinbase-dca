# python-coinbase-dca

I built this script to quickly and easily take advantage of the volatility in crypto.

Specifically, I believe BTC will crash again as it did in Dec 2022, and I also believe it will reach a new all-time high relatively shortly thereafter. Everything I know about finance and economics says the best strategy for investing in a volatile asset is to use dollar cost averaging. There are two ways to achieve this: buy a little every day like Microstrategy and El Salvador, or set up limit buy orders in specific price steps to catch every valuation. Since I am not working with billions like MSTR and El Salvator, I have to use the second method.

This script features two modes for investment, flat and aggressive. Flat is just that: spending the same at each step. Aggressive is based on a geometric progression: spending more at lower steps.

```
python3 coinbase-dca.py BTC-USD flat 80000 1000 250 80
python3 coinbase-dca.py DOGE-USD flat 0.12 0.01 0.01 100
python3 coinbase-dca.py LTC-USD flat 70 5 5 50
```
The above example creates limit buy orders in BTC-USD, beginning at the $80,000 level and ending at the $1,000 level, and placing orders for $80 at each $250 step (80000, 79750, 79500, etc).

```
python3 coinbase-dca.py BTC-USD aggr 80000 22000 250 n
```
