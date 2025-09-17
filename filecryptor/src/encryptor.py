import os
import struct
from cryptography.fernet import Fernet
from . import utils

# Constants for header
MAGIC = b'FENC'         # 4 bytes
VERSION = b'\x01'       # 1 byte
SALT_SIZE = 16          # bytes
ITERATIONS_SIZE = 4     # store as big-endian unsigned int
HEADER_SIZE = 4 + 1 + SALT_SIZE + ITERATIONS_SIZE  # = 25


def encrypt_file(input_path: str, output_path: str, password: str, iterations: int = 200_000) -> None:
    """
    Encrypt the input file and write to output file with header containing salt + iterations.
    """
    try:
        # Đọc thông tin toàn bộ file
        with open(input_path, 'rb') as f:
            infomation = f.read()

        # Sinh salt
        salt = os.urandom(SALT_SIZE)

        # Chuyển password + salt + iterations thành key
        key = utils.derive_key(password=password, salt=salt, iterations=iterations)

        # Mã hóa thông tin
        fernet = Fernet(key=key)
        encrypted_infomation = fernet.encrypt(infomation)

        # Chuyển iteration từ int thành Big-endian
        iteratons_packed = struct.pack('>I', iterations)

        # Ghi header kèm thông tin đã mã hóa
        with open(output_path, 'wb') as f:
            f.write(MAGIC)
            f.write(VERSION),
            f.write(salt),
            f.write(iteratons_packed)
            f.write(encrypted_infomation)

        print(f'[+] Encrypted \'{input_path}\' → \'{output_path}!\'')
    except FileNotFoundError:
        raise FileNotFoundError(f'Can\'t find {input_path}!')
    except Exception:
        raise Exception(f'Unhandling Error')






