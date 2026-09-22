#!/usr/bin/env bash 
set -euo pipefail 

echo "==========================================" 
echo " STARTING LOG PROCESSING PIPELINE" 
echo "==========================================" 

# 1. Kích hoạt môi trường ảo nếu có 
if [ -d "venv" ]; then 
   source venv/bin/activate 
fi 

# 2. Tạo file app.log mẫu nếu chưa tồn tại 
if [ ! -f "app.log" ]; then 
   echo "Creating sample app.log..." 
   cat << 'LOG' > app.log
2026-09-21 10:00:00 INFO System_started 
2026-09-21 10:01:15 ERROR Database_timeout 
2026-09-21 10:02:30 CRITICAL Out_of_memory 
2026-09-21 10:03:10 ERROR Connection_failed 
LOG
fi 

# 3. Chạy Unit Tests kiểm tra tính đúng đắn của hàm 
echo "--> Running Unit Tests..." 
python3 test_main.py 

# 4. Chạy chương trình xử lý log chính 
echo "--> Running Main Pipeline..." 
python3 main.py 

echo "==========================================" 
echo " PIPELINE EXECUTED SUCCESSFULLY!" 
echo "=========================================="
