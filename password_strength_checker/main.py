from src import checker
import getpass

def main():
    print(checker.check_password_strength('abc'))

    print(checker.check_password_strength('abcd1234'))
    
    print(checker.check_password_strength('!abc12345'))

    print(checker.check_password_strength('Abc12345!XYZ'))         

    print(checker.check_password_strength('Abc12345!@#$%^XYZ'))

    password = getpass.getpass('Your password: ')
    print(checker.check_password_strength(password))

    
if __name__ == '__main__':
    main()