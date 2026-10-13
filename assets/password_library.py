# Adding encoding='utf-8' fix the program to run in Windows environments, since Windows by default uses Windows-1252 (cp-1252) which is a legacy encoding. Linux uses utf-8 by default
with open('assets/10k-most-common.txt', encoding='utf-8') as f1:
        pass_lib1 = f1.read()
        lib1 = pass_lib1.splitlines()

with open('assets/100k-most-used-passwords-NCSC.txt', encoding='utf-8') as f2: 
        pass_lib2 = f2.read()
        lib2 = pass_lib2.splitlines()

password_library = set(lib1+lib2)

def common_password(password):
    # If password is a common password, it return as True
    if password in password_library:
        return True
    else:
        return False

# Tester to make sure both libs are working and merging together
# print(len(lib1)) # 10001
# print(len(lib2)) # 99840
# print(len(password_library)) # 101075 unique passwords