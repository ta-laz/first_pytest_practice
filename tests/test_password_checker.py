from lib.password_checker import * 
import pytest 

def test_if_password_is_valid(): 
    password = PasswordChecker()
    assert password.check("123456789") == True

def test_if_password_is_invalid(): 
    password = PasswordChecker()
    with pytest.raises(Exception) as e: 
        password.check("123")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."