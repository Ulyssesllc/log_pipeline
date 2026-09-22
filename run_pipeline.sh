#!/usr/bin/env bash 
set -euo pipefail

echo "==> Bắt đầu pipeline tự động..."
LOG_FILE="app.log"

#Kiểm tra file log có tồn tại không 
if [[ ! -f "LOG_FILE" ]]; then
   echo "Tạo file log mẫu ..."
   echo "2026-09-21 ERROR Database_connection_failed" > "$LOG_FILE"
fi

#Chạy python script xử lí dữ liệu
python3 main.py
echo "==> Pipeline hoàn tất thành công!"
