# python-coinbase-dca

I built this script to take advantage of the volatility in crypto.

Specifically, I believe BTC will crash again as it did in Dec 2022, I also believe it will reach a new all-time high relatively shortly thereafter, and I believe it will continue to be a volatile asset in the future. Everything I know about finance and economics says the best strategy for investing in a volatile asset is to use **dollar cost averaging**.

There are two ways to achieve this: buy a little every day like Microstrategy and El Salvador, or set up limit buy orders in specific price steps to catch every valuation. Since I am not working with billions like MSTR and El Salvator I have to use the second method.

This script features entering buy and sell orders on Coinbase. Those orders can be "flat" where each order is the same volume of coin, or "weighted" where order volumes follow a linear gradient ±95% of the baseline volume across the order sequence. This script is only tested with BTC-USD, DOGE-USD, LTC-USD and PUMP-USD.

***USE THIS SCRIPT AT YOUR OWN RISK!!!***

## Set Up

Install Python Libraries
```
pip install coinbase-advanced-py
python3 -m pip install coinbase-advanced-py --break-system-packages
```

Generate a ***ECDSA*** Coinbase API key with read and order submission rights.

Paste the API Key name from Coinbase into script API_KEY
Paste Private key from Coinbase into script API_SECRET
```
API_KEY = "organizations/{org_id}/apiKeys/{key_id}"
API_SECRET = """-----BEGIN EC PRIVATE KEY-----\nYOUR PRIVATE KEY\n-----END EC PRIVATE KEY-----\n"""
```

### Test

`python3 coinbase-dca.py test`

Output should dump a list of accounts.

## Usage

### BTC-USD

create orders for <ins>BTC-USD</ins> to <ins>buy</ins> starting at <ins>$100,000</ins> and ending at <ins>$10,000</ins>, at every <ins>$1,000</ins> step, spending <ins>$1,000</ins> total

```python3 coinbase-dca.py BTC-USD buy flat 100000 10000 10000 1000```

```python3 coinbase-dca.py BTC-USD buy weighted 100000 10000 10000 1000```

create orders for <ins>BTC-USD</ins> to <ins>sell</ins> starting at <ins>$100,000</ins> and ending at <ins>$1,000,000</ins>, at every <ins>$100,000</ins> step, selling <ins>1</ins> BTC total

```python3 coinbase-dca.py BTC-USD sell flat 100000 1000000 100000 1```

```python3 coinbase-dca.py BTC-USD sell weighted 100000 1000000 100000 1```

Note that BTC-USD and LTC-USD orders can be placed to the hundred-millionth place ```0.0000000n```

```python3 coinbase-dca.py LTC-USD sell flat 100 1000 100 114.07908907```

However some coins like DOGE-USD only support tens place 0.1

```python3 coinbase-dca.py DOGE-USD sell flat 1 10 1 10000.5```

## To-Do

1. N/A