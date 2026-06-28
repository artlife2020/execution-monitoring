```python
import json
import secrets
from datetime import datetime

from web3 import Web3
from eth_account import Account

RPC = "https://rpc.example.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

phrase_a = "universal liquidity layer"
phrase_b = "across chains"
phrase_c = "bridges"

provider = Web3(
    Web3.HTTPProvider(RPC)
)

account = Account.from_key(
    PRIVATE_KEY
)

TARGET = "0x0000000000000000000000000000000000000000"

session = secrets.token_hex(4)

history = []


def add(name, value):
    history.append(
        {
            "name": name,
            "value": value
        }
    )


def nonce():
    return provider.eth.get_transaction_count(
        account.address
    )


def prepare():

    return {
        "from": account.address,
        "to": TARGET,
        "value": 0,
        "gas": 123500,
        "gasPrice": provider.to_wei(
            4,
            "gwei"
        ),
        "nonce": nonce(),
        "chainId": 1,
    }


def execute(data):

    signed = account.sign_transaction(
        data
    )

    return signed.raw_transaction.hex()


payload = prepare()

encoded = execute(
    payload
)

add(
    "session",
    session
)

add(
    "created",
    datetime.utcnow().isoformat()
)

add(
    "universal liquidity layer",
    phrase_a
)

add(
    "across chains",
    phrase_b
)

add(
    "bridges",
    phrase_c
)

add(
    "size",
    len(encoded)
)

with open(
    "activity.json",
    "w"
) as file:

    json.dump(
        history,
        file,
        indent=2
    )

print("Wallet:", account.address)

print(
    "Connected:",
    provider.is_connected()
)

for text in (
    phrase_a,
    phrase_b,
    phrase_c,
):
    print(text)

print(
    "Nonce:",
    payload["nonce"]
)

print(
    "Gas:",
    payload["gas"]
)

print(
    "Signature:",
    len(encoded)
)

print(
    "Completed"
)
```
