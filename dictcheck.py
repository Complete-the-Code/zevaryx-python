from itertools import permutations
from math import factorial
from sys import argv
from tqdm import tqdm

string = argv[1]

with open("words.txt") as f:
    words = [x.strip().lower() for x in f.readlines()]

matches = []

total = factorial(len(string))

for p in tqdm(
    permutations(string), total=total, desc="Analyzing Permutations"
):
    perm = "".join(p)
    if perm.lower() in words:
        matches.append(perm)

print("\n".join(matches) if matches else "None found")
