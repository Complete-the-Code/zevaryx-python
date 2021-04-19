from string import ascii_uppercase


def menu(strings: list):
    while True:
        print(
            """
 Choose an option:

 1) Atbash Decipher

 0) Go back
        """
        )
        choice = input("> ")
        if choice == "1":
            results = {k: decipher(k) for k in strings}
            for k in results:
                print(f"\n{k}: {results[k]}")
        elif choice == "0":
            break


def decipher(string: str) -> str:
    """
    Atbash deciphering
    Credit: https://github.com/jameslyons/pycipher/

    :param string: String to decipher
    :return: Deciphered string
    """
    ret = ""
    for c in string:
        ret += ascii_uppercase[25 - ascii_uppercase.index(c)]
    return ret
