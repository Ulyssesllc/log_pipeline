
# Log Processing Pipeline

Hệ thống xử lý và thống kê file log tự động kết hợp giữa Shell Script an toàn và Pandas Vectorization.

## Yêu cầu Hệ thống
- Python 3.10+
- Pandas &gt;= 2.0.0

## Cài đặt
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

## Khởi chạy Pipeline

Chạy kịch bản tự động duy nhất:

```
./run_pipeline.sh

```

## Cấu trúc Dự án

* `main.py`: Module kiểm tra lỗi bằng lập trình phòng thủ &amp; thống kê Pandas.
* `test_main.py`: Bộ kiểm thử Unit Test cho các trường hợp biên.
* `run_pipeline.sh`: Kịch bản điều khiển pipeline bằng Bash (Strict mode).
* `pyproject.toml` &amp; `requirements.txt`: Khai báo phụ thuộc và cấu hình linter/type checker. EOF



