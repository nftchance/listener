from .utils import get_contract, get_w3

w3 = get_w3()

contracts = [
    "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "0xdAC17F958D2ee523a2206206994597C13D831ec7"
]

topics = [
    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
]

filter = w3.eth.filter({
    "address": contracts,
    "topics": topics
})

def extract(w3):
    extracted = []

    events = filter.get_new_entries()

    if events:
        for event in events:
            receipt = w3.eth.getTransactionReceipt(event.transactionHash)

            extracted.append({
                "address": event.address,
                "receipt": receipt
            })

    return extracted