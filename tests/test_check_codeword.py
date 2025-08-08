from lib.check_codeword import *

def test_check_if_horse_works(): 
    result = check_codeword("horse")
    assert result == "Correct! Come in."
    
def test_check_if_invalid_password(): 
    result = check_codeword("bird")
    assert result == "WRONG!"
    
def test_check_if_almost_correct(): 
    result = check_codeword("hulke")
    assert result == "Close, but nope."