from base64 import b32decode
from itertools import permutations
from math import factorial
from sys import argv
from tqdm import tqdm

string = argv[1]
with open("words.txt") as f:
    words = [x.strip() for x in f.readlines()]


def pad(string):
    if (missing := len(string) % 8) != 0:
        string += "=" * (8 - missing)
    return string


total = factorial(len(string))

for p in tqdm(
    permutations(string), total=total, desc="Analyzing Permutations"
):
    perm = "".join(p)
    perm = pad(perm)
    if (word := str(b32decode(perm))) in words:
        print(word)
