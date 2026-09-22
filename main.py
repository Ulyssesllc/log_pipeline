from pathlib import Path
from typing import Generator

import pandas as pd


def read_log(file_path: str) -> list[str]:
    print(f"Reading log file from: {file_path}")
    return []


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


def stream_log_file(log_file: str) -> Generator[str, None, None]:
    file_path = Path(log_file)
    if not file_path.exists():
        print(f"Cảnh báo: File '{log_file}' không tồn tại.")
        return

    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                yield line.strip()


def process_logs_vectorized(log_file: str) -> pd.DataFrame:
    file_path = Path(log_file)
    if not file_path.exists():
        return pd.DataFrame(columns=["level", "count"])

    # đảm bảo đọc nguyên từng dòng vào 1 cột raw_line
    df = pd.read_csv(
        log_file,
        header=None,
        names=["raw_line"],
        sep=r"\r?\n",
        engine="python",
        skip_blank_lines=True,
    )

    if df.empty:
        return pd.DataFrame(columns=["level", "count"])

    # Tách chuỗi thành tối đa 4 cột
    split_df = df["raw_line"].str.strip().str.split(" ", n=3, expand=True)

    # Đảm bảo đủ 4 cột nếu file có dòng log bị thiếu dữ liệu
    if split_df.shape[1] < 4:
        for col_idx in range(split_df.shape[1], 4):
            split_df[col_idx] = None

    df[["date", "time", "level", "message"]] = split_df.iloc[:, :4]

    # Lọc và thống kê lỗi
    error_mask = df["level"].isin(["ERROR", "CRITICAL"])
    summary = (
        df.loc[error_mask]
        .groupby("level", as_index=False)
        .size()
        .rename(columns={"size": "count"})
    )

    return summary


if __name__ == "__main__":
    read_log("app.log")
    # Main pipeline script
    try:
        sample = "2026-09-21 ERROR Database_timeout"
        result = validate_and_parse(sample)
        print("Kết quả parse:", result)
    except ValueError as err:
        print(f"Lỗi xử lý: {err}")

    print("\n===Đọc thử 3 dòng đầu qua Generator===")
    log_gen = stream_log_file("app.log")
    for _ in range(3):
        try:
            print(next(log_gen))
        except StopIteration:
            break

    print("\n=== Thống kê toàn bộ file log ===")
    summary_df: pd.DataFrame = process_logs_vectorized("app.log")
    print(summary_df)
