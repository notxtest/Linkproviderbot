import os

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")

ADMINS = [
    int(x.strip())
    for x in os.getenv("ADMINS", "").split(",")
    if x.strip()
]

START_PIC = os.getenv("START_PIC", "https://graph.org/file/9b84ec73a967e27c15de9-d1e9e4da7828acaedc.jpg")
LINK_PIC = os.getenv("LINK_PIC", "https://graph.org/file/3106ef9a5e09dd9f94500-b6461844ac16ddb6c7.jpg")
