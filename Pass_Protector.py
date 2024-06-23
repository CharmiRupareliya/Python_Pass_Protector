# Importing the Fernet module from the cryptography library for encryption and decryption.

from cryptography.fernet import Fernet
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
'''
# Function to generate and save a new encryption key.
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

print()
print(Fore.MAGENTA + Style.BRIGHT + "Welcome to Pass Protector!")
# Function to load the existing encryption key from the "key.key" file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)  # Initialize a Fernet object with the loaded key for encrypting and decrypting passwords

# Function to view the stored account names and their decrypted passwords.
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

# Function to add a new account name and password to the file
def add():
    name = input(Fore.BLUE + 'Account Name: ')
    pwd = input(Fore.BLUE +"Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True: # Main loop to continuously prompt the user for actions.
    mode = input(Fore.BLACK + Style.BRIGHT +
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":

        break

    if mode == "view":
        view()
        print()
    elif mode == "add":
        add()
        print()
    else:
        print(Fore.RED + "Invalid mode.")
        continue