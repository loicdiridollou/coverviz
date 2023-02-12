"""Test module for file.py."""
import json
from pathlib import Path

import coverviz.file as cf


def test_load_json(tmp_path: Path):
    """Testing file.load_json method."""
    tmp_file = tmp_path / "test_file.json"
    dictionary = {
        "name": "test",
        "rollno": 56,
        "phonenumber": "5376770500"
    }
    json_object = json.dumps(dictionary, indent=4)

    with tmp_file.open(mode="w") as outfile:
        outfile.write(json_object)

    cf.load_json(tmp_file)
