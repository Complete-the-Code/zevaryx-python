from . import caesar, atbash


def menu(strings: list):
    while True:
        print(
            """
 Choose an option:

 1) Caesar Cipher
 2) Atbash Cipher

 0) Go back
        """
        )
        choice = input("> ")
        if choice == "1":
            caesar.menu(strings)
        elif choice == "2":
            atbash.menu(strings)
        elif choice == "0":
            break
