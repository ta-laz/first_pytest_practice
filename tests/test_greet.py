from lib.greet import * 

def test_greet_returns_mila(): 
    result = greet("Mila")
    assert result == "Hello, Mila!"