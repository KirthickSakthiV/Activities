from ecdsa import SigningKey, VerifyingKey, SECP256k1

def generate_keys():
    # Generate a new private key
    private_key = SigningKey.generate(curve=SECP256k1)
    # Get the corresponding public key
    public_key = private_key.get_verifying_key()
    # Serialize keys to PEM format
    private_key_pem = private_key.to_pem()
    public_key_pem = public_key.to_pem()
    # Save the keys to files
    with open("private_key.pem", "wb") as f:
        f.write(private_key_pem)
    with open("public_key.pem", "wb") as f:
        f.write(public_key_pem)
    print("Keys generated and saved to files.")

def load_keys():
    # Load private key from PEM file
    with open("private_key.pem", "rb") as f:
        private_key = SigningKey.from_pem(f.read())
    # Load public key from PEM file
    with open("public_key.pem", "rb") as f:
        public_key = VerifyingKey.from_pem(f.read())
    print("Private key:", private_key.to_string().hex())
    print("Public key:", public_key.to_string().hex())

if __name__ == "__main__":
    generate_keys()
    load_keys()
