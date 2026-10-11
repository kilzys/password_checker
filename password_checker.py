# Functions
from password_library import common_password
from string import punctuation, digits, ascii_lowercase, ascii_uppercase
secure_level = {'uppercase': False, 
    'lowercase': False,
    'length': False,
    'digits': False,
    'special_char': False
     }
number = False

def pass_check(password):
    key = common_password(password)
    if key:
        print(f'\033[31mKNOWN PASSWORD! This is a common password in the world, dont use it!\033[m')
    else:
        # Checking length and password
        if len(password) >= 12:
            secure_level['length'] = True

        for word in password:
            # Number check
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
                print(f'Check {index}/5 [{check_level}]: \033[32mSuccess!\033[m')
            else:
                print(f'Check {index}/5 [{check_level}]: \033[31mFail!\033[m')
            index += 1

        # How secure is the password
        if level == 5:
            print(f'Password: \033[36mStrong\033[m')
        elif 5 > level > 3:
            print(f'Password:  \033[33mMedium\033[m')
        else:
            print(f'Password:  \033[31mWeak\033[m')