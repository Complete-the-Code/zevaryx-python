from string import ascii_uppercase as upper


def menu(strings: list):
    while True:
        print(
            """
 Choose an option:

 1) Caesar cipher bruteforce

 0) Go back
        """
        )
        choice = input("> ")
        if choice == "1":
            results = {k: decrypt(k) for k in strings}
            for k in results:
                rstr = "\n  ".join(
                    f"Rot {x:>2}: {results[k][x]}" for x in results[k]
                )
                print(f"\n{k}:\n  {rstr}")
        elif choice == "0":
            break


def decrypt(string: str, start: int = 1) -> dict:
    """
    Bruteforce decrypt a string using a Caesar cipher

    :param string: Cipher string
    :param start: Offset to start on
    :return: "Decrypted" strings with index
    """
    strings = {}
    for k in range(start, len(upper)):
        t = ""
        for letter in string:
            num = upper.find(letter) - k
            if num < 0:
                num += len(upper)
            t += upper[num]
        strings[k] = t

    return strings
