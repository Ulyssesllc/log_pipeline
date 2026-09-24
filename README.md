# 🚀 Log Processing Pipeline (`log-pipeline`)

[![CI](https://github.com/Ulyssesllc/log_pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/Ulyssesllc/log_pipeline/actions)
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![Coverage](https://img.shields.io/badge/coverage-92%25-brightgreen.svg)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)
![Mypy](https://img.shields.io/badge/mypy-checked-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Log Processing Pipeline** là một công cụ dòng lệnh (CLI) chuẩn production, hiệu năng cao giúp tự động hóa quá trình phân tích, thống kê, xuất báo cáo dữ liệu và trực quan hóa các lỗi hệ thống (`ERROR`, `CRITICAL`) từ các tệp log.

Dự án được xây dựng tuân thủ đầy đủ các tiêu chuẩn kỹ thuật phần mềm hiện đại: **Pandas Vectorization**, **Pytest (Coverage >90%)**, **Pre-commit Hooks**, **Docker Containerization**, và **GitHub Actions CI/CD**.

---

## 📌 Các Tính Năng Nổi Bật

- **⚡ Xử lý dữ liệu tốc độ cao**: Sử dụng **Pandas Vectorization** giúp tối ưu hóa hiệu năng phân tích tập log lớn.
- **🛠️ Giao diện CLI linh hoạt**: Hỗ trợ truyền tham số dòng lệnh bằng `argparse` (`--input`, `--output-dir`, `--verbose`).
- **📊 Trực quan hóa chuẩn công bố**: Tự động tạo biểu đồ thống kê mức độ lỗi với **Seaborn & Matplotlib**.
- **📁 Xuất báo cáo đa định dạng**: Tự động xuất kết quả thống kê ra các tệp dữ liệu chuẩn **CSV** (`summary.csv`) và **JSON** (`summary.json`).
- **🛡️ Tự động hóa & Kiểm soát chất lượng**:
  - Quản lý mã nguồn với **Ruff** (Linter & Formatter) và **Mypy** (Static Type Checking).
  - Tự động kiểm tra chất lượng mã trước khi commit qua **Pre-commit Hooks**.
- **🐳 Đóng gói Container**: Hỗ trợ chạy ứng dụng nhất quán trên mọi môi trường bằng **Docker** & **Docker Compose**.
- **🔄 Tự động hóa CI/CD**: Workflow **GitHub Actions** tự động linting, type-checking, chạy unit tests và build Docker image mỗi khi `push` hoặc tạo `Pull Request`.

---

## 📂 Cấu Trúc Dự Án

```text
log_pipeline/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD Workflow
├── reports/                   # Thư mục chứa báo cáo CSV, JSON & biểu đồ
│   ├── error_report.png
│   ├── summary.csv
│   └── summary.json
├── app.log                    # File log mẫu đầu vào
├── Dockerfile                 # File đóng gói Docker image
├── docker-compose.yml         # File cấu hình Docker Compose
├── main.py                    # Entrypoint chính của công cụ CLI
├── pyproject.toml             # Khai báo cấu hình dự án & Python CLI Package
├── README.md                  # Hướng dẫn sử dụng dự án
├── requirements.txt           # Danh sách các thư viện phụ thuộc
├── run_pipeline.sh            # Kịch bản Bash điều khiển pipeline tự động
├── test_main.py               # Bộ Unit Tests (Pytest)
├── visualize.py               # Module vẽ biểu đồ trực quan hóa
└── .pre-commit-config.yaml   # Cấu hình Pre-commit hooks
```

---

## 🛠️ Hướng Dẫn Cài Đặt

### 1. Yêu cầu hệ thống
- **Python 3.12+**
- **Git**
- **Docker & Docker Compose** (Tùy chọn)

### 2. Cài đặt môi trường cục bộ (Local Setup)

```bash
# Clone repository
git clone https://github.com/Ulyssesllc/log_pipeline.git
cd log_pipeline

# Khởi tạo và kích hoạt môi trường ảo Python
python3 -m venv venv
source venv/bin/activate

# Cài đặt dự án ở chế độ Editable CLI
pip install -e .

# Cài đặt pre-commit hooks
pre-commit install
```

---

## 🚀 Hướng Dẫn Sử Dụng

### 1. Sử dụng lệnh CLI (`log-pipeline`)

Sau khi cài đặt gói thành công, bạn có thể gọi trực tiếp lệnh `log-pipeline` từ bất kỳ đâu:

```bash
# Chạy với tham số mặc định (đọc app.log và lưu báo cáo vào ./reports)
log-pipeline

# Chạy với các tùy chọn tùy chỉnh
log-pipeline --input /path/to/custom.log --output-dir ./my_reports --verbose

# Xem hướng dẫn tham số dòng lệnh
log-pipeline --help
```

### 2. Chạy toàn bộ Pipeline tự động bằng Bash Script

```bash
./run_pipeline.sh
```

### 3. Chạy ứng dụng bằng Docker & Docker Compose

```bash
# Khởi chạy pipeline trong Docker container
docker-compose up --build
```

---

## 🧪 Kiểm Thử & Kiểm Soát Chất Lượng (Quality Control)

### 1. Chạy Unit Tests & Đo Code Coverage với `pytest`

```bash
pytest --cov=main --cov-report=term-missing
```

### 2. Kiểm tra định dạng & Static Type Check

```bash
# Kiểm tra linter và định dạng mã nguồn
ruff check .
ruff format --check .

# Kiểm tra kiểu dữ liệu tĩnh
mypy .

# Chạy toàn bộ pre-commit hooks thủ công
pre-commit run --all-files
```

---

## 🔄 Luồng CI/CD (GitHub Actions)

Dự án được cấu hình sẵn luồng Tích hợp Liên tục (CI) trong tệp `.github/workflows/ci.yml`. Mỗi khi bạn thực hiện `push` hoặc tạo `Pull Request` lên nhánh `main`, GitHub Actions sẽ tự động kích hoạt máy ảo Ubuntu để thực hiện 2 công việc:

1. **`test-and-lint`**: Cài đặt phụ thuộc, chạy `ruff`, `mypy`, và `pytest` kiểm thử tự động.
2. **`docker-build`**: Xây dựng thử nghiệm Docker Image để đảm bảo môi trường đóng gói không bị vỡ.

---

## 📄 Giấy Phép (License)

Dự án được phân phối dưới giấy phép **MIT License**.
