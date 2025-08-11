from lib.present import * 
import pytest 

def test_if_present_init(): 
    my_present = Present() 
    assert my_present.contents == None

def test_if_wrapped_works_correctly(): 
    my_present = Present() 
    my_present.wrap("box")
    assert my_present.contents == "box"

def test_if_wrapped_error_correct(): 
    my_present = Present()
    my_present.wrap("box")
    with pytest.raises(Exception) as e: 
        my_present.wrap("toy")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_if_unwrap_works_correctly(): 
    my_present = Present()
    my_present.wrap("box")
    assert my_present.unwrap() == "box"

def test_if_unwrapped_error_correct(): 
    my_present = Present()
    with pytest.raises(Exception) as e: 
        my_present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped." 

def test_if_wrap_and_then_unwrap(): 
    my_present = Present()
    my_present.wrap("book")
    assert my_present.unwrap() == "book"