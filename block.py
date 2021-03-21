from datetime import datetime
from hashlib import sha256


class Block:
    def __init__(self, transactions, previous_hash, nonce=0):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.time_stamp = datetime.now()
        self.hash = self.generate_hash()

    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)

    def generate_hash(self):
        block_contents = str(
            self.time_stamp) + str(self.transactions) + str(self.nonce) + str(self.previous_hash)

        block_hash = sha256(block_contents.encode())

        return block_hash.hexdigest()
