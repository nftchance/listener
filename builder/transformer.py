from .utils import get_contract

def transform(extraction):
    transformation = []

    for event in extraction:
        contract = get_contract(event['address'])

        logs = contract.events.Transfer().processReceipt(event['receipt'])

        transformation.append(logs)

    return transformation