from itertools import permutations
from math import factorial
from tqdm import tqdm

strings = ["EDOTCOM", "YDOTCOM", "EDOTCOR", "YDOTCOR", "EDOTCOMYR"]

exts = ["gif", "png", "jpg", "wav", "mp4", "mp3", "txt"]

total = sum(factorial(len(string)) for string in strings) * len(exts)

perms = []

pbar = tqdm(desc="Getting Permutations", total=total)

for string in strings:
    for p in permutations(string):
        perm = "".join(p)
        for ext in exts:
            pbar.update(1)
            perms.append(perm + "." + ext)

with open("all_with_exts.txt", "w+") as f:
    f.write("\n".join(perms))
