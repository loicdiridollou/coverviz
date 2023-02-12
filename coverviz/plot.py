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
    cmap = sn.color_palette("RdYlGn", len(modules)).as_hex()

    for i, key in enumerate(modules):
        sizes.append(dic[key][1] or 1)
        coverage.append(dic[key][0] / (dic[key][1] or 1))
        modules[i] = f"{modules[i]}\n{coverage[i]:.0%}"

    sorted_cov = sorted(coverage)
    for i in range(len(modules)):
        colors.append(cmap[sorted_cov.index(coverage[i])])

    return modules, sizes, colors


def treemap(sizes, labels: list | None = None, colors: list | None = None):
    """Draw treemap of the coverage."""
    fig = plt.figure(figsize=(15, 10))  # noqa
    squarify.plot(sizes, label=labels, color=colors, edgecolor="white")
    plt.axis("off")
    plt.show()


def sunburst(nodes, total=np.pi * 2, offset=0, level=0):
    """Draw sunburst plot of the coverage."""
    ax = plt.subplot(111, projection="polar")

    if level == 0 and len(nodes) == 1:
        label, value, subnodes = nodes[0]
        ax.bar([0], [0.5], [np.pi * 2])
        ax.text(0, 0, label, ha="center", va="center")
        sunburst(subnodes, total=value, level=level + 1, ax=ax)
    elif nodes:
        d = np.pi * 2 / total
        labels = []
        widths = []
        local_offset = offset
        for label, value, subnodes in nodes:
            labels.append(label)
            widths.append(value * d)
            sunburst(subnodes, total=total, offset=local_offset,
                     level=level + 1, ax=ax)
            local_offset += value
        values = np.cumsum([offset * d] + widths[:-1])
        heights = [1] * len(nodes)
        bottoms = np.zeros(len(nodes)) + level - 0.5
        rects = ax.bar(values, heights, widths, bottoms, linewidth=1,
                       edgecolor="white", align="edge")
        for rect, label in zip(rects, labels, strict=True):
            x = rect.get_x() + rect.get_width() / 2
            y = rect.get_y() + rect.get_height() / 2
            rotation = (90 + (360 - np.degrees(x) % 180)) % 360
            ax.text(x, y, label, rotation=rotation, ha="center", va="center")

    if level == 0:
        ax.set_theta_direction(-1)
        ax.set_theta_zero_location("N")
        ax.set_axis_off()

    plt.show()
