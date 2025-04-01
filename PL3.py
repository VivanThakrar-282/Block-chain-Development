import hashlib
import datetime
import time

class Block:
    def __init__(self, index, previous_hash, transactions, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    def mine_block(self):
        # Find a hash that satisfy the difficult condition of (pow Algorithm)#
        while True:
            hash_value = self.compute_hash()
            if hash_value[:self.difficulty] == '0'*self.difficulty:
                return hash_value #find valid hash
            self.nonce = self.nonce + 1

    def compute_hash(self):
        # compute the hash of block's content
        block_content = f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()
    
transactions = "vivan pays 100 BTC to sunil"
gensis_block = Block(0,"0",transactions,difficulty=4)

print(f"Block Mined Hash: {gensis_block.hash}")
print(f"Nonce: {gensis_block.nonce}")

