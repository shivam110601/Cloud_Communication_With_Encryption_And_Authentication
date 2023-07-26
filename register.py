import math
import random
import smtplib
import hashlib
from cryptography import public_key
from gmail import email_id, app_password

hashed_value = ""


def hash_string(value):
    hash_object = hashlib.sha256()
    hash_object.update(value.encode('utf-8'))
    return hash_object.hexdigest()


if __name__ == '__main__':
    digits = "0123456789"
    OTP = ""

    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    message = OTP + " is your OTP"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    emailid = input("Enter your email: ")
    s.login(email_id, app_password)
    s.sendmail('&&&&&&', emailid, message)

    a = input("Enter your OTP >>: ")
    if a == OTP:
        print("Verified")
        loginid: str = input("Setup ID: ")
        password: str = input("Setup password: ")
        string = loginid + password + str(public_key)
        hashed_value += hash_string(string)
    else:
        print("Please Check your OTP again")