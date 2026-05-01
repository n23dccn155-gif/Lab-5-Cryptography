from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


def generate_rsa_key_pair(key_size: int = 2048) -> tuple[str, str]:
    key = RSA.generate(key_size)

    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()

    return public_key, private_key


def rsa_encrypt(plaintext: str, public_key_pem: str) -> str:
    try:
        rsa_key = RSA.import_key(public_key_pem)
        cipher = PKCS1_OAEP.new(rsa_key)

        ciphertext = cipher.encrypt(plaintext.encode())
        return binascii.hexlify(ciphertext).decode()

    except Exception as e:
        return f"Error: {str(e)}"

def rsa_decrypt(ciphertext_hex: str, private_key_pem: str) -> str:
    try:
        rsa_key = RSA.import_key(private_key_pem)
        cipher = PKCS1_OAEP.new(rsa_key)

        decoded_data = binascii.unhexlify(ciphertext_hex)
        plaintext = cipher.decrypt(decoded_data)

        return plaintext.decode()

    except Exception as e:
        return f"Error: {str(e)}"