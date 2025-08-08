from lib.report_length import *

def test_check_len_dog(): 
    result = report_length("dog")
    assert result == "This string was 3 characters long."

def test_check_len_bicycle(): 
    result = report_length("bicycle")
    assert result == "This string was 7 characters long."

def test_check_len_watashiwa(): 
    result = report_length("watashiwa")
    assert result == "This string was 9 characters long."