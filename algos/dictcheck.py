import difflib
from tqdm import tqdm


def menu(strings: list, words: list):
    while True:
        print(
            """
 Choose an option:

 1) Check direct dictionary matches
 2) Check partial dictionary matches
 3) Check dictionary matches of portions

 0) Go back
    """
        )
        choice = input("> ")
        if choice == "1":
            results = {k: dictcheck(k, words) for k in strings}
            for k in results:
                rstr = "\n  ".join(x for x in results[k])
                print(f"\n{k}:\n  {rstr}")
        elif choice == "2":
            results = {k: dictcheck_partial(k, words) for k in strings}
            for k in results:
                rstr = "\n  ".join(x for x in results[k])
                print(f"\n{k}:\n  {rstr}")
        elif choice == "3":
            results = {k: dictcheck_portion(k, words) for k in strings}
            for k in results:
                rstr = "\n  ".join(x for x in results[k])
                print(f"\n{k}:\n  {rstr}")
        elif choice == "0":
            break


def dictcheck(string: str, words: list, leave=True) -> list:
    """
    Check permutations of string for dictionary match

    :param string: String to check
    :param words: Dictionary to check against
    :return: List of matches
    """
    total = len(words)
    matches = []
    for word in tqdm(
        words,
        total=total,
        desc=f"Analyzing Permutations ({string})",
        unit="words",
        leave=leave,
    ):
        if sorted(string.lower()) == sorted(word.lower()):
            matches.append(word)
    return matches


def dictcheck_partial(
    string: str, words: list, cutoff: float = 0.5, matches: int = 25
) -> list:
    """
    Check string for partial dictinary matches

    :param string: String to check
    :param words: Dictionary to check against
    :return: List of matches
    """
    print(f"Checking {string} for partial matches to dictionary...")
    string = string.lower()
    matches = difflib.get_close_matches(
        string, words, cutoff=cutoff, n=matches
    )
    return [
        x
        for x in matches
        if all(string.count(y) <= x.count(y) for y in string)
    ]


def dictcheck_portion(
    string: str, words: list, cutoff: float = 0.5, matches: int = 25
) -> list:
    """
    Check string for partial dictinary matches

    :param string: String to check
    :param words: Dictionary to check against
    :return: List of matches
    """
    print(f"Checking {string} for partial matches to dictionary...")
    string = string.lower()
    matches = difflib.get_close_matches(
        string, words, cutoff=cutoff, n=matches
    )
    return [
        x
        for x in matches
        if all(string.count(y) >= x.count(y) for y in string)
        and len(string) >= len(x)
        and not any(y not in string for y in x)
    ]
