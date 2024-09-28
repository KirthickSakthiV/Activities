import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return (f"Block(Index: {self.index}, Data: {self.data}, "
                f"Previous Hash: {self.previous_hash}, Hash: {self.hash})")

# Create the genesis block (the first block in the blockchain)
genesis_block = Block(0, "0", "Genesis Block")
# Create subsequent blocks
block1 = Block(1, genesis_block.hash, "Block 1 Data")
block2 = Block(2, block1.hash, "Block 2 Data")
# Print the blocks
print(genesis_block)
print(block1)
print(block2)
