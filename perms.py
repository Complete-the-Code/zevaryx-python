import difflib
import argparse


parser = argparse.ArgumentParser(description="Get close matches")
parser.add_argument("strings", type=str, nargs="+", help="Strings to parse")
parser.add_argument(
    "-c",
    "--cutoff",
    dest="cutoff",
    default=0.5,
    type=float,
    help="Percentage of match for match cutoff (i.e. 0.5)",
)
parser.add_argument(
    "-m",
    "--matches",
    dest="matches",
    default=25,
    type=int,
    help="How many matches to return",
)

args = parser.parse_args()


with open("words.txt") as f:
    words = list(set([x.strip().lower() for x in f.readlines()]))

for string in args.strings:
    print(
        f"\nGetting close matches for {string} (cutoff={args.cutoff}, matches={args.matches})"
    )
    string = string.lower()
    matches = difflib.get_close_matches(
        string, words, cutoff=args.cutoff, n=args.matches
    )
    true_matches = [x for x in matches if all(y in x for y in string)]
    print("\n".join(x for x in true_matches))
