import os

def doc_file(duong_dan):
    if not os.path.exists(duong_dan):
        print("Khong tim thay file:", duong_dan)
        return None
    f = open(duong_dan, "r", encoding="utf-8")
    noi_dung = f.read()
    f.close()
    return noi_dung

def ghi_file(duong_dan, noi_dung):
    f = open(duong_dan, "w", encoding="utf-8")
    f.write(noi_dung)
    f.close()
    print("Da ghi xong vao file:", duong_dan)

def kiem_tra_key_des(key_hex):
    # DES key 8 bytes = 16 hex characters
    if len(key_hex) != 16:
        print(f"Loi: Key DES (hex) phai co dung 16 ky tu hex (8 bytes), ban nhap {len(key_hex)} ky tu")
        return False
    return True

def kiem_tra_key_3des(key_hex):
    # 3DES key 16 or 24 bytes = 32 or 48 hex characters
    if len(key_hex) not in [32, 48]:
        print(f"Loi: Key 3DES (hex) phai co 32 hoac 48 ky tu hex, ban nhap {len(key_hex)} ky tu")
        return False
    return True

def kiem_tra_key_aes(key_hex):
    # AES key 16, 24, 32 bytes = 32, 48, 64 hex characters
    if len(key_hex) not in [32, 48, 64]:
        print(f"Loi: Key AES (hex) phai co 32, 48 hoac 64 ky tu hex, ban nhap {len(key_hex)} ky tu")
        return False
    return True

def kiem_tra_trong(text, ten_o="Du lieu"):
    if text == "" or text.strip() == "":
        print("Loi:", ten_o, "khong duoc de trong!")
        return False
    return True

def bao_loi(thong_bao):
    print(f"\n[!] LỖI: {thong_bao}")

# Alias để main.py không bị lỗi import
print_error = bao_loi

def bao_ok(thong_bao):
    print("[OK]", thong_bao)

def in_ket_qua(ten, gia_tri):
    print("=" * 40)
    print(ten + ":", gia_tri)
    print("=" * 40)
if __name__ == "__main__":
    print("=== Test utils.py - Duong Van Hay ===")
    print("1. Kiem tra key DES")
    print("2. Kiem tra key AES")
    print("3. Kiem tra key 3DES")
    print("4. Kiem tra o nhap trong")
    print("5. Ghi va doc file")
    print("0. Thoat")
 
    while True:
        chon = input("\nChon chuc nang (0-5): ")
 
        if chon == "1":
            key = input("Nhap key DES: ")
            ket_qua = kiem_tra_key_des(key)
            if ket_qua:
                bao_ok("Key DES hop le!")
 
        elif chon == "2":
            key = input("Nhap key AES: ")
            ket_qua = kiem_tra_key_aes(key)
            if ket_qua:
                bao_ok("Key AES hop le!")
 
        elif chon == "3":
            key = input("Nhap key 3DES: ")
            ket_qua = kiem_tra_key_3des(key)
            if ket_qua:
                bao_ok("Key 3DES hop le!")
 
        elif chon == "4":
            text = input("Nhap du lieu (de trong de test loi): ")
            ket_qua = kiem_tra_trong(text, "Du lieu nhap")
            if ket_qua:
                bao_ok("Du lieu hop le!")
 
        elif chon == "5":
            noi_dung = input("Nhap noi dung can ghi vao file: ")
            ghi_file("test.txt", noi_dung)
            print("Noi dung doc lai:", doc_file("test.txt"))
 
        elif chon == "0":
            print("Thoat chuong trinh.")
            break
 
        else:
            bao_loi("Chon sai, vui long chon lai!")