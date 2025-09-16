from cryptography.fernet import Fernet
# from package.module import class

key = Fernet.generate_key()
f = Fernet(key)
message = 'This is message.'
encryted_message = f.encrypt(message.encode('utf-8'))
# hoặc
encryted_message = f.encrypt(bytes(message, 'utf-8'))
# encrypt() nhận vào bytes[]
print(encryted_message)

decrypted_message = f.decrypt(encryted_message)
print(decrypted_message)
