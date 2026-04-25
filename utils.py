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

def kiem_tra_key_des(key):
    if len(key) != 8:
        print("Loi: Key DES phai co dung 8 ky tu, ban nhap", len(key), "ky tu")
        return False
    return True

def kiem_tra_key_3des(key):
    if len(key) not in [16, 24]:
        print("Loi: Key 3DES phai co 16 hoac 24 ky tu, ban nhap", len(key), "ky tu")
        return False
    return True

def kiem_tra_key_aes(key):
    if len(key) not in [16, 24, 32]:
        print("Loi: Key AES phai co 16, 24 hoac 32 ky tu, ban nhap", len(key), "ky tu")
        return False
    return True

def kiem_tra_trong(text, ten_o="Du lieu"):
    if text == "" or text.strip() == "":
        print("Loi:", ten_o, "khong duoc de trong!")
        return False
    return True

def bao_loi(thong_bao):
    print("[LOI]", thong_bao)

def bao_ok(thong_bao):
    print("[OK]", thong_bao)

def in_ket_qua(ten, gia_tri):
    print("=" * 40)
    print(ten + ":", gia_tri)
    print("=" * 40)