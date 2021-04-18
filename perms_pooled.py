import difflib
from itertools import permutations
from math import factorial
import numpy as np
from sys import argv
from tqdm import tqdm
import multiprocessing as mp
from multiprocessing import Pool, Manager

string = argv[1]
MAX_POOLS = mp.cpu_count() // 2  # Real cores only


def get_match(perm, word):
    return difflib.SequenceMatcher(None, perm, word).ratio()


with open("words.txt") as f:
    words = [x.strip() for x in f.readlines()]

manager = Manager()

highest_percs = manager.dict()
highest_matches = manager.dict()


def process(perms):
    cp = mp.current_process().name
    for idx, perm in enumerate(perms):
        if idx % 10 == 0:
            print(f"[{cp}] {idx}/{len(perms)} processed")
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


all_perms = ["".join(x) for x in permutations(string)]

splits = list(np.array_split(np.array(all_perms), MAX_POOLS))

with Pool(MAX_POOLS) as p:
    p.map(process, splits)

sorted_percs = {
    k: v for k, v in sorted(highest_percs.items(), key=lambda item: item[1])
}

for i in range(10):
    k = list(sorted_percs.keys())[i]
    print(f"{k}: {highest_matches[k]}")
