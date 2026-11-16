"""Settings and file paths. Every path in the project is built here.

DATA_ROOT decides where the data lives: a local folder on the laptop
(default ./data) or r2://github-trends in production. Paths are built with
string formatting, not os.path or pathlib, because those break "r2://".
"""

import os


def data_root() -> str:
    """Return DATA_ROOT from the environment, without a trailing slash."""
    return os.environ.get("DATA_ROOT", "./data").rstrip("/")


def raw_path(dt: str, hour: int) -> str:
    return f"{data_root()}/raw/dt={dt}/{hour:02d}.parquet"


def stage_path(dt: str) -> str:
    return f"{data_root()}/stage/events/dt={dt}/events.parquet"


def repo_daily_path(dt: str) -> str:
    return f"{data_root()}/mart/repo_daily/dt={dt}/repo_daily.parquet"


def top_repos_path(dt: str) -> str:
    return f"{data_root()}/mart/top_repos/dt={dt}/top_repos.parquet"


def dashboard_path() -> str:
    return f"{data_root()}/mart/dashboard/dashboard.parquet"
