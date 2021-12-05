import re


def check_user_name(user_name):
    pattern=r"[a-zA-Z_]{5,14}"
    res = re.fullmatch(pattern, user_name)
    if res:
        print("Yes , It is okay.. ")
    else:
        print("Invalid user name.. ")


def ceck_email(email):
    pat=r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b'
    res = re.fullmatch(pat, email)
    if res:
        print("Yes , It is okay.. ")
    else:
        print("Invalid Email.. ")
a=ceck_email('hamedsojodi1374@gmail.com')

