import sys
from symmetric import generate_random_key, symmetric_encrypt, symmetric_decrypt
from asymmetric import generate_rsa_key_pair, rsa_encrypt, rsa_decrypt
from hashing import md5_hash, sha256_hash
from utils import print_error

def main_menu():
    while True:
        print("\n" + "="*55)
        print("🔐 CRYPTOGRAPHY TOOLKIT")
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
            print("👋 Cảm ơn bạn đã sử dụng chương trình!")
            sys.exit(0)
        else:
            print("❌ Lựa chọn không hợp lệ! Vui lòng nhập số từ 1-4.")

# ==================== SYMMETRIC MENU ====================
def symmetric_menu():
    print("\n--- Symmetric Encryption ---")
    
    # Chọn thuật toán bằng số
    print("1. DES")
    print("2. 3DES")
    print("3. AES")
    alg_choice = input("Chọn thuật toán (1-3): ").strip()
    
    if alg_choice == "1":
        algorithm = "DES"
    elif alg_choice == "2":
        algorithm = "3DES"
    elif alg_choice == "3":
        algorithm = "AES"
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return

    # Chọn chức năng
    print("\n1. Mã hóa (Encrypt)")
    print("2. Giải mã (Decrypt)")
    action = input("Chọn chức năng (1-2): ").strip()

    if action == "1":  # Encrypt
        plaintext = input("\nNhập Plaintext: ").strip()
        
        print("\n1. Nhập key thủ công")
        print("2. Tự sinh key ngẫu nhiên")
        key_choice = input("Chọn (1-2): ").strip()
        
        if key_choice == "2":
            try:
                key_hex = generate_random_key(algorithm)
                print(f"🔑 Key ngẫu nhiên (hex): {key_hex}")
            except Exception as e:
                print_error(str(e))
                return
        else:
            key_hex = input("Nhập Secret Key (dạng hex): ").strip()
        
        try:
            ciphertext = symmetric_encrypt(algorithm, plaintext, key_hex)
            print(f"\n✅ Ciphertext (hex):\n{ciphertext}")
        except Exception as e:
            print_error(str(e))
            
    elif action == "2":  # Decrypt
        ciphertext = input("\nNhập Ciphertext (hex): ").strip()
        key_hex = input("Nhập Secret Key (hex): ").strip()
        
        try:
            plaintext = symmetric_decrypt(algorithm, ciphertext, key_hex)
            print(f"\n✅ Plaintext:\n{plaintext}")
        except Exception as e:
            print_error(str(e))
    else:
        print("❌ Lựa chọn không hợp lệ!")

# ==================== ASYMMETRIC MENU ====================
def asymmetric_menu():
    print("\n--- Asymmetric Encryption (RSA) ---")
    print("1. Sinh cặp khóa (Key Pair)")
    print("2. Mã hóa (Encrypt)")
    print("3. Giải mã (Decrypt)")
    choice = input("Chọn chức năng (1-3): ").strip()
    
    if choice == "1":
        try:
            pub, priv = generate_rsa_key_pair()
            print("\n🔑 Public Key (PEM):\n", pub)
            print("\n🔒 Private Key (PEM):\n", priv)
        except Exception as e:
            print_error(str(e))
    
    elif choice == "2":
        plaintext = input("\nNhập Plaintext: ").strip()
        pub_key = input("\nDán Public Key (PEM):\n").strip()
        try:
            ct = rsa_encrypt(plaintext, pub_key)
            print(f"\n✅ Ciphertext (hex):\n{ct}")
        except Exception as e:
            print_error(str(e))
    
    elif choice == "3":
        ciphertext = input("\nNhập Ciphertext (hex): ").strip()
        priv_key = input("\nDán Private Key (PEM):\n").strip()
        try:
            pt = rsa_decrypt(ciphertext, priv_key)
            print(f"\n✅ Plaintext:\n{pt}")
        except Exception as e:
            print_error(str(e))
    else:
        print("❌ Lựa chọn không hợp lệ!")

# ==================== HASH MENU ====================
def hash_menu():
    print("\n--- Hash Functions ---")
    text = input("Nhập chuỗi cần băm: ").strip()
    
    print("\n1. MD5")
    print("2. SHA-256")
    choice = input("Chọn loại hash (1-2): ").strip()
    
    try:
        if choice == "1":
            print(f"\nMD5     : {md5_hash(text)}")
        elif choice == "2":
            print(f"\nSHA-256 : {sha256_hash(text)}")
        else:
            print("❌ Lựa chọn không hợp lệ!")
    except Exception as e:
        print_error(str(e))

if __name__ == "__main__":
    main_menu()