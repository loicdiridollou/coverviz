"""Module with the old functions for experiments."""
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict:
    """Loader for json coverage file."""
    return json.load(path.open())


def clean_up_json(dic: dict[str, dict]) -> dict:
    """Clean up coverage file."""
    dic_res = {}

    for fname in dic["files"]:
        res = fname.split("/")
        root = dic_res
        for j, wrd in enumerate(res):
            if j == len(res) - 1:
                root[wrd] = [dic["files"][fname]["summary"]["covered_lines"],
                             dic["files"][fname]["summary"]["num_statements"]]
            else:
                if wrd not in root:
                    root[wrd] = {}
                root = root[wrd]

    return dic_res


def identify_modules(dic: dict[str, Any], path: str = ""):
    """Find the modules and coverage."""
    res = []
    for key in dic:
        if isinstance(dic[key], dict) and key != "tests":
            res.append([f"{path}/{key}", generate_coverage(dic[key])])
            res += identify_modules(dic[key], f"{path}/{key}")
        if isinstance(dic[key], list):
            res.append([f"{path}/{key}", dic[key]])

    return res


def generate_coverage(dic):
    """Generate module coverages."""
    lines = 0
    coverred = 0
    for key in dic:
        if isinstance(dic[key], dict) and key != "tests":
            cov, tot = generate_coverage(dic[key])
            coverred += cov
            lines += tot
        elif isinstance(dic[key], list):
            coverred += dic[key][0]
            lines += dic[key][1]

    return [coverred, lines]


def split_coverage(lst: list):
    """Generate trie structure of the coverage."""
    res = {}
    for idx, value in lst:
        idx = idx.split("/")
        root = res
        while idx:
            elm = idx[0]
            idx = idx[1:]
            if elm not in root:
                root[elm] = {}
            root = root[elm]
        root["coverage"] = value
    return res


def generate_coverage_level(dic: dict[str, Any], prefix):
    """Generate data for the files and sub modules."""
    res = {}
    route = prefix.split(".")
    for elm in route:
        dic = dic[elm]

    for key in dic:
        if key != "coverage":
            res[key] = dic[key]["coverage"]

    return res
