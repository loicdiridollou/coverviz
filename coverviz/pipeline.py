"""Full pipeline for coverviz."""
from pathlib import Path

import coverviz.preprocessing as cpre


def load_and_generate(path: Path):
    """Pipeline for the process."""
    data = cpre.load_json(path)
    return len(data)
