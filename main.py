from cryptography.fernet import Fernet
import os


def write_key():
    key = ""

    if not os.path.isfile("key.key"):
        key = Fernet.generate_key()

        with open("key.key", "wb") as f:
            f.write(key)
        
    else:
        with open("key.key") as f:
            key = f.readline()

    return key


def main():
    key = write_key()
    print(key)


if __name__ == "__main__":
    main()
