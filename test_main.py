from main import validate_and_parse 
def test_parse_valid_log() -> None: 
    # Test case chuẩn (Typical case) 
    line = "2026-09-21 ERROR Database_timeout" 
    result = validate_and_parse(line) 
    assert result["level"] == "ERROR" 
    assert result["message"] == "Database_timeout" 

def test_parse_empty_line_raises_error() -> None: 
    # Test case biên: Dòng rỗng / AssertionError (Boundary condition) 
    try: 
        validate_and_parse("") 
        assert False, "Phải quăng lỗi khi dòng log rỗng!" 
    except (AssertionError, ValueError): 
        assert True 

if __name__ == "__main__": 
    test_parse_valid_log() 
    test_parse_empty_line_raises_error() 
    print("Tất cả các bài Unit Test đều PASSED!")
