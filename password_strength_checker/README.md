Chức năng chính

Nhập mật khẩu từ người dùng

Có thể nhập trực tiếp qua terminal (ẩn input để bảo mật càng tốt).

Kiểm tra các tiêu chí cơ bản của mật khẩu:

Độ dài (>= 8 ký tự).

Chứa ít nhất 1 chữ hoa (A–Z).

Chứa ít nhất 1 chữ thường (a–z).

Chứa ít nhất 1 chữ số (0–9).

Chứa ít nhất 1 ký tự đặc biệt (ví dụ: !@#$%^&\*()-\_=+[]{};:,.<>?/).

Đánh giá độ mạnh mật khẩu (ví dụ chia thành các mức):

    Rất yếu (chỉ toàn chữ thường, độ dài ngắn).

    Yếu (có số hoặc chữ hoa nhưng vẫn quá ngắn).

    Trung bình (đủ 8 ký tự và có ít nhất 3 nhóm ký tự khác nhau).

    Mạnh (đủ điều kiện và dài > 12 ký tự).

    Rất mạnh (dài > 16 ký tự và đầy đủ 4 nhóm).

    Kiểm tra mật khẩu có nằm trong danh sách mật khẩu phổ biến (password123, 123456, qwerty, ...) không.

Xuất kết quả ra màn hình:

    In ra mức độ của mật khẩu.

    Gợi ý cải thiện nếu mật khẩu chưa đủ mạnh (ví dụ: "Hãy thêm ký tự đặc biệt để tăng độ an toàn").

Viết thành module để có thể import vào dự án khác.

Viết test cases đơn giản (dùng unittest hoặc pytest).
