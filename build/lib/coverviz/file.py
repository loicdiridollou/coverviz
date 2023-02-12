"""Experiment file."""
import json
from pathlib import Path


def load_json(path: Path) -> dict:
    """Data loader."""
    return json.load(path.open())
