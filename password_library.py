with open('10k-most-common.txt') as f1:
        pass_lib1 = f1.read()
        lib1 = pass_lib1.split('\n')
        f1.close()

with open('100k-most-used-passwords-NCSC.txt') as f2:
        pass_lib2 = f2.read()
        lib2 = pass_lib2.split('\n')
        f2.close()

password_library = lib1+lib2

def common_password(password):
    # If password is a common password, it return as True
    if password in password_library:
        return True
    else:
        return False

# Tester to make sure both libs are working and merging together
# print(len(lib1)) # 10002
# print(len(lib2)) # 99841
# print(len(password_library)) # 109843