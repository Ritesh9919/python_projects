from cryptography.fernet import Fernet


# def generate_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)




def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def add():
    name = input("Enter the name of the account: ").lower()
    password = input("Enter the password: ").lower()

    with open("password.txt", "a") as f:
        f.write(f"{name} | {fer.encrypt(password.encode()).decode()}\n")




def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, password = data.split("|")
            print(f"Account: {name}| Password: {fer.decrypt(password.encode()).decode()}")




while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view) or  q to quit: ").lower()
    if mode == "q":
        break

    if mode == "add":
        add()

    elif mode == "view":
        view()
    else:
        print("Invalid mode")
        continue