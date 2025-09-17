# 🔐 FileCrypt

**FileCrypt** là một công cụ Python đơn giản để **mã hóa** và **giải mã** file bằng thuật toán AES.  
Mục tiêu: bảo vệ dữ liệu nhạy cảm của bạn (tài liệu, mật khẩu, ảnh, ...) khỏi truy cập trái phép.

---

## 🎯 Mục tiêu

- Hiểu cách mã hóa file bằng AES trong Python.
- Học cách tạo khóa từ mật khẩu bằng PBKDF2.
- Thực hành đọc/ghi file nhị phân an toàn.
- Xây dựng CLI nhỏ gọn: `encrypt` / `decrypt`.

---

## ✨ Tính năng

- Mã hóa file bất kỳ bằng **AES-256-CBC**.
- Sinh khóa từ mật khẩu bằng **PBKDF2-HMAC-SHA256**.
- Sinh **IV (Initialization Vector)** ngẫu nhiên mỗi lần mã hóa.
- Lưu trữ `salt + iv` cùng file đã mã hóa để giải mã.
- CLI đơn giản:
  - `python filecrypt.py encrypt <file_path>`
  - `python filecrypt.py decrypt <encrypted_file>`

---

## 📂 Cấu trúc thư mục

```bash
FileCrypt/
│── README.md            # mô tả project
│── requirements.txt     # thư viện cần cài
│── filecrypt.py         # script chính
│── examples/
│    └── secret.docx
│── src/
│    └── utils.py # hàm tiện ích: sinh key, padding
│    └── decryptor.py # mã hóa
│    └── encryptor.py # giải mã
│    └── argparser.py # đọc cli
│    └── __init__.docx
```

---

## ⚙️ Cài đặt

Yêu cầu: Python >= 3.8

```bash
# Cài thư viện
pip install -r requirements.txt
```

---

## 🚀 Cách sử dụng

### 1. Mã hóa file

```bash
python filecryptor.py -m encrypt -i examples/secret.docx -o examples/encrypted_secret.enc
```

👉 Tạo ra `encrypted_secret.enc`

### 2. Giải mã file

```bash
python filecryptor.py -m decrypt -i examples/encrypted_secret.enc -o examples/decrypted_secret.docx
```

👉 Khôi phục thành `decrypted_secret.docx`

---

## 🔒 Lưu ý bảo mật

- Mật khẩu yếu → dễ bị brute force.
- Đừng dùng cùng một mật khẩu cho nhiều file quan trọng.
- Nên backup mật khẩu ở nơi an toàn (quên mật khẩu = mất file vĩnh viễn).

---

## 📚 Kiến thức học được

- File I/O trong Python (`rb`, `wb`).
- Khái niệm AES, IV, Salt.
- Cách sinh key từ mật khẩu (PBKDF2).
- Thiết kế công cụ CLI nhỏ gọn.
