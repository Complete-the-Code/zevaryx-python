from itertools import permutations
from math import factorial
from sys import argv
from tqdm import tqdm

string = argv[1]

with open("words.txt") as f:
    words = [x.strip().lower() for x in f.readlines()]

matches = []

total = len(words)

for word in tqdm(
    words, total=total, desc="Analyzing Permutations", unit="words"
):
    if sorted(string.lower()) == sorted(word.lower()):
        matches.append(word)

print("\n".join(matches) if matches else "None found")
