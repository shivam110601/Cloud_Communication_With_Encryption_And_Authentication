import os
import rsa


def generate_keys():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key


def encrypt_message(message, public_key):
    encrypted_message = rsa.encrypt(message.encode("utf-8"), public_key)
    return encrypted_message


def decrypt_message(encrypted_message, private_key):
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode("utf-8")
    return decrypted_message


def encrypt_file(file_path, public_key):
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = []
    for chunk in range(0, len(data), 245):
        encrypted_chunk = rsa.encrypt(data[chunk:chunk + 245], public_key)
        encrypted_data.append(encrypted_chunk)
    return encrypted_data


def decrypt_file(encrypted_data, private_key):
    decrypted_data = b""
    for chunk in encrypted_data:
        decrypted_chunk = rsa.decrypt(chunk, private_key)
        decrypted_data += decrypted_chunk
    file_name = os.path.basename("file")
    with open(f"decrypted_{file_name}", "wb") as file:
        file.write(decrypted_data)

def main():
    message = "This is a secret message."
    encrypted_message = encrypt_message(message, public_key)
    decrypted_message = decrypt_message(encrypted_message, private_key)
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

    file_path = "examplefile"
    encrypted_data = encrypt_file(file_path, public_key)
    decrypt_file(encrypted_data, private_key)

public_key, private_key = generate_keys()

if __name__ == "__main__":
    main()
