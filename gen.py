from itertools import combinations, repeat
from multiprocessing import cpu_count
import os
import random
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map

THREADS = cpu_count() - 4


def get_random_color():
    return "#" + str(hex(random.randint(0, 16777215)))[2:]


def dictcheck(string: str, words: list, leave=True, position=0) -> list:
    """
    Check permutations of string for dictionary match

    :param string: String to check
    :param words: Dictionary to check against
    :return: List of matches
    """
    matches = []
    for word in words:
        if sorted(string.lower()) == sorted(word.lower()):
            matches.append(word)
    return matches


def dictcheck_chunk(minsize: int = 2) -> list:
    minsize_words = []
    combs = list(set("".join(c) for c in combinations(string, minsize)))

    r = process_map(
        dictcheck,
        combs,
        repeat(words),
        desc=f"Generating len{minsize}.txt",
        max_workers=THREADS,
        chunksize=THREADS // 4,
        leave=False,
    )
    for lst in r:
        minsize_words += lst
    if len(minsize_words) > 0:
        os.makedirs(f"gens/{string}", exist_ok=True)
        fpath = f"gens/{string}/len{minsize}.txt"
        with open(fpath, "w+") as f:
            f.write("\n".join(sorted(list(set(minsize_words)))))
    return minsize_words


def gen_lens(string: str, words: list, minsize: int = 2):
    for i in tqdm(
        range(minsize, len(string)),
        desc="Generating lenX.txt",
        unit="file",
    ):
        dictcheck_chunk(i)


with open("words.txt") as f:
    words = [x.strip() for x in f.readlines()]

string = "ACDDEEEEHLMOOOPRSTTTW"
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
gen_lens(string, words)
