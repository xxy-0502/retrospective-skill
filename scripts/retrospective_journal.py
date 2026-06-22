#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create deterministic folders and placeholder files for retrospectives."""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime
from pathlib import Path


def parse_date(value: str | None) -> date:
    if not value:
        return date.today()
    return datetime.strptime(value, "%Y-%m-%d").date()


def build_paths(root: Path, entry_date: date) -> dict[str, Path | str | int]:
    iso_year, iso_week, _ = entry_date.isocalendar()
    year = f"{entry_date.year:04d}"
    month = f"{entry_date.year:04d}-{entry_date.month:02d}"
    week = f"{iso_year:04d}-W{iso_week:02d}"

    year_dir = root / year
    month_dir = year_dir / month
    week_dir = month_dir / week

    return {
        "date": entry_date.isoformat(),
        "year": year,
        "month": month,
        "iso_year": iso_year,
        "iso_week": iso_week,
        "week": week,
        "year_dir": year_dir,
        "month_dir": month_dir,
        "week_dir": week_dir,
        "daily_path": week_dir / f"{entry_date.isoformat()}.md",
        "week_summary_path": week_dir / "week-summary.md",
        "month_summary_path": month_dir / "month-summary.md",
        "year_summary_path": year_dir / "year-summary.md",
    }


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def daily_template(entry_date: date, week: str, month: str) -> str:
    return f"""# 每日复盘 - {entry_date.isoformat()}

元数据：

- 日期：{entry_date.isoformat()}
- 月份：{month}
- 周次：{week}

## 原始记录

未提供。

## 我做了什么

- 未提供。

## 今日状态

- 精力：未提供。
- 情绪：未提供。
- 专注：未提供。
- 压力：未提供。

## AI复盘

### 总结

待填写。

### 信号

- 待填写。

### 做得好的地方

- 待填写。

### 做得不好的地方

- 待填写。

### KISS 明日行动

#### Keep｜继续保持

- 待填写。

#### Improve｜需要改进

- 待填写。

#### Start｜开始做

- 待填写。

#### Stop｜停止做

- 待填写。

### 下一步行动

- 待填写。
"""


def week_template(week: str) -> str:
    return f"""# 周总结 - {week}

## 本周发生了什么

- 待总结。

## 亮点

- 待总结。

## 阻力

- 待总结。

## 模式观察

- 待总结。

## 下周实验

- 待总结。
"""


def month_template(month: str) -> str:
    return f"""# 月总结 - {month}

## 本月证据

- 待总结。

## 能力增长

- 待总结。

## 代价

- 待总结。

## 系统修正

- 待总结。

## 下月重点

- 待总结。
"""


def year_template(year: str) -> str:
    return f"""# 年总结 - {year}

## 年度证据

- 待总结。

## 主要项目与结果

- 待总结。

## 身份与习惯变化

- 待总结。

## 反复出现的课题

- 待总结。

## 下一年战略重点

- 待总结。
"""


def create_files(paths: dict[str, Path | str | int]) -> None:
    week_dir = paths["week_dir"]
    if not isinstance(week_dir, Path):
        raise TypeError("week_dir must be a Path")

    week_dir.mkdir(parents=True, exist_ok=True)

    daily_path = paths["daily_path"]
    week_summary_path = paths["week_summary_path"]
    month_summary_path = paths["month_summary_path"]
    year_summary_path = paths["year_summary_path"]
    if not all(isinstance(p, Path) for p in [daily_path, week_summary_path, month_summary_path, year_summary_path]):
        raise TypeError("output paths must be Path objects")

    entry_date = datetime.strptime(str(paths["date"]), "%Y-%m-%d").date()
    write_if_missing(daily_path, daily_template(entry_date, str(paths["week"]), str(paths["month"])))
    write_if_missing(week_summary_path, week_template(str(paths["week"])))
    write_if_missing(month_summary_path, month_template(str(paths["month"])))
    write_if_missing(year_summary_path, year_template(str(paths["year"])))


def serializable(paths: dict[str, Path | str | int]) -> dict[str, str | int]:
    result: dict[str, str | int] = {}
    for key, value in paths.items():
        result[key] = str(value) if isinstance(value, Path) else value
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Create retrospective journal folders and placeholder files.")
    parser.add_argument("--root", default="reviews", help="Root folder for retrospective files.")
    parser.add_argument("--date", help="Entry date in YYYY-MM-DD format. Defaults to today.")
    parser.add_argument("--create", action="store_true", help="Create folders and placeholder files if missing.")
    args = parser.parse_args()

    root = Path(args.root)
    entry_date = parse_date(args.date)
    paths = build_paths(root, entry_date)

    if args.create:
        create_files(paths)

    print(json.dumps(serializable(paths), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
