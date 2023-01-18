from web3 import Web3

abi = [{
    "anonymous": False,
    "inputs": [
        {
            "indexed": True,
            "internalType": "address",
            "name": "from",
            "type": "address"
        },
        {
            "indexed": True,
            "internalType": "address",
            "name": "to",
            "type": "address"
        },
        {
            "indexed": False,
            "internalType": "uint256",
            "name": "value",
            "type": "uint256"
        }
    ],
    "name": "Transfer",
    "type": "event"
}]

connected_contracts = {}

RPC = "https://eth-mainnet.g.alchemy.com/v2/7hOvTTdNWW7ngDBuxt0RI4h91giaqhxP"
w3 = Web3(Web3.HTTPProvider(RPC))

def get_w3():
    return w3

def get_contract(address):
    if address not in connected_contracts:
        connected_contracts[address] = w3.eth.contract(address=address, abi=abi)

    return connected_contracts[address]