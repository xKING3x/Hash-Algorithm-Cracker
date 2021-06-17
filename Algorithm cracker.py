#Before you start using the program be sure that the password list and the script are in the same directory and you need to browse it in your terminall too

import hashlib

def hash_name():
    
    resp = input("""Options:  1)SHA1
          2)SHA256
          3)MD5
Enter the hash algorithm number you want to run: """)
    print("You selected option: ", resp)   
    if resp == '1':
        def convert_text_to_sha1(text):
            digest = hashlib.sha1(
            text.encode()
            ).hexdigest()
            return digest
        def sha1():
            user_sha1 = input("Enter the SHA1 to Crack: ")
            cleaned_user_sha1 = user_sha1.strip().lower()
            with open('passwords.txt') as f:    # <----- enter your password wordlist
                for line in f:
                    password = line.strip()
                    converted_sha1 = convert_text_to_sha1(
                        password)
                    if cleaned_user_sha1 == converted_sha1:
                        print(f"Password Found: {password}")
                        return
            print("Could not find the password")
        if __name__ == "__main__":
            sha1()
    elif resp == '2':
        def convert_text_to_sha256(text):
            digest = hashlib.sha256(
            text.encode()
            ).hexdigest()
            return digest
        def sha256():
            user_sha256 = input("Enter the SHA256 to Crack: ")
            cleaned_user_sha256 = user_sha256.strip().lower()
            with open('passwords.txt') as f:    # <----- enter your password wordlist
                for line in f:
                    password = line.strip()
                    converted_sha256 = convert_text_to_sha256(
                        password)
                    if cleaned_user_sha256 == converted_sha256:
                        print(f"Password Found: {password}")
                        return
            print("Could not find the password")
        if __name__ == "__main__":
            sha256()
    elif resp == '3':
        def convert_text_to_md5(text):
            digest = hashlib.md5(
            text.encode()
            ).hexdigest()
            return digest
        def md5():
            user_md5 = input("Enter the MD5 to Crack: ")
            cleaned_user_md5 = user_md5.strip().lower()
            with open('passwords.txt') as f:    # <----- enter your password wordlist
                for line in f:
                    password = line.strip()
                    converted_md5 = convert_text_to_md5(
                        password)
                    if cleaned_user_md5 == converted_md5:
                        print(f"Password Found: {password}")
                        return
            print("Could not find the password")
        if __name__ == "__main__":
            md5()
    else:
        print("Invalid Optrion")

hash_name()