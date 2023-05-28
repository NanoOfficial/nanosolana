# nanosolana
Solana Python SDK

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# About:
- Easy to use solana python SDK.

# Installation:
## Installing using pip
```
pip install git+https://github.com/NanoOfficial/nanosolana@main
```

## Client:
```python
from nanosolana import Client

myClient = Client("https://api.devnet.solana.com")
```

## Usage example:
```python
from nanosolana import Client, PublicKey

myClient = Client("url")
public_key = PublicKey("publicKey")

balance = myClient.get_balance(public_key)
print(balance)
```