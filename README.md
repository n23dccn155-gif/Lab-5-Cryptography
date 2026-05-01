# Cryptography Toolkit - Lab 5.1

Bộ công cụ mật mã (Cryptography Toolkit) được phát triển như một phần của bài tập thực hành môn **An toàn và Bảo mật thông tin**. Ứng dụng cung cấp các tính năng mã hóa đối xứng, bất đối xứng và các hàm băm tiêu chuẩn.

## Tính năng chính

Ứng dụng được thiết kế với giao diện dòng lệnh (CLI) thân thiện, hỗ trợ đầy đủ các yêu cầu của bài Lab:

### 1. Mã hóa đối xứng (Symmetric Encryption)

* **Thuật toán hỗ trợ:** DES, 3DES, AES.
* **Chế độ hoạt động:** Hỗ trợ cả **CBC** (Cipher Block Chaining) và **ECB** (Electronic Codebook).
* **Quản lý khóa:** Cho phép người dùng nhập khóa thủ công (dạng Hex) hoặc tự động sinh khóa ngẫu nhiên an toàn.
* **Chức năng:** Mã hóa Plaintext và Giải mã Ciphertext.

### 2. Mã hóa bất đối xứng (Asymmetric Encryption)

* **Thuật toán:** RSA (Rivest–Shamir–Adleman).
* **Quản lý khóa:** Tự động sinh cặp khóa Public Key & Private Key (định dạng PEM).
* **Chức năng:** Mã hóa bằng Public Key và Giải mã bằng Private Key (định dạng Hex).

### 3. Hàm băm (Hash Functions)

* **Thuật toán hỗ trợ:** MD5 và SHA-256.
* **Chức năng:** Tính toán giá trị Digest (băm) từ một chuỗi văn bản đầu vào.

### 4. Trải nghiệm người dùng (UX)

* Hệ thống Menu phân cấp rõ ràng.
* Hỗ trợ tính năng **Copy kết quả** trực tiếp vào Clipboard.
* Xử lý lỗi thông minh (sai độ dài key, sai định dạng dữ liệu) giúp ứng dụng chạy mượt mà.
* Tùy chọn **Thử lại (Try Again)** nhanh chóng sau mỗi lần thực hiện.

## Công nghệ sử dụng

* **Ngôn ngữ:** Python 3.x
* **Thư viện chính:** `pycryptodome` (Thư viện chuẩn về mật mã học).
* **Hệ điều hành hỗ trợ:** Windows (tối ưu tính năng Copy).

## Cài đặt và Sử dụng

### 1. Cài đặt thư viện

Yêu cầu máy tính đã cài đặt Python. Mở terminal/cmd và chạy lệnh:

```bash
pip install -r requirement.txt
```

### 2. Chạy ứng dụng

```bash
python main.py
```

## Cấu trúc dự án

* `main.py`: Điểm điều hướng chính, xử lý giao diện Menu và luồng UX.
* `symmetric.py`: Cài đặt logic cho DES, 3DES, AES.
* `asymmetric.py`: Cài đặt logic cho thuật toán RSA.
* `hashing.py`: Thực hiện các hàm băm MD5 và SHA-256.
* `utils.py`: Các hàm tiện ích, kiểm tra hợp lệ dữ liệu và xử lý thông báo lỗi.

---

**Nhóm thực hiện:** 

- Hảo - Asymmetric Encryption (RSA)
- Hiệp - Symmertric
- Trường Hiếu - Hash Functions (MD5, SHA-256)
- Trung Hiếu - UI & Integration
- Hay - Utils & Error Handling
