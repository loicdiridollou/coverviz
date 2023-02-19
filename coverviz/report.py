"""Module to generate the pdf report with all coverage."""
from matplotlib.backends.backend_pgf import PdfPages


def save_report(filename, figs):
    """Save list of figures to PDF report."""
    p = PdfPages(filename)
    for fig in figs:
        fig.savefig(p, format="pdf")
    p.close()
