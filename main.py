from cryptography.fernet import Fernet
import os


# CONSTANTS --------------------------------------------- #
CMDL_WIDTH = 60

# HELPER FUNCTIONS -------------------------------------- #
def print_ln(sign, amount):
    print(str(sign * amount))


def print_msg(msg, centered=False):
    if centered:
        pass
        # TODO: fix this -------------------------------- !
        # if len(msg) > 60:
        #     msg = msg.split()
        #     c = -1

        #     for i in range(len(msg)):
        #         if c + 1 + len(msg[i]) >= 60:


        # print(msg.center(CMDL_WIDTH))
    else:
        print(msg)


# FUNCTIONALITIES --------------------------------------- #
def get_key():
    key = ""

    if not os.path.isfile("key.key"):
        key = Fernet.generate_key()

        with open("key.key", "wb") as f:
            f.write(key)
        
    else:
        with open("key.key") as f:
            key = f.readline()

    return str(key)


def generate_password():
    pass

def add_password():
    pass


def view_password():
    pass


def confirm_exit():
    pass


def menu():
    msg = "WELCOME IN PASSWORD MANAGER"
    print_ln("-", 60)
    print_msg(msg)



def main():
    key = get_key()
    # print(key)


if __name__ == "__main__":
    main()
