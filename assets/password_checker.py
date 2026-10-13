# Imports
from assets.password_library import common_password
from string import punctuation, digits, ascii_lowercase, ascii_uppercase
from assets.hashpassword import hash_password

def pass_check(password):
    # Start from default
    secure_level = {'uppercase': False, 'lowercase': False,'length': False,'digits': False,'special_char': False}

    # If 'exit' the program leaves
    if password.lower().strip() == 'exit':
        print("\033[m")
        return

    # If password is blank
    if password.strip() == '':
        print('\033[31mBlank password! Some systems allow it, and attackers try it first.\033[m')
        return

    # Check for common passwords
    key = common_password(password)
    if key:
        print(f'\033[31m{password} is a KNOWN PASSWORD! This is a common password in the world, dont use it!\033[m')
    else:
        # Checking length and password
        if len(password) >= 12:
            secure_level['length'] = True

        for word in password:
            # Password check
            # Spaces are ignored
            if word in ascii_lowercase:
                secure_level['lowercase'] = True
            if word in ascii_uppercase:
                secure_level['uppercase'] = True
            if word in digits:
                secure_level['digits'] = True
            if word in punctuation:
                secure_level['special_char'] = True

        # Final check
        level = 0
        index = 1
        for check_level in secure_level:
            if secure_level[check_level]:
                level+=1
                print(f'\033[34mCheck {index}/5 [{check_level}]:\033[m \033[32mSuccess!\033[m')
            else:
                print(f'\033[34mCheck {index}/5 [{check_level}]:\033[m \033[31mFail!\033[m')
            index += 1

        # How secure is the password
        if level == 5:
            print(f'\033[34mPassword:\033[m \033[36mStrong\033[m')
        elif 5 > level > 3:
            print(f'\033[34mPassword:\033[m  \033[33mMedium\033[m')
        else:
            print(f'\033[34mPassword:\033[m  \033[31mWeak\033[m')


        # Hash digest
        print(f'\033[34mHash sha256 digest of your password:\n\033[35m> {hash_password(password)}\033[m')