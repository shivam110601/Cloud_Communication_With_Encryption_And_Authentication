import hashlib
from cryptography import public_key


def hash_string(value):
    hash_object = hashlib.sha256()
    hash_object.update(value.encode('utf-8'))
    return hash_object.hexdigest()


if __name__ == '__main__':
    loginid: str = input("Enter ID: ")
    password: str = input("Enter password: ")
    string = loginid + password + str(public_key)
    hashed_data = hash_string(string)

