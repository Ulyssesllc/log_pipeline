from pathlib import Path

import pytest

from main import (
    export_reports,
    main,
    process_logs_vectorized,
    setup_logging,
    stream_log_file,
    validate_and_parse,
)


def test_validate_and_parse_valid() -> None:
    line = "2026-09-21 10:00:00 ERROR Database_timeout"
    result = validate_and_parse(line)
    assert result["date"] == "2026-09-21"
    assert result["time"] == "10:00:00"
    assert result["level"] == "ERROR"
    assert result["message"] == "Database_timeout"


def test_validate_and_parse_invalid_columns() -> None:
    invalid_line = "2026-09-21 ERROR"
    with pytest.raises(ValueError, match="Dòng log không đúng cấu trúc"):
        validate_and_parse(invalid_line)


def test_stream_log_file(tmp_path: Path) -> None:
    log_file = tmp_path / "stream.log"
    log_file.write_text("line1\n\nline2\n", encoding="utf-8")
    lines = list(stream_log_file(log_file))
    assert lines == ["line1", "line2"]


def test_stream_log_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        list(stream_log_file(Path("missing.log")))


def test_process_logs_nonexistent_file() -> None:
    fake_path = Path("nonexistent_log_file.log")
    with pytest.raises(FileNotFoundError):
        process_logs_vectorized(fake_path)


def test_process_logs_and_export(tmp_path: Path) -> None:
    log_file = tmp_path / "test_app.log"
    log_content = (
        "2026-09-21 10:00:00 ERROR DB_Connection_Failed\n"
        "2026-09-21 10:05:00 INFO System_Started\n"
        "2026-09-21 10:10:00 CRITICAL Out_Of_Memory\n"
    )
    log_file.write_text(log_content, encoding="utf-8")

    summary_df = process_logs_vectorized(log_file)
    assert not summary_df.empty
    assert len(summary_df) == 2

    output_dir = tmp_path / "reports"
    export_reports(summary_df, output_dir)

    assert (output_dir / "summary.csv").exists()
    assert (output_dir / "summary.json").exists()


def test_setup_logging() -> None:
    setup_logging(verbose=True)
    setup_logging(verbose=False)


def test_main_cli_execution(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    log_file = tmp_path / "cli_app.log"
    log_file.write_text("2026-09-21 10:00:00 ERROR Test_Error\n", encoding="utf-8")
    output_dir = tmp_path / "cli_reports"

    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "-i", str(log_file), "-o", str(output_dir), "-v"],
    )
    main()

    assert (output_dir / "summary.csv").exists()
