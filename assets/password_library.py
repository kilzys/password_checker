# Adding encoding='utf-8' fix the program to run in Windows environments, since Windows by default uses Windows-1252 (cp-1252) which is a legacy encoding. Linux uses utf-8 by default
with open('assets/10k-most-common.txt', encoding='utf-8') as f1:
        pass_lib1 = f1.read()
        lib1 = pass_lib1.split('\n')
        f1.close()

with open('assets/100k-most-used-passwords-NCSC.txt', encoding='utf-8') as f2: 
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