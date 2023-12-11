import sys
import bcrypt
import os
import hashlib


def crack_md5(target_hash, password_list):
    for password in password_list:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == target_hash:
            return password
    return None

def crack_bcrypt(target_hash, password_list):
    for password in password_list:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        if hashed_password == target_hash:
            return password
    return None

def crack_sha256(target_hash, password_list):
    for password in password_list:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == target_hash:
            return password
    return None

def main():
    file_path = "passwords.txt"
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found. Make sure the file exists.")
        sys.exit(1)

    with open(file_path, "r") as file:
        password_list = [line.strip() for line in file]

    target_hash = input("Enter the hash to crack: ")

    hash_method = input("Choose password hash method (1: MD5, 2: BCrypt, 3: SHA-256): ")

    if hash_method == "1":
        crack_method = crack_md5
    elif hash_method == "2":
        crack_method = crack_bcrypt
    elif hash_method == "3":
        crack_method = crack_sha256
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    cracked_password = crack_method(target_hash, password_list)

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found in the list.")

if __name__ == "__main__":
    main()

