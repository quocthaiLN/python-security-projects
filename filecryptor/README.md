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
│── filecrypt.py         # script chính (CLI)
│── utils.py             # hàm tiện ích: sinh key, padding
│── examples/
│    ├── sample.txt
│    └── secret.docx
```

---

## ⚙️ Cài đặt

Yêu cầu: Python >= 3.8

```bash
# Clone project
git clone https://github.com/yourusername/FileCrypt.git
cd FileCrypt

# Cài thư viện
pip install -r requirements.txt
```

Nội dung `requirements.txt`:

```
cryptography
```

---

## 🚀 Cách sử dụng

### 1. Mã hóa file

```bash
python filecrypt.py encrypt examples/sample.txt
```

👉 Tạo ra `sample.txt.enc`

### 2. Giải mã file

```bash
python filecrypt.py decrypt examples/sample.txt.enc
```

👉 Khôi phục thành `sample.txt`

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

---

## 🧩 Tiếp theo (gợi ý mở rộng)

- Thêm chế độ AES-GCM để có authenticated encryption (phù hợp cho integrity).
- Lưu metadata (original filename, timestamp) an toàn.
- Tích hợp GUI nhỏ (Tkinter) hoặc package thành CLI cài được bằng pip.
- Thêm testing (pytest) cho các trường hợp encrypt/decrypt, sai mật khẩu, file corrupt.

---
