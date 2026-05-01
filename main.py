import sys
import os
from symmetric import generate_random_key, symmetric_encrypt, symmetric_decrypt
from asymmetric import generate_rsa_key_pair, rsa_encrypt, rsa_decrypt
from hashing import md5_hash, sha256_hash
from utils import print_error, bao_ok

def copy_to_clipboard(text):
    """Sao chép text vào clipboard trên Windows"""
    try:
        os.system(f'echo {text}| clip')
        print(" [OK] Đã sao chép vào Clipboard!")
    except Exception:
        print(" [!] Không thể sao chép tự động. Hãy bôi đen để copy thủ công.")

def ket_qua_menu(result_text):
    """Menu hiển thị kết quả và các tùy chọn Copy/Try Again/Back"""
    print("\n" + "-"*30)
    print(" KẾT QUẢ:")
    print(result_text)
    print("-"*30)
    
    while True:
        print("\n1. Copy kết quả")
        print("2. Thử lại (Lượt mới)")
        print("3. Quay lại Menu chính")
        c = input("Lựa chọn (1-3): ").strip()
        
        if c == "1":
            copy_to_clipboard(result_text)
        elif c == "2":
            return "retry"
        elif c == "3":
            return "back"
        else:
            print(" Lựa chọn không hợp lệ!")

def main_menu():
    while True:
        print("\n" + "="*55)
        print(" CRYPTOGRAPHY TOOLKIT")
        print("="*55)
        print("1. Symmetric Encryption (DES / 3DES / AES)")
        print("2. Asymmetric Encryption (RSA)")
        print("3. Hash Functions (MD5 / SHA-256)")
        print("4. Thoát chương trình")
        print("="*55)
        
        choice = input("Nhập lựa chọn (1-4): ").strip()
        
        if choice == "1":
            symmetric_menu()
        elif choice == "2":
            asymmetric_menu()
        elif choice == "3":
            hash_menu()
        elif choice == "4":
            print(" Cảm ơn bạn đã sử dụng chương trình!")
            sys.exit(0)
        else:
            print(" Lựa chọn không hợp lệ! Vui lòng nhập số từ 1-4.")

# ==================== SYMMETRIC MENU ====================
def symmetric_menu():
    while True:
        print("\n--- Symmetric Encryption ---")
        print("1. DES")
        print("2. 3DES")
        print("3. AES")
        print("0. Quay lại")
        alg_choice = input("Chọn thuật toán (0-3): ").strip()
        
        if alg_choice == "0": break
        algorithm = {"1": "DES", "2": "3DES", "3": "AES"}.get(alg_choice)
        if not algorithm:
            print(" Lựa chọn không hợp lệ!")
            continue

        print("\n1. CBC (Khuyên dùng)")
        print("2. ECB (Cơ bản)")
        mode_choice = input("Chọn chế độ (1-2): ").strip()
        mode = "CBC" if mode_choice == "1" else "ECB"

        print("\n1. Mã hóa (Encrypt)")
        print("2. Giải mã (Decrypt)")
        action = input("Chọn chức năng (1-2): ").strip()

        while True:
            try:
                if action == "1":  # Encrypt
                    plaintext = input("\nNhập Plaintext: ").strip()
                    print("1. Nhập key thủ công (Hex)\n2. Tự sinh key ngẫu nhiên")
                    key_choice = input("Chọn (1-2): ").strip()
                    
                    if key_choice == "2":
                        key_hex = generate_random_key(algorithm)
                        print(f" Key ngẫu nhiên (hex): {key_hex}")
                    else:
                        key_hex = input("Nhập Secret Key (hex): ").strip()
                    
                    result = symmetric_encrypt(algorithm, plaintext, key_hex, mode)
                    msg = f"Ciphertext [{mode}] (hex): {result}"
                else:  # Decrypt
                    ciphertext = input("\nNhập Ciphertext (hex): ").strip()
                    key_hex = input("Nhập Secret Key (hex): ").strip()
                    result = symmetric_decrypt(algorithm, ciphertext, key_hex, mode)
                    msg = f"Plaintext: {result}"
                
                status = ket_qua_menu(result)
                if status == "back": return
                if status == "retry": continue
            except Exception as e:
                print_error(str(e))
                if input("\nThử lại? (y/n): ").lower() != 'y': break

# ==================== ASYMMETRIC MENU ====================
def asymmetric_menu():
    while True:
        print("\n--- Asymmetric Encryption (RSA) ---")
        print("1. Sinh cặp khóa (Key Pair)")
        print("2. Mã hóa (Encrypt)")
        print("3. Giải mã (Decrypt)")
        print("0. Quay lại")
        choice = input("Chọn chức năng (0-3): ").strip()
        
        if choice == "0": break
        
        while True:
            try:
                if choice == "1":
                    pub, priv = generate_rsa_key_pair()
                    print("\n Public Key (PEM):\n", pub)
                    print("\n Private Key (PEM):\n", priv)
                    if ket_qua_menu("Đã sinh xong Key") == "back": return
                    break
                elif choice == "2":
                    plaintext = input("\nNhập Plaintext: ").strip()
                    pub_key = input("Dán Public Key (PEM): ").strip()
                    result = rsa_encrypt(plaintext, pub_key)
                    if ket_qua_menu(result) == "back": return
                elif choice == "3":
                    ciphertext = input("\nNhập Ciphertext (hex): ").strip()
                    priv_key = input("Dán Private Key (PEM): ").strip()
                    result = rsa_decrypt(ciphertext, priv_key)
                    if ket_qua_menu(result) == "back": return
                break
            except Exception as e:
                print_error(str(e))
                if input("\nThử lại? (y/n): ").lower() != 'y': break

# ==================== HASH MENU ====================
def hash_menu():
    while True:
        print("\n--- Hash Functions ---")
        text = input("Nhập chuỗi cần băm: ").strip()
        if not text: break

        print("1. MD5")
        print("2. SHA-256")
        print("0. Quay lại")
        choice = input("Chọn loại hash (0-2): ").strip()
        
        if choice == "0": break
        
        try:
            if choice == "1":
                result = md5_hash(text)
            elif choice == "2":
                result = sha256_hash(text)
            else:
                print(" Lựa chọn không hợp lệ!")
                continue
                
            if ket_qua_menu(result) == "back": break
        except Exception as e:
            print_error(str(e))
            if input("\nThử lại? (y/n): ").lower() != 'y': break

if __name__ == "__main__":
    main_menu()