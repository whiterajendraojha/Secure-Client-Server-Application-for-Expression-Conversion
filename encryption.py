from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 32-byte AES key (for 256-bit encryption)
KEY = b'0123456789abcdef0123456789abcdef'

# Encrypt message using AES encryption
def encrypt_message(message):
    cipher = AES.new(KEY, AES.MODE_CBC)  # Create AES cipher in CBC mode
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')  # Encode IV
    ct = base64.b64encode(ct_bytes).decode('utf-8')  # Encode ciphertext
    return iv + ct

# Decrypt message using AES encryption
def decrypt_message(encrypted_message):
    iv = base64.b64decode(encrypted_message[:24])  # First 24 characters = IV
    ct = base64.b64decode(encrypted_message[24:])  # Remaining characters = Ciphertext
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')  # Remove padding
    return pt
