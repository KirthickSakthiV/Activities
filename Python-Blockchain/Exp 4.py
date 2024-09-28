import hashlib
import time

class ProofOfWork:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def mine(self, block_data):
        nonce = 0
        start_time = time.time()
        while True:
            candidate_block = f"{block_data}{nonce}".encode()
            hash_result = hashlib.sha256(candidate_block).hexdigest()
            if hash_result.startswith('0' * self.difficulty):
                end_time = time.time()
                return nonce, hash_result, end_time - start_time
            nonce += 1

# Example usage
if __name__ == "__main__":
    difficulty = 4  # Difficulty target (number of leading zeros)
    block_data = "This is some block data"
    pow_system = ProofOfWork(difficulty)
    nonce, hash_result, time_taken = pow_system.mine(block_data)
    
    print(f"Block Data: {block_data}")
    print(f"Nonce: {nonce}")
    print(f"Hash Result: {hash_result}")
    print(f"Time Taken: {time_taken:.2f} seconds")
