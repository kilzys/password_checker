# Functions
from password_library import common_password
from string import punctuation, digits
secure_level = {'uppercase': False, 
    'lowercase': False,
    'lenght': False,
    'numbers': False,
    'symbol': False
     }
number = False

def pass_check(password):
    key = common_password(password)
    if key:
        print(f'\033[31mKNOWN PASSWORD! This is a common password in the world, dont use it!\033[m')
    else:
        # Checking lenght and password
        if len(password) >= 12:
            secure_level['lenght'] = True

        for word in password:
            # Number check
            try:
                temp = int(word)
                secure_level['numbers'] = True
                number = True
            except:
                # Since the possibility of number is removed, everything else is special characters and words
                # Upper check
                temp = word.upper()
                if temp == word:
                    secure_level['uppercase'] = True

                # Lower check
                temp = word.lower()
                if temp == word:
                    secure_level['lowercase'] = True

                # Symbol check
                if word in punctuation:
                    secure_level['symbol'] = True

            


        # Final check
        level = 0
        index = 1
        for check_level in secure_level:
            if secure_level[check_level]:
                level+=1
                print(f'Check {index}/5 [{check_level}]: \033[32mSucess!\033[m')
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
