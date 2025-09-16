import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


def derive_key(password : str, salt : bytes, iterations: int) -> bytes:
    """
    Derive a Fernet-compatible key (base64 urlsafe) from a password.

    :param password: str (UTF-8)
    :param salt: bytes (cryptographically random)
    :param iterations: int (cost parameter)
    :return: bytes (urlsafe-base64 encoded key) suitable for Fernet
    """
    # Kiểm tra kiểu dữ liệu
    if not isinstance(salt, (bytes, bytearray)):
        raise TypeError('Salt must be bytes')
    
    # Chuyển về UTF-8 do derive()
    encode_password = password.encode('utf-8')

    # Dùng để biến mật khảu thành khóa
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), # Thuật toán
        length=32, # Đọ dài đầu ra
        salt=salt, # salt
        iterations=iterations, # Số vòng?
    )
    # Lấy key dạng raw bytes
    raw_key = kdf.derive(encode_password)
    # Chuyển raw_key về định dạng Fernet() chấp nhận
    key = base64.urlsafe_b64encode(raw_key)
    return key
