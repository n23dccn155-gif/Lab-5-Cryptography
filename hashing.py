import hashlib

def generate_md5(text):
    # Mã hóa chuỗi đầu vào thành định dạng bytes và băm bằng thuật toán MD5
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def generate_sha256(text):
    # Mã hóa chuỗi đầu vào thành định dạng bytes và băm bằng thuật toán SHA-256
    return hashlib.sha256(text.encode('utf-8')).hexdigest()