import hashlib

def generate_device_id(current_device_id):
    # Example using SHA-256
    hash_object = hashlib.sha256(current_device_id.encode())
    return hash_object.hexdigest()[:16]  # Assuming a truncated version is used

current_device_id = "5187F3F7-D934-4679-86C7-49EDD7EA5176"
device_id = generate_device_id(current_device_id)
print(f"Device ID: {device_id}")