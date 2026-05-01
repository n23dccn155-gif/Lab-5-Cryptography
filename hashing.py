import hashlib

def md5_hash(text):
    # Mã hóa chuỗi đầu vào thành định dạng bytes và băm bằng thuật toán MD5
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def sha256_hash(text):
    # Mã hóa chuỗi đầu vào thành định dạng bytes và băm bằng thuật toán SHA-256
    return hashlib.sha256(text.encode('utf-8')).hexdigest()