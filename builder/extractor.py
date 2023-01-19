import asyncio
import json
from web3 import Web3
from websockets import connect

from utils import get_contract

ws_url = 'wss://eth-mainnet.g.alchemy.com/v2/7hOvTTdNWW7ngDBuxt0RI4h91giaqhxP'
http_url = 'https://eth-mainnet.g.alchemy.com/v2/7hOvTTdNWW7ngDBuxt0RI4h91giaqhxP'
web3 = Web3(Web3.HTTPProvider(http_url))

USDC_TRANSFER = '{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["logs", {"address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "topics": ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"]}]}'

async def get_event():
    async with connect(ws_url) as ws:
        await ws.send(USDC_TRANSFER)
        subscription_response = await ws.recv()
        print(subscription_response)

        while True:
            message = await asyncio.wait_for(ws.recv(), timeout=15)
            response = json.loads(message)

            receipt = response['params']['result']
            address = Web3.toChecksumAddress(receipt['address'])
            contract = get_contract(address)

            receipt = web3.eth.getTransactionReceipt(receipt['transactionHash'])

            logs = contract.events.Transfer().processReceipt(receipt)
            print('logs', logs)

            # extracted.append({
            #     "address": event.address,
            #     "receipt": receipt
            # })
            # print(tx)
            # if tx.to == account:
            #     print("Pending transaction found with the following details:")
            #     print({
            #         "hash": txHash,
            #         "from": tx["from"],
            #         "value": web3.fromWei(tx["value"], 'ether')
            #     })

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(get_event())