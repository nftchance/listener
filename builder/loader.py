# AttributeDict({'args': AttributeDict({'from': '0xcca169D1Ec38D4e216036e92082B6E8cb31e96Db', 'to': '0xCCF4Aed18269c27Ab7f649E8b30Bfe6AFe8a72d2', 'value': 9819000000}), 'event': 'Transfer', 'logIndex': 492, 'transactionIndex': 172, 'transactionHash': HexBytes('0x4a51d732dd271a6687c9359b65f2d97eda56617dccd857b5b0ab60fd79cf18b4'), 'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7', 'blockHash': HexBytes('0x1e73b6c8615fda7238daf01a7c0bea5a6277d5e8828f1180b1ef39c8473f2a55'), 'blockNumber': 16436368})

def load(transformation):
    # Loop through every receipt that we have -- one may have more than one event.
    for receipt in transformation:

        # Loop through all of the events in each receipt.
        for log in receipt:
            print(log.blockNumber)
            # print(log.address)
            # print(log.args)

            # TODO: use the name of the event to send them to the right place.