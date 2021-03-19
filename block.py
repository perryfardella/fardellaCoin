from datetime import datetime
from hashlib import sha256


class Block:
    def __init__(self, transactions, previous_hash, nonce=0):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = datetime.now()

    def print_block(self):
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())

    def generate_hash(self):
        block_contents = str(
            self.timestamp) + str(self.transactions) + str(self.nonce) + str(self.previous_hash)
        return block_contents
