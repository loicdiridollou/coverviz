"""Top-level code to generate report."""
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path

import coverviz.plot as cplt
import coverviz.preprocessing as om
from coverviz.preprocessing import clean_up_json, load_json


def main():
    """Orchestrate method."""
    args = parse_args()

    cov = Path("./coverage.json")
    cov_data = load_json(cov)
    vv = clean_up_json(cov_data)
    res = om.identify_modules(vv)
    new = om.split_coverage(res)
    fin = om.generate_coverage_level(new[""], args.prefix)
    modules, sizes, colors = cplt.prepare_data(fin)
    cplt.treemap(sizes, modules, colors)


def parse_args(args: list[str] | None = None):
    """Argument parser to locate coverage json file and report type."""
    desc = "Generating visual report about test coverage."""
    parser = ArgumentParser(description=desc, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("--file-path", type=Path, default=Path("./coverage.json"))
    parser.add_argument("--report-type", nargs="+", default=["treemap"])
    parser.add_argument("--prefix", type=str)

    return parser.parse_args(args)


if __name__ == "__main__":
    sys.exit(main())
