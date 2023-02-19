"""Module with plotting functions."""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import squarify


def prepare_data(dic: dict[str, list[int]]) -> tuple[list, list, list]:
    """Prepare data for plotting."""
    modules = list(dic.keys())
    sizes = []
    coverage = []
    colors = []
    cmap = sn.color_palette("RdYlGn", 101).as_hex()

    for i, key in enumerate(modules):
        sizes.append(dic[key][1] or 1)
        coverage.append(dic[key][0] / (dic[key][1] or 1))
        modules[i] = f"{modules[i]}\n{coverage[i]:.0%}"
        colors.append(cmap[int(100 * coverage[i])])

    return modules, sizes, colors


def treemap(sizes, labels: list | None = None, colors: list | None = None,
            title: str | None = None) -> plt.FigureBase:
    """Draw treemap of the coverage."""
    fig = plt.figure(figsize=(15, 10))
    squarify.plot(sizes, label=labels, color=colors, edgecolor="white")
    plt.axis("off")
    if title:
        plt.title(title)

    return fig


def barh(sizes: list[int], labels: list[str], colors: list | None = None,
         title: str = "") -> plt.FigureBase:
    """Draew horizontal bar graph of the coverage."""
    # Example data
    y_pos = np.arange(len(labels))

    subplots = plt.subplots(figsize=(15, 10))
    fig: plt.FigureBase = subplots[0]
    ax: plt.Axes = subplots[1]

    y_labels = [label.split("\n")[0] for label in labels]
    bar_labels = [label.split("\n")[1] for label in labels]

    hbars = ax.barh(y_pos, sizes, color=colors, align="center")
    ax.set_yticks(y_pos, labels=y_labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.bar_label(hbars, labels=bar_labels, label_type="center")
    ax.set_xlabel("Number of lines in the module/file.")
    ax.set_title(title)

    return fig
