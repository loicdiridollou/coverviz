from pathlib import Path
import json


def load_json(path: Path) -> dict:
    return json.load(path.open())
