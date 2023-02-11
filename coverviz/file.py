from pathlib import Path
import json


def load_json(path: Path) -> dict:
    return json.load(path.open())


if __name__ == "__main__":
    load_json(Path('.'))
