from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate and save a new encryption key"""
    key = Fernet.generate_key()
    with open('key.key', 'wb') as f:
        f.write(key)
    return key

def add_key():
    """Get the existing key or generate a new one if missing"""
    try:
        with open('key.key', 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return generate_key()

def ensure_password_file():
    """Create password file if it doesn't exist"""
    if not os.path.exists('password.txt'):
        open('password.txt', 'w').close()
def view(fer):

    with open('password.txt', 'r') as f:
        for line in f.readlines():

            generate_data = line.rstrip()
            username, password1 = generate_data.split("|")
            print("Username:", username,"| Password:", fer.decrypt(password1.encode()).decode())

def add(fer, account, password):
    account = input("What is your account name or email? ")
    password = input("What is your password? ")

    with open('password.txt', 'a') as f:
        f.write(account + "|" + fer.encrypt(password.encode()).decode() + "\n")

def delete():
    with open('password.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        print("No passwords to remove. ")
        return

    print("\n\nSaved passwords:")
    counter = 1
    for line in lines:
        account, _ = line.strip().split("|")
        print(f"{counter}. {account}")
        counter += 1

    try:
        choose = int(input("Enter the number to delete (E to cancel): "))
        if choose == "E":
            return
        if 1 <= choose <= len(lines):
            del lines[choose-1]
            with open('password.txt', 'w') as f:
                f.writelines(lines)
        else:
            print("Invalid number")
    except:
        print("Invalid input")

def main():
    master_password = input("What is the Master Password? ").lower()
    if master_password != "cs50":
        print("Not quite right. Hint: Its the best CS course!")
        return


    key = add_key() + master_password.encode()
    fer = Fernet(key)

    while True:
        mode = input("\nWould you like to add, view, delete passwords? (Type 'E' to exit): ").lower()
        if mode == 'e':
            break
        elif mode == 'add':
            add(fer, None, None)
        elif mode == 'view':
            view(fer)
        elif mode == 'delete':
            delete()
        else:
            print("Invalid mode. Try again.")

if __name__ == "__main__":
    main()

