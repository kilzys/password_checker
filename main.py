from assets.password_checker import pass_check

# Your password
try:
    pass_check(input('\033[47;30mType your password: [exit for leave]\033[m \033[36m'))
except KeyboardInterrupt:
    print('\033[m\n')
