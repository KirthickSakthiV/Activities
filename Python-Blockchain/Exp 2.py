import hashlib
def hash_data_sha256(data):
  # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()
  # Update the hash object with the data (must be encoded to bytes)
    sha256.update(data.encode('utf-8'))
  # Retrieve the hexadecimal representation of the hash
    return sha256.hexdigest()
# Example usage
data = "Hello, World!"
hashed_data = hash_data_sha256(data)
print(f"Original Data: {data}")
print(f"SHA-256 Hash: {hashed_data}")
