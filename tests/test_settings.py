import pytest

from pipeline import settings

DT = "2026-11-15"


@pytest.mark.parametrize("root", ["./data", "r2://github-trends"])
def test_paths_follow_the_layout(monkeypatch, root):
    monkeypatch.setenv("DATA_ROOT", root)

    assert settings.raw_path(DT, 7) == f"{root}/raw/dt={DT}/07.parquet"
    assert settings.raw_path(DT, 23) == f"{root}/raw/dt={DT}/23.parquet"
    assert settings.stage_path(DT) == f"{root}/stage/events/dt={DT}/events.parquet"
    assert (
        settings.repo_daily_path(DT)
        == f"{root}/mart/repo_daily/dt={DT}/repo_daily.parquet"
    )
    assert (
        settings.top_repos_path(DT)
        == f"{root}/mart/top_repos/dt={DT}/top_repos.parquet"
    )
    assert settings.dashboard_path() == f"{root}/mart/dashboard/dashboard.parquet"


def test_default_root_is_local_data_folder(monkeypatch):
    monkeypatch.delenv("DATA_ROOT", raising=False)

    assert settings.data_root() == "./data"


def test_trailing_slash_is_removed(monkeypatch):
    monkeypatch.setenv("DATA_ROOT", "r2://github-trends/")

    assert settings.stage_path(DT) == (
        f"r2://github-trends/stage/events/dt={DT}/events.parquet"
    )
