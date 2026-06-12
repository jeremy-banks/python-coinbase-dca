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

### Buy

create orders to buy BTC-USD starting at $100,000 and ending at $25,000, at every $250 step, investing $1,000 total

```python3 coinbase-dca.py buy BTC-USD flat 100000 25000 250 1000```

create orders to buy LTC-USD starting at $70 and ending at $20, at every $5 step, investing $1,000 total

```python3 coinbase-dca.py buy LTC-USD flat 70 20 5 1000```

create orders to buy BTC-USD starting at $69,000 and ending at $17,500, at every $250 step, investing $20,000 total

```python3 coinbase-dca.py buy BTC-USD aggr 69000 17500 250 20000```

### Sell

create orders selling BTC-USD starting at $100,000 and ending at $300,000, at every $250 step, selling $1,000 total

```python3 coinbase-dca.py sell BTC-USD flat 100000 300000 250 1000```

create orders selling LTC-USD starting at $20 and ending at $70, at every $5 step, selling $1,000 total

```python3 coinbase-dca.py sell LTC-USD flat 20 70 5 1000```

create orders selling BTC-USD starting at $16,000 and ending at $69,000, at every $250 step, selling $20,000 total

```python3 coinbase-dca.py sell BTC-USD aggr 16000 69000 250 20000```
