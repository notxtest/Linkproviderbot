import base64

def encode_channel_id(channel_id: int) -> str:
    return base64.urlsafe_b64encode(str(channel_id).encode()).decode()

def decode_channel_id(encoded: str) -> int:
    return int(base64.urlsafe_b64decode(encoded.encode()).decode())
