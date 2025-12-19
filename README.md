# python-coinbase-dca

I built this script to quickly and easily take advantage of the volatility in crypto.

Specifically, I believe BTC will crash again as it did in Dec 2022, and I also believe it will reach a new all-time high relatively shortly thereafter. Everything I know about finance and economics says the best strategy for investing in a volatile asset is to use dollar cost averaging. There are two ways to achieve this: buy a little every day like Microstrategy and El Salvador, or set up limit buy orders in specific price steps to catch every valuation. Since I am not working with billions like MSTR and El Salvator, I have to use the second method.

This script features two modes for investment, flat and aggressive. Flat is just that: spending the same at each step. Aggressive is based on a geometric progression: spending more at lower steps.

```
# create orders BTC-USD starting at $80,000 and ending at $22,000, at every $250 step, investing $1000
python3 coinbase-dca.py BTC-USD flat 80000 22000 250 1000

# create orders LTC-USD starting at $80,000 and ending at $22,000, at every $250 step, investing $1000
python3 coinbase-dca.py LTC-USD flat 70 20 5 1000

# create orders starting at $80,000 and ending at $22,000, at every $250 step, investing $20000
python3 coinbase-dca.py BTC-USD aggr 80000 22000 250 20000
```
