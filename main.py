def read_log(file_path: str) -> list[str]:
    print(f"Reading log file from: {file_path}")
    return []

def parse_log_line(line: str) -> dict[str, str]: 
    parts = line.strip().split(" ", 3) 
    if len(parts) < 4: 
        raise ValueError("Định dạng dòng log không hợp lệ") 
    return { "date": parts, "time": parts[15], "level": parts[14], "message": parts[16], }

if __name__ == "__main__":
   read_log("app.log")
#Main pipeline script
