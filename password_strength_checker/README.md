# 🔑 Chức Năng Chính - Password Strength Checker

## 1️⃣ Nhập mật khẩu từ người dùng

- Có thể nhập trực tiếp qua **terminal**.
- Nên ẩn input để bảo mật tốt hơn (dùng `getpass` trong Python).

## 2️⃣ Kiểm tra các tiêu chí cơ bản của mật khẩu

- **Độ dài**: `>= 8` ký tự.
- **Chứa ít nhất 1 chữ hoa**: `A–Z`.
- **Chứa ít nhất 1 chữ thường**: `a–z`.
- **Chứa ít nhất 1 chữ số**: `0–9`.
- **Chứa ít nhất 1 ký tự đặc biệt**:  
  `!@#$%^&*()-_=+[]{};:,.<>?/`

## 3️⃣ Đánh giá độ mạnh của mật khẩu

Chia thành các mức sau:

| Mức độ            | Tiêu chí                                           |
| ----------------- | -------------------------------------------------- |
| 🔴 **Rất yếu**    | Chỉ toàn chữ thường, độ dài ngắn (< 8 ký tự).      |
| 🟠 **Yếu**        | Có số hoặc chữ hoa nhưng vẫn quá ngắn (< 8 ký tự). |
| 🟡 **Trung bình** | Đủ ≥ 8 ký tự và có ít nhất 3 nhóm ký tự khác nhau. |
| 🟢 **Mạnh**       | Đủ điều kiện cơ bản và dài > 12 ký tự.             |
| 🟣 **Rất mạnh**   | Dài > 16 ký tự và chứa đầy đủ 4 nhóm ký tự.        |

## 4️⃣ Kiểm tra mật khẩu phổ biến

- Đối chiếu với danh sách mật khẩu phổ biến:  
  `password123`, `123456`, `qwerty`, ...

## 5️⃣ Xuất kết quả ra màn hình

- In ra **mức độ** của mật khẩu.
- Nếu chưa đủ mạnh → gợi ý cải thiện, ví dụ:
  > 💡 _"Hãy thêm ký tự đặc biệt để tăng độ an toàn."_

## 6️⃣ Viết thành module tái sử dụng

- Đóng gói dưới dạng module để có thể `import` vào các dự án khác.

## 7️⃣ Viết test cases

- Dùng **unittest** hoặc **pytest** để kiểm thử tự động.
