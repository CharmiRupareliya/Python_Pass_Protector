# Python_Pass_Protector
Pass Protector - A Secure Python Password Manager 

>>Description:

  This repository contains the code for Pass Protector, a Python program that helps you securely store and manage your passwords. It utilizes encryption to ensure your passwords remain confidential even if the 
  storage file falls into the wrong hands.

>>Features:

1.Encryption for Password Security: Pass Protector uses the powerful Fernet library from the cryptography module to encrypt user's passwords before storing them in a text file.
2.User-Friendly Interface: The program provides a simple menu-driven interface for adding new passwords, viewing existing ones, and exiting the program.
3.Colorama Integration: The program utilizes the colorama library to display colorful output for a more visually appealing experience.
4.Clear Instructions: The code includes comments to enhance readability and understanding.

>>Instructions for Adding and Viewing Passwords:

1.Adding a New Password: When prompted to "add," enter the account name and your password. Pass Protector will encrypt the password and store it securely with the account name in a file named "passwords.txt."
2.Viewing Existing Passwords: Choosing "view" will display a list of your stored account names and their decrypted passwords.

>>Modules Used:

1.Fernet (cryptography): Provides secure and efficient encryption/decryption functionalities.
2.colorama: Enhances the visual experience with colored text output.

Embrace Secure Password Management with Pass Protector!
