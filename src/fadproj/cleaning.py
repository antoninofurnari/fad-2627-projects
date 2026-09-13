"""Cleaning steps, written so that the sample-size accounting comes for free.

Replace the example with your own steps. The point of the pattern is that every step
records how many rows it removed, so the table in the report cannot drift out of step
with what the code actually did.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class Accounting:
    """Record how many rows survive each cleaning step.

    >>> account = Accounting(df)
    >>> df = account.step("dropped duplicates", df.drop_duplicates())
    >>> account.table()
    """

    def __init__(self, frame: pd.DataFrame, label: str = "raw") -> None:
        self._rows: list[tuple[str, int]] = [(label, len(frame))]

    def step(self, label: str, frame: pd.DataFrame) -> pd.DataFrame:
        """Record the size of `frame` under `label` and return it unchanged."""
        self._rows.append((label, len(frame)))
        return frame

    def table(self) -> pd.DataFrame:
        """The accounting as a table, with the rows lost at each step."""
        out = pd.DataFrame(self._rows, columns=["step", "rows"])
        out["lost"] = out["rows"].shift().sub(out["rows"]).fillna(0).astype(int)
        out["share kept"] = (out["rows"] / out.loc[0, "rows"]).round(3)
        return out


def load_clean(path: str | Path, account: Accounting | None = None) -> pd.DataFrame:
    """Load the dataset and apply the cleaning both notebooks should share.

    Put your cleaning here rather than in a notebook cell, so Part 2 analyses the same
    frame Part 1 described. If you clean in the notebook, the two drift apart and the
    sample-size table in your report stops describing your data.

    Returns an **empty DataFrame** when the file is not there, instead of raising. A
    fork has an empty `data/` until someone runs `data/download.py`, and the notebooks
    have to survive a "Restart & Run All" in that state — that is what the repository
    check executes. An empty frame flows through the rest of the notebook as no rows;
    an exception stops it dead.

    >>> account = Accounting(pd.DataFrame())
    >>> df = load_clean("../data/your_dataset.csv", account)
    >>> account.table()
    """
    path = Path(path)
    if not path.exists():
        return pd.DataFrame()

    frame = pd.read_csv(path)
    if account is None:
        account = Accounting(frame)

    # ---------------------------------------------------------------- your steps here
    # Each one goes through `account.step`, so the table in the report is generated
    # from what the code did rather than typed by hand. For example:
    #
    #     frame = account.step("dropped duplicates", frame.drop_duplicates())
    #     frame = account.step("dropped rows with no outcome", frame.dropna(subset=["y"]))
    #
    # Removing rows is a decision: say in the report what the removed rows had in
    # common, not only how many there were.

    return frame
