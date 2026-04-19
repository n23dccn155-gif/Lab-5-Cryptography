from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, DES3, AES
import binascii

def generate_random_key(algorithm: str) -> str:
    """Trả về key dạng hex string"""
    if algorithm == "DES":
        key = get_random_bytes(8)
    elif algorithm == "3DES":
        key = get_random_bytes(24)
    elif algorithm == "AES":
        key = get_random_bytes(32)   # AES-256
    else:
        raise ValueError("Unsupported algorithm")
    return binascii.hexlify(key).decode('utf-8')

def symmetric_encrypt(algorithm: str, plaintext: str, key_hex: str, mode: str = "CBC") -> str:
    """Trả về ciphertext dạng hex"""
    ...

def symmetric_decrypt(algorithm: str, ciphertext_hex: str, key_hex: str, mode: str = "CBC") -> str:
    """Trả về plaintext"""
    ...