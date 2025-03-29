import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1

def sha256_hash (data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# Generate ECDSA keys
private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.get_verifying_key()

transactions_data = "vivan sends 12 BTC to Abhishek"

hashed_data = sha256_hash(transactions_data)
print("Hashed Data:", hashed_data)

#Sign the hashed data with private key
signature = private_key.sign(hashed_data.encode())
print("Signature:", signature.hex())

#verify the signature using public key
is_valid = public_key.verify(signature, hashed_data.encode())
print("is Signature valid?", is_valid)

