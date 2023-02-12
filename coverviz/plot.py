"""Module with plotting functions."""
import seaborn as sn


def prepare_data(dic: dict[str, list[int]]) -> tuple[list, list, list]:
    """Prepare data for plotting."""
    modules = list(dic.keys())
    sizes = []
    coverage = []
    colors = []
    cmap = sn.color_palette("RdYlGn", len(modules)).as_hex()

    for i, key in enumerate(modules):
        sizes.append(dic[key][1] or 1)
        coverage.append(dic[key][0] / (dic[key][1] or 1))
        modules[i] = f"{modules[i]}\n{coverage[i]:.0%}"

    sorted_cov = sorted(coverage)
    for i in range(len(modules)):
        colors.append(cmap[sorted_cov.index(coverage[i])])

    return modules, sizes, colors
