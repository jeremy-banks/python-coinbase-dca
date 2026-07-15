# python-coinbase-dca

I built this script to quickly and easily take advantage of the volatility in crypto.

Specifically, I believe BTC will crash again as it did in Dec 2022, and I also believe it will reach a new all-time high relatively shortly thereafter. Everything I know about finance and economics says the best strategy for investing in a volatile asset is to use dollar cost averaging. There are two ways to achieve this: buy a little every day like Microstrategy and El Salvador, or set up limit buy orders in specific price steps to catch every valuation. Since I am not working with billions like MSTR and El Salvator, I have to use the second method.

I wrote that in Dec, and am updating this script in Feb after the dip to 60k. This script worked exactly as intended. I am revising the script and documentation deciding to invest even more in this current dip. I believe BTC will continue to occilate, and I plan to use this script to exploit each opportunity.

## WARNING

Only tested with BTC-USD, LTC-USD and DOGE-USD. ***USE AT YOUR OWN RISK!!!***

## Set Up

Install Python Libraries
```
pip install coinbase-advanced-py
python3 -m pip install coinbase-advanced-py --break-system-packages
```

Generate a Coinbase API key with read and order submission rights.

Paste the API Key name from Coinbase into script API_KEY
Paste Private key from Coinbase into script API_SECRET
```
API_KEY = "organizations/{org_id}/apiKeys/{key_id}"
API_SECRET = """-----BEGIN EC PRIVATE KEY-----\nYOUR PRIVATE KEY\n-----END EC PRIVATE KEY-----\n"""
```

## Usage

### Test

```
python3 coinbase-dca.py test
```

Output should dump a list of accounts.

### Placing Orders

#### BTC-USD
create orders to buy BTC-USD starting at $100,000 and ending at $10,000, at every $1,000 step, spending $1,000 total

```python3 coinbase-dca.py buy BTC-USD flat 100000 10000 10000 1000```

create orders selling BTC-USD starting at $100,000 and ending at $1,000,000, at every $100,000 step, selling 1.00470762 BTC total

```python3 coinbase-dca.py sell BTC-USD flat 100000 1000000 100000 1.00470762```

#### DOGE-USD
create orders to buy DOGE-USD starting at $0.50 and ending at $0.05, at every $0.05 step, spending $1,000 total

```python3 coinbase-dca.py buy DOGE-USD flat 0.5 0.05 0.05 1000```

create orders selling DOGE-USD starting at $1.00 and ending at $10.00, at every $1.00 step, selling 10000.5 DOGE total

```python3 coinbase-dca.py sell DOGE-USD flat 1 10 1 10000.5```

#### LTC-USD
create orders to buy LTC-USD starting at $100 and ending at $10, at every $10 step, spending $1,000 total

```python3 coinbase-dca.py buy LTC-USD flat 100 10 10 1000```

create orders selling LTC-USD starting at $100 and ending at $1000, at every $100 step, selling 114.07908907 LTC total

```python3 coinbase-dca.py sell LTC-USD flat 100 1000 100 114.07908907```

### Flat vs Aggr
This script features two modes of buying and selling: flat and aggresive. Flat means every buy or sell order is for the same amount, for example $100. Aggressive modifies prices of each order using the gradient multiplier default of 0.5 to 1.5

```
python3 coinbase-dca.py buy BTC-USD aggr 100000 10000 15000 1000
placing limit buy: $71.43 (~0.00071429 $BTC-USD) @ $100000.0
placing limit buy: $95.24 (~0.00112045 $BTC-USD) @ $85000.0
placing limit buy: $119.05 (~0.00170068 $BTC-USD) @ $70000.0
placing limit buy: $142.86 (~0.00259740 $BTC-USD) @ $55000.0
placing limit buy: $166.67 (~0.00416667 $BTC-USD) @ $40000.0
placing limit buy: $190.48 (~0.00761905 $BTC-USD) @ $25000.0
placing limit buy: $214.29 (~0.02142857 $BTC-USD) @ $10000.0
```
