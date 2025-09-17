import struct
from . import utils
from cryptography.fernet import Fernet, InvalidToken
# Constants for header
MAGIC = b'FENC'         # 4 bytes
VERSION = b'\x01'       # 1 byte
SALT_SIZE = 16          # bytes
ITERATIONS_SIZE = 4     # store as big-endian unsigned int
HEADER_SIZE = 4 + 1 + SALT_SIZE + ITERATIONS_SIZE  # = 25

def decrypt_file(input_path: str, output_path: str, password: str) -> None:
    decrypted_information = b''
    try: 
        # Mở file và đọc
        with open(input_path, 'rb') as f:
            # Lấy header và kiểm tra
            header = f.read(HEADER_SIZE)
            if (len(header) < HEADER_SIZE):
                raise ValueError('Input file too small or file corrupt')
            
            # Lấy thông tin về magic và version
            magic = header[0:4]
            version = header[4:5]
            if magic != MAGIC:
                raise ValueError('Unreconzied file')

            # Lấy salt và iterations   
            salt = header[5:5+SALT_SIZE]
            packed_iterations = header[5+SALT_SIZE: 5 + SALT_SIZE + ITERATIONS_SIZE]
            iterations = struct.unpack('>I', packed_iterations)[0]

            # Tạo key
            key = utils.derive_key(password=password, salt=salt, iterations=iterations)

            # Đọc dữ liệu mã hóa
            cipher_text = f.read()

            # Giải mã
            fernet = Fernet(key=key)
            decrypted_information = fernet.decrypt(cipher_text)
    except FileNotFoundError:
        raise FileNotFoundError(f'Can\'t find {input_path}!')
    except InvalidToken:
        raise InvalidToken(f'Can\'t decrypt file because wrong password or file was changed!')
    except Exception:
        raise Exception(f'Unhandling Error')
    
    try:
        with open(output_path, 'wb') as f:
            f.write(decrypted_information)
    except FileNotFoundError:
        raise FileNotFoundError(f'Can\'t find {output_path}!')
    except Exception:
        raise Exception(f'Unhandling Error!')
    
    print(f'[+] Decrypted \'{input_path}\' → \'{output_path}\'')
   
    


        
