import re
from typing import Optional

HASH_TYPE_REGEX = {
    re.compile(r"^[a-f0-9]{32}(:.+)?$", re.IGNORECASE): [
        "MD5",
        "MD4",
        "MD2",
        "Double MD5",
        "LM",
        "RIPEMD-128",
        "Haval-128",
        "Tiger-128",
        "Skein-256(128)",
        "Skein-512(128)",
        "Lotus Notes/Domino 5",
        "ZipMonster",
        "PrestaShop",
    ],
    re.compile(r"^[a-f0-9]{64}(:.+)?$", re.IGNORECASE): [
        "SHA-256",
        "RIPEMD-256",
        "SHA3-256",
        "Haval-256",
        "GOST R 34.11-94",
        "GOST CryptoPro S-Box",
        "Skein-256",
        "Skein-512(256)",
        "Ventrilo",
    ],
    re.compile(r"^[a-f0-9]{128}(:.+)?$", re.IGNORECASE): [
        "SHA-512",
        "Whirlpool",
        "Salsa10",
        "Salsa20",
        "SHA3-512",
        "Skein-512",
        "Skein-1024(512)",
    ],
    re.compile(r"^[a-f0-9]{56}$", re.IGNORECASE): [
        "SHA-224",
        "Haval-224",
        "SHA3-224",
        "Skein-256(224)",
        "Skein-512(224)",
    ],
    re.compile(r"^[a-f0-9]{40}(:.+)?$", re.IGNORECASE): [
        "SHA-1",
        "Double SHA-1",
        "RIPEMD-160",
        "Haval-160",
        "Tiger-160",
        "HAS-160",
        "Skein-256(160)",
        "Skein-512(160)",
    ],
    re.compile(r"^[a-f0-9]{96}$", re.IGNORECASE): [
        "SHA-384",
        "SHA3-384",
        "Skein-512(384)",
        "Skein-1024(384)",
    ],
    re.compile(r"^[a-f0-9]{16}$", re.IGNORECASE): [
        "DES(Oracle)",
        "Half MD5",
        "FNV-164",
        "CRC-64",
    ],
    re.compile(r"^[a-f0-9]{48}$", re.IGNORECASE): [
        "Haval-192",
        "Tiger-192",
        "SHA-1(Oracle)",
        "XSHA (v10.4 - v10.6)",
    ],
}


def menu(strings: list):
    while True:
        print(
            """
 Choose an option:

 1) Check strings for hash matches

 0) Go back
        """
        )
        choice = input("> ")
        if choice == "1":
            results = {k: is_hash(k) for k in strings}
            for k in results:
                rstr = (
                    "\n  ".join(x for x in results[k])
                    if results[k]
                    else "Not a hash"
                )
                print(f"\n{k}:\n  {rstr}")
        elif choice == "0":
            break


def is_hash(string: str) -> Optional[list]:
    """
    Checks if a string is a hash of some sort

    :param string: String to check
    :return: The matching hash function(s)
    """
    for algo in HASH_TYPE_REGEX:
        if algo.match(string.lower()):
            return HASH_TYPE_REGEX[algo]
