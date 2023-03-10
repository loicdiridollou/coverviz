"""Top-level code to generate report."""
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path

import coverviz.plot as cplt
import coverviz.preprocessing as om
from coverviz.preprocessing import clean_up_json, load_json
from coverviz.report import save_report


def main():
    """Main orchestration function."""
    args = parse_args()
    generate_treemap(args)
    generate_barh(args)


def generate_treemap(args):
    """Generate treemap graphs."""
    cov = Path("./coverage.json")
    cov_data = load_json(cov)
    vv = clean_up_json(cov_data)
    res = om.identify_modules(vv)
    new = om.split_coverage(res)
    list_modules = om.identify_modules_2(vv)

    import pdb; pdb.set_trace()
    figs = []
    for module in list_modules:
        mod_name = module[1:].replace("/", ".")
        fin = om.generate_coverage_level(new[""], mod_name)
        modules, sizes, colors = cplt.prepare_data(fin)
        title = mod_name.replace(args.prefix, "")[1:]
        figs.append(cplt.treemap(sizes, modules, colors, title=f"Coverage for {title}"))

    save_report(args.output + "11.pdf", figs)


def generate_barh(args):
    """Generate horizontal bar graphs."""
    cov = Path("./coverage.json")
    cov_data = load_json(cov)
    vv = clean_up_json(cov_data)
    res = om.identify_modules(vv)
    new = om.split_coverage(res)
    list_modules = om.identify_modules_2(vv)

    figs = []
    for module in list_modules:
        mod_name = module[1:].replace("/", ".")
        fin = om.generate_coverage_level(new[""], mod_name)
        modules, sizes, colors = cplt.prepare_data(fin)
        title = mod_name.replace(args.prefix, "")[1:]
        figs.append(cplt.barh(sizes, modules, colors, title=f"Coverage for {title}"))

    save_report(args.output + "22.pdf", figs)


def parse_args(args: list[str] | None = None):
    """Argument parser to locate coverage json file and report type."""
    desc = "Generating visual report about test coverage."""
    parser = ArgumentParser(description=desc, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("--file-path", type=Path, default=Path("./coverage.json"))
    parser.add_argument("--report-type", nargs="+", default=["treemap"])
    parser.add_argument("--prefix", type=str, default="")
    parser.add_argument("--output", type=str, default="report.pdf")

    return parser.parse_args(args)


if __name__ == "__main__":
    sys.exit(main())
