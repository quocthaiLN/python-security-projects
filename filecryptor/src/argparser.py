import argparse

def parse_args():
    parser_cli = argparse.ArgumentParser(
        description='File Encrypt/Decrypt Tool',
        epilog=
        'Example: python filecryptor.py -m encrypt -i examples/secret.docx -o examples/encrypted_secret.enc'
    )

    parser_cli.add_argument(
        '--mode', '-m', type=str, required=True,
        help='Choose encrypt mode or decrypt mode'
    )

    parser_cli.add_argument(
        '--input_path', '-i', type=str, required=True,
        help='Input file path'
    )

    parser_cli.add_argument(
        '--output_path', '-o', type=str, required=True,
        help='Output file path'
    )

    return parser_cli.parse_args()



    