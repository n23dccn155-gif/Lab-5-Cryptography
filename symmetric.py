from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, DES3, AES
from Crypto.Util.Padding import pad, unpad
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
    key_hex = key_hex.replace(" ", "").strip()
    key = binascii.unhexlify(key_hex)
    pt_bytes = plaintext.encode('utf-8')
    
    if algorithm == "DES":
        cipher_module = DES
    elif algorithm == "3DES":
        cipher_module = DES3
    elif algorithm == "AES":
        cipher_module = AES
    else:
        raise ValueError("Unsupported algorithm")
        
    block_size = cipher_module.block_size
    
    if mode == "CBC":
        cipher = cipher_module.new(key, cipher_module.MODE_CBC)
        iv = cipher.iv
    elif mode == "ECB":
        cipher = cipher_module.new(key, cipher_module.MODE_ECB)
        iv = b""
    else:
        raise ValueError("Unsupported mode. Please use 'CBC' or 'ECB'.")
        
    # Encrypt with padding to meet block size requirements
    ct_bytes = cipher.encrypt(pad(pt_bytes, block_size))
    # Prepend IV (if CBC) to ciphertext before returning as hex
    return binascii.hexlify(iv + ct_bytes).decode('utf-8')

def symmetric_decrypt(algorithm: str, ciphertext_hex: str, key_hex: str, mode: str = "CBC") -> str:
    """Trả về plaintext"""
    key_hex = key_hex.replace(" ", "").strip()
    ciphertext_hex = ciphertext_hex.replace(" ", "").strip()
    
    key = binascii.unhexlify(key_hex)
    data = binascii.unhexlify(ciphertext_hex)
    
    if algorithm == "DES":
        cipher_module = DES
    elif algorithm == "3DES":
        cipher_module = DES3
    elif algorithm == "AES":
        cipher_module = AES
    else:
        raise ValueError("Unsupported algorithm")
        
    block_size = cipher_module.block_size
    
    if mode == "CBC":
        iv = data[:block_size]
        ct = data[block_size:]
        cipher = cipher_module.new(key, cipher_module.MODE_CBC, iv)
    elif mode == "ECB":
        ct = data
        cipher = cipher_module.new(key, cipher_module.MODE_ECB)
    else:
        raise ValueError("Unsupported mode. Please use 'CBC' or 'ECB'.")
        
    try:
        pt = unpad(cipher.decrypt(ct), block_size)
        return pt.decode('utf-8')
    except ValueError:
        raise ValueError("Lỗi: Sai khóa, sai mode hoặc dữ liệu Ciphertext đã bị thay đổi (corrupted)!")
