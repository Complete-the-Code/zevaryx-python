from algos import dictcheck, hashcheck
import ciphers
import os
import re
from utils import words as uwords


strings = []

num_match = re.compile(r"[0-9]*")


def main_menu():
    global strings
    while True:
        print(
            f"""
 Strings loaded:

  {', '.join(strings) if strings else 'No strings loaded'}

 Choose a task:

 1) Add a string to check
 2) Remove a string to check
 3) Compare strings to dictionary
 4) Compare strings to hashes
 5) Ciphers

 0) Quit
        """
        )
        choice = input("> ")
        if choice == "1":
            if (string := input("Enter new string: ")) :
                strings.append(string)
        elif choice == "2":
            print(
                "\n".join(
                    f"{idx}) {string}" for idx, string in enumerate(strings)
                )
            )
            to_remove = input("Index to remove: ")
            while not num_match.match(to_remove) and 0 > int(to_remove) > len(
                strings
            ):
                to_remove = input("Index to remove: ")
            strings.pop(int(to_remove))
        elif choice == "3":
            dictcheck.menu(strings, words)
        elif choice == "4":
            hashcheck.menu(strings)
        elif choice == "5":
            ciphers.menu(strings)
        elif choice == "0":
            break


if __name__ == "__main__":
    print(">> Syncing dictionaries...")
    uwords.download_update()
    words = uwords.get_words()
    strs_hash = 0
    if os.path.exists("strings.txt"):
        print(">> Loading strings from strings.txt...")
        with open("strings.txt") as f:
            strings = [x.strip() for x in f.readlines()]
            strs_hash = hash(str(strings))
    main_menu()
    if hash(str(strings)) != strs_hash:
        print("\n\n>> Saving strings changes to strings.txt..")
        with open("strings.txt", "w") as f:
            f.write("\n".join(strings))
    print(">> Goodbye <<")
