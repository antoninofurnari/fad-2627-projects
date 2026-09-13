"""Functions shared by the two notebooks.

Anything used in both `part1_analysis.ipynb` and `part2_modelling.ipynb` belongs here,
imported rather than copy-pasted. Import it from a notebook with:

    import sys
    sys.path.append("../src")
    from fadproj import Accounting, load_clean

Keep the functions small and give them docstrings: this module is read during marking.
"""

from fadproj.cleaning import Accounting, load_clean

__all__ = ["Accounting", "load_clean"]
