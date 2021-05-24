import csv
import os
from sys import argv
from tqdm import tqdm

if not os.path.exists("split/"):
    os.mkdir("split")

file = argv[1]
with open(file) as f:
    for i, _ in enumerate(f):
        pass
    total = i
with open(file) as f:
    reader = csv.DictReader(f)
    file_no = 0
    current_file = open(
        f"split/{file.split('.')[0]}_{file_no}.csv", "w+", newline=""
    )
    writer = csv.DictWriter(current_file, fieldnames=["Words", "Remainder"])
    writer.writeheader()
    for row in tqdm(reader, desc=f"Splitting {file}", total=total, unit="row"):
        if (
            reader.line_num % 2_500_000 == 0
        ):  # Google Sheets max cell count is 5M
            current_file.close()
            file_no += 1
            current_file = open(
                f"split/{file.split('.')[0]}_{file_no}.csv", "w+", newline=""
            )
            writer = csv.DictWriter(
                current_file, fieldnames=["Words", "Remainder"]
            )
            writer.writeheader()
        writer.writerow(row)
