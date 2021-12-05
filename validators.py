import re


def check_user_name(user_name):
    pattern=r"[a-zA-Z_]{5,14}"
    res = re.fullmatch(pattern, user_name)
    if res:
        print("Yes , It is okay.. ")
    else:
        print("Invalid user name.. ")


def check_email(email):
    pat=r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b'
    res = re.fullmatch(pat, email)
    if res:
        print("Yes , It is okay.. ")
    else:
        print("Invalid Email.. ")


def check_phone(phone):
    pattern=r'(09|\+98)(\d|3[0-3-5-6-7-8-9]|01)\d{8}'
    res =re.fullmatch(pattern, phone)
    if res:
        print("Yes , It is okay.. ")
    else:
        print("Invalid phone.. ")



