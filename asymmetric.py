from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generate_rsa_key_pair(key_size: int = 2048) -> tuple[str, str]:
    """Trả về (public_pem, private_pem)"""
    ...

def rsa_encrypt(plaintext: str, public_key_pem: str) -> str:
    """Trả về ciphertext hex"""

def rsa_decrypt(ciphertext_hex: str, private_key_pem: str) -> str:
    ...