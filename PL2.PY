import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()
    
if __name__ == "__main__":
    # Create the genesis block
    genesis_block = Block(
        index = 0,
        timestamp = "2025-01-28 12:04:00",
        data = "Genesis block data",
        previous_hash = "0"
    )

    print("Genesis Block: ")
    print(f"Index: {genesis_block.index}")
    print(f"Timestamp: {genesis_block.timestamp}")
    print(f"Data: {genesis_block.data}")
    print(f"Previous Hash: {genesis_block.previous_hash}")
    print(f"Hash: {genesis_block.hash}")
