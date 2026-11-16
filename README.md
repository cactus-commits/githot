# GitHot

A small data pipeline that shows which GitHub repositories are trending, built to cost nothing to run.

Once a day it takes all public GitHub events from [GH Archive](https://www.gharchive.org/), cleans them with SQL in three layers (RAW → STAGE → MART), and shows the result in a dashboard.

## Status



## Planned stack

| Part | Tool |
|---|---|
| Language | Python, managed with `uv` |
| Transformations | SQL files run by DuckDB |
| File format | Parquet |
| Storage | Cloudflare R2 |
| Daily schedule | GitHub Actions |
| Dashboard | Streamlit Community Cloud |

## How to run


Needs [uv](https://docs.astral.sh/uv/). From the repo root:

```
uv sync               # install Python packages into .venv
uv run pytest         # run the tests
uv run ruff check .   # check code style
```
