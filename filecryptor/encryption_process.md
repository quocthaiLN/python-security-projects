# 🔐 Quy trình mã hóa với file trong Python

## 1. Chuẩn bị

- **Mục tiêu**: Mã hóa/giải mã dữ liệu bằng mật khẩu người dùng nhập
  vào.
- **Thư viện**: `cryptography` (Fernet, PBKDF2HMAC).

---

## 2. Quy trình

### 2.1 Người dùng nhập mật khẩu 🔑

- Mật khẩu do người dùng nhập sẽ không trực tiếp làm khóa mã hóa.
- Thay vào đó, mật khẩu được chuyển thành khóa đối xứng bằng **Key
  Derivation Function (KDF)**.

### 2.2 Sinh khóa từ mật khẩu 🛠️

- Dùng **PBKDF2HMAC** với:
  - Thuật toán băm: `SHA-256`
  - Salt: ngẫu nhiên sinh ra
  - Số vòng lặp: thường từ 100.000 trở lên
- Kết quả: một khóa 32 bytes (dùng cho Fernet).

### 2.3 Mã hóa dữ liệu 📦

- Tạo đối tượng `Fernet(key)`
- Gọi `fernet.encrypt(data)` → dữ liệu mã hóa (ciphertext)

### 2.4 Lưu file 🔒

- File sau khi mã hóa có cấu trúc:
  1.  **Header**: chứa salt + số vòng lặp (dùng cho giải mã sau này)
  2.  **Ciphertext**: dữ liệu đã mã hóa

### 2.5 Giải mã dữ liệu 🔓

1.  Người dùng nhập mật khẩu
2.  Đọc salt + số vòng lặp từ header
3.  Sinh lại khóa bằng PBKDF2HMAC
4.  Dùng Fernet giải mã `ciphertext`

---

## 3. Vai trò mật khẩu 🔑

- Mật khẩu đóng vai trò là **khóa gốc** (master key).
- Từ mật khẩu sinh ra **khóa mã hóa đối xứng**.
- Nếu mật khẩu sai → không thể giải mã dữ liệu.

---

✅ Đây là quy trình **chuẩn & an toàn** để mã hóa file bằng Python với
mật khẩu người dùng.
