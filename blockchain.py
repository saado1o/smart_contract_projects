import hashlib
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = {
            'index': 0,
            'timestamp': datetime.now(),
            'transactions': [],
            'previous_hash': '0' * 64  # Genesis block with no previous hash
        }
        self.chain.append(genesis_block)

    def add_transaction(self, sender, receiver, amount, remarks):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'remarks': remarks,
            'timestamp': datetime.now()  # Capture current time as datetime object
        }
        self.chain.append(transaction)
        return transaction

    def get_chain(self):
        return self.chain
