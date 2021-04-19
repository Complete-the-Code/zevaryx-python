from hashlib import sha256
from pathlib import Path
import requests
from tqdm import tqdm

BSIZE = 65536


def download_update(filepath: str = "words.txt") -> bool:
    """
    Download an update to the words file

    :param filepath: Path to dictionary file
    :return: If download was needed
    """
    fpath = Path(filepath)
    if fpath.exists():
        if fpath.is_dir():
            raise ValueError("Filepath is a folder, not a file")
        return False

    data = requests.get(
        "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt",
        stream=True,
    )
    data.raise_for_status()
    size = int(data.headers.get("content-length", 0))
    with tqdm(
        total=size, unit="iB", unit_scale=True, desc="Downloading words.txt"
    ) as t:
        with fpath.open(mode="w+") as f:
            for chunk in data.iter_content(BSIZE):
                t.update(len(chunk))
                f.write(chunk.decode("UTF-8"))
    return True


def get_words(filepath: str = "words.txt") -> list:
    """
    Read the dictionary file

    :param filepath: Path to the dictionary file
    :return: List of words
    """
    fpath = Path(filepath)
    if not fpath.exists():
        raise FileNotFoundError(f"Specified dictionary ({filepath}) not found")

    if fpath.is_dir():
        raise ValueError("Filepath is a folder, not a file")

    with fpath.open() as f:
        words = list(set([x.strip() for x in f.readlines()]))

    return words
