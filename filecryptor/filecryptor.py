import getpass

from src import argparser
from src import encryptor
from src import decryptor

def run_file_cryptor(mode: str, input_path: str, output_path) -> None:
    try:
        password = getpass.getpass('Enter password: ')
        if mode == 'encrypt':
            encryptor.encrypt_file(input_path=input_path,
                                    output_path=output_path,
                                    password=password)
        elif mode == 'decrypt':
            decryptor.decrypt_file(input_path=input_path,
                                    output_path=output_path,
                                    password=password)
    except Exception as e:
        print(f'Error: {e}')
        
if __name__ == '__main__':
    args = argparser.parse_args()
    run_file_cryptor(mode=args.mode,
                     input_path=args.input_path,
                     output_path=args.output_path)
