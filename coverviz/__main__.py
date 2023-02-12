"""Top-level code to generate report."""
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path


def main():
    """Orchestrate method."""
    args = parse_args()
    print(args.file_path)


def parse_args(args: list[str] | None = None):
    """Argument parser to locate coverage json file and report type."""
    desc = "Generating visual report about test coverage."""
    parser = ArgumentParser(description=desc, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("--file-path", type=Path, default=Path("./coverage.json"))
    parser.add_argument("--report-type", nargs="+", default=["treemap"])

    return parser.parse_args(args)


if __name__ == "__main__":
    sys.exit(main())
