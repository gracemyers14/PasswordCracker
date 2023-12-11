import hashlib

def crack_md5(target_hash, password_list):
    for password in password_list:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == target_hash:
            return password
    return None

if __name__ == "__main__":
    target_hash = input("Enter the MD5 hash to crack: ")
    password_list = ["password", "123456", "admin", "letmein", "qwerty", "abcdef", "secret"]

    cracked_password = crack_md5(target_hash, password_list)
    
    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found in the list.")