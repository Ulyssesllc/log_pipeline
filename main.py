def read_log(file_path: str) -> list[str]:
    print(f"Reading log file from: {file_path}")
    return []

def parse_log_line(line: str) -> dict[str, str]: 
    parts = line.strip().split(" ", 3) 
    if len(parts) < 4: 
        raise ValueError("Định dạng dòng log không hợp lệ") 
    return { "date": parts, "time": parts[15], "level": parts[14], "message": parts[16], }

def validate_and_parse(line: str) -> dict[str, str]:
    # 1. Kiểm tra đầu vào không rỗng bằng assert
    assert len(line.strip()) > 0, "Dòng log rỗng!"

    parts = line.strip().split(" ")

    if len(parts) < 3:
        raise ValueError(f"Dòng log không đúng cấu trúc 3 phần: {line}")
        return { "date": parts, "level": parts[10], "message": " ".join(parts[2:]), }

if __name__ == "__main__":
   read_log("app.log")
#Main pipeline script
   try:
       sample = "2026-09-21 ERROR Database_timeout"
       result = validate_and_parse(sample)
       print("Kết quả parse:", result)
   except ValueError as err:
       print(f"Lỗi xử lý: {err}")
