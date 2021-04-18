import difflib
from itertools import permutations
from math import factorial
from sys import argv
from tqdm import tqdm

string = argv[1]


def get_match(perm, word):
    return difflib.SequenceMatcher(None, perm, word).ratio()


with open("words.txt") as f:
    words = [x.strip() for x in f.readlines()]

highest_percs = {}
highest_matches = {}

total = factorial(len(string))

for p in tqdm(
    permutations(string), total=total, desc="Analyzing Permutations"
):
    perm = "".join(p)
    highscore = 0
    highest = None
    for word in words:
        if (score := get_match(perm, word)) > highscore:
            highscore = score
            highest = word
        elif score == highscore:
            if type(highest) is str:
                highest = [highest, word]
            elif type(highest) is list:
                highest.append(word)
    highest_percs[perm] = highscore
    highest_matches[perm] = highest

sorted_percs = {
    k: v for k, v in sorted(highest_percs.items(), key=lambda item: item[1])
}

for i in range(10):
    k = list(sorted_percs.keys())[i]
    print(f"{k}: {highest_matches[k]}")
