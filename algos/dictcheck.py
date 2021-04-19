import difflib
from tqdm import tqdm


def menu(strings: list, words: list):
    while True:
        print(
            """
 Choose an option:

 1) Check direct dictionary matches
 2) Check partial dictionary matches

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
        elif choice == "0":
            break


def dictcheck(string: str, words: list) -> list:
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
