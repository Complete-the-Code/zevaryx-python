from glob import glob
import csv
from tqdm import tqdm

string = "ACDDEEEEHLMOOOPRSTTTW"


def check_valid(word, remainder):
    return "".join(sorted(word)) in "".join(sorted(remainder))


def get_diff(word):
    loc_string = string
    for char in word:
        loc_string = loc_string.replace(char, "", 1)
    return loc_string


def gen_doubles(words):
    solutions = {}
    old_len = 0
    cur_len = 0
    for word in tqdm(
        words, total=len(words), desc="Generating doubles", unit="words"
    ):
        diff = get_diff(word)
        tmp_words = [x for x in words if not x == word]
        for word2 in tqdm(
            tmp_words,
            total=len(tmp_words),
            desc=f"Checking {word}",
            unit="doubles",
            leave=False,
        ):
            # Inline de-dup while validating
            sorted_key = " ".join(sorted([word, word2]))
            if check_valid(word2, diff):
                diff2 = get_diff(word + word2)
                solutions[sorted_key] = diff2
    return solutions


def gen_triples(words):
    solutions = {}
    for word in tqdm(
        words, total=len(words), desc="Generating Triples", unit="words"
    ):
        diff = get_diff(word)
        tmp_words = [x for x in words if not x == word]
        for word2 in tqdm(
            tmp_words,
            total=len(tmp_words),
            desc=f"Checking {word}",
            unit="combinations",
            leave=False,
        ):
            # Inline de-dup while validating

            if check_valid(word2, diff):
                tmp_words2 = [x for x in tmp_words if not x == word2]
                for word3 in tqdm(
                    tmp_words2,
                    total=len(tmp_words2),
                    desc=f"Checking {word2}",
                    unit="triples",
                    leave=False,
                    position=2,
                ):
                    diff2 = get_diff(word + word2)
                    sorted_key = " ".join(sorted([word, word2, word3]))
                    if check_valid(word3, diff2):
                        diff3 = get_diff(word + word2 + word3)
                        solutions[sorted_key] = diff3
    return solutions


words = ["THE"]

for file in glob(f"gens/{string}/len*.txt"):
    with open(file) as f:
        words += sorted([x.strip().upper() for x in f.readlines()])

words = sorted(sorted(list(set(words))), key=len)
solutions = gen_triples(words)

# Dedup solutions
# processed = []
# keys = []
# for solution in tqdm(
#     solutions,
#     total=len(solutions),
#     desc="Deduplicating solutions",
#     unit="words",
# ):
#     s = " ".join(sorted(solution["Words"].split(" ")))
#     if s not in keys:
#         processed.append({"Words": s, "Remainder": solution["Remainder"]})
#         keys.append(s)
#
# solutions = processed

with open("diffs_tripleword.csv", "w+", newline="") as f:
    writer = csv.writer(f, dialect="excel", quotechar='"')
    writer.writerow(("Words", "Remainder"))
    for solution in solutions:
        writer.writerow((solution, solutions[solution]))
