import argparse
import json
import logging
from collections.abc import Generator
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def validate_and_parse(line: str) -> dict[str, str]:
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("Dòng log rỗng!")

    # n=3 để chỉ tách 3 khoảng trắng đầu tiên, phần còn lại giữ nguyên làm message
    parts = cleaned.split(" ", maxsplit=3)
    if len(parts) < 4:
        raise ValueError(f"Dòng log không đúng cấu trúc 4 phần: {line.strip()}")

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3],
    }


def stream_log_file(log_file: Path) -> Generator[str, None, None]:
    if not log_file.exists():
        raise FileNotFoundError(f"Tệp log không tồn tại: {log_file}")
    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                yield line.strip()


def process_logs_vectorized(log_file: Path) -> pd.DataFrame:
    if not log_file.exists():
        raise FileNotFoundError(f"Tệp log không tồn tại: {log_file}")

    df: pd.DataFrame = pd.read_csv(
        log_file,
        header=None,
        names=["raw_line"],
        engine="python",
    )
    split_df = df["raw_line"].str.split(" ", n=3, expand=True)
    df[["date", "time", "level", "message"]] = split_df
    error_df: pd.DataFrame = df.loc[df["level"].isin(["ERROR", "CRITICAL"])]
    summary: pd.DataFrame = error_df.groupby("level").size().reset_index(name="count")
    return summary


def export_reports(summary_df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "summary.csv"
    json_path = output_dir / "summary.json"

    summary_df.to_csv(csv_path, index=False)

    summary_dict = summary_df.to_dict(orient="records")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary_dict, f, indent=4, ensure_ascii=False)

    logger.info(f"Đã xuất báo cáo CSV: {csv_path}")
    logger.info(f"Đã xuất báo cáo JSON: {json_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Log Processing Pipelime CLI - Phân tích và thống kê log hệ thống"
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=Path("app.log"),
        help="Đường dẫn tới file log đầu vào (Mặc định: app.log)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("reports"),
        help="Thư mục lưu báo cáo kết quả (Mặc định: reports),",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Hiển thị log chi tiết (Debug level)",
    )
    args = parser.parse_args()
    setup_logging(args.verbose)

    logger.info("Starting Log Processing Pipeline CLI...")
    logger.debug(f"Input file: {args.input}, Output directory: {args.output_dir}")

    try:
        summary_df = process_logs_vectorized(args.input)
        logger.info("Xử lí log hoàn tất thành công.")
        export_reports(summary_df, args.output_dir)
    except (FileNotFoundError, OSError, ValueError) as e:
        logger.error(f"Lỗi khi xử lí pipeline: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
