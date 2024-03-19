import re
def email(mail):
    pattern=("^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$")
    if re.search(pattern,mail):
        return "Right email"
    else:
        return("Wrong email")
user_input=input("enter your email: ")
print(email(user_input))